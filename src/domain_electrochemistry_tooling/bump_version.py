"""bump_version — bump the version of an EMMO domain ontology.

This script is IDENTICAL across the EMMO domain repos (domain-chemical-substance,
domain-electrochemistry, domain-battery).  Domain-specific knowledge lives in the
``version_tooling`` section of ``config.yml`` at the repository root:

    version_tooling:
      main_ttl: battery.ttl            # file that carries the canonical owl:versionInfo
      ttl_files:                       # TTLs carrying versioned URIs / versionInfo
        - battery.ttl
        - battery-dependencies.ttl
      catalog_files:                   # OASIS XML catalogs mapping versioned IRIs
        - catalog-v001.xml
      uri_segments:                    # URI segments owned by this domain
        - "emmo/domain/battery/"

Updates all owl:versionIRI, owl:imports, owl:versionInfo and XML catalog entries
that reference the current version; advances owl:priorVersion /
owl:backwardCompatibleWith (string-literal and IRI forms) to record the version
being superseded; refreshes dcterms:issued / dcterms:modified to today.

Usage (after pip install -e ., or via python src/<pkg>/bump_version.py):
    bump-version --minor             # 0.18.7 -> 0.19.0
    bump-version --patch             # 0.18.7 -> 0.18.8
    bump-version --major             # 0.18.7 -> 1.0.0
    bump-version --version 0.20.0    # set explicit target version
    bump-version --minor --dry-run   # preview changes without writing
    bump-version --no-dates --patch  # don't touch dcterms:issued/modified
    bump-version --check             # verify version consistency; exit 1 on drift
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
import textwrap
from pathlib import Path

import yaml

SEMVER = re.compile(r"\d+\.\d+\.\d+")
PRIOR_PROPS = ("owl:priorVersion", "owl:backwardCompatibleWith")


# ── configuration ────────────────────────────────────────────────────────────

def find_repo_root() -> Path:
    """Walk up from cwd until we find a config.yml with a version_tooling section."""
    for directory in [Path.cwd(), *Path.cwd().parents]:
        cfg = directory / "config.yml"
        if cfg.exists():
            data = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
            if "version_tooling" in data:
                return directory
    raise SystemExit(
        "Cannot locate repository root: no config.yml with a version_tooling "
        "section found in this or any parent directory."
    )


def load_config(repo_root: Path) -> dict:
    data = yaml.safe_load((repo_root / "config.yml").read_text(encoding="utf-8"))
    vt = data.get("version_tooling") or {}
    missing = [k for k in ("main_ttl", "ttl_files", "catalog_files", "uri_segments") if not vt.get(k)]
    if missing:
        raise SystemExit(f"config.yml version_tooling is missing keys: {', '.join(missing)}")
    return vt


def get_current_version(repo_root: Path, main_ttl: str) -> str:
    ttl = (repo_root / main_ttl).read_text(encoding="utf-8")
    m = re.search(r'owl:versionInfo\s+"(\d+\.\d+\.\d+)"', ttl)
    if not m:
        raise SystemExit(
            f"Could not determine the current version from {main_ttl}.\n"
            'Expected a line like: owl:versionInfo "X.Y.Z"'
        )
    return m.group(1)


def calc_new_version(old: str, bump: str) -> str:
    major, minor, patch = map(int, old.split("."))
    if bump == "major":
        return f"{major + 1}.0.0"
    if bump == "minor":
        return f"{major}.{minor + 1}.0"
    if bump == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"Unknown bump type: {bump!r}")


# ── rewriting ────────────────────────────────────────────────────────────────

def _is_prior_version_line(line: str) -> bool:
    return any(p in line for p in PRIOR_PROPS)


def update_content(
    content: str,
    old_ver: str,
    new_ver: str,
    segments: list[str],
    update_dates: bool,
    today: str,
) -> tuple[str, list[tuple[int, str, str]]]:
    """Apply version substitutions, returning (new_content, changes).

    Per-line strategy
    -----------------
    owl:priorVersion / owl:backwardCompatibleWith lines
        Point at the version being superseded (``old_ver``), handling both the
        string-literal form ("0.19.0") and the IRI form
        (<.../domain/x/0.19.0/x>) for segments owned by this domain.

    dcterms:issued / dcterms:modified lines (when update_dates)
        Set to today's date (release semantics: bump-version runs at release prep).

    All other lines
        Replace each owned ``{segment}{old_ver}/`` with the new version and
        ``owl:versionInfo "{old_ver}"`` with the new version.
    """
    changes: list[tuple[int, str, str]] = []
    out: list[str] = []

    for i, line in enumerate(content.splitlines(keepends=True), 1):
        if _is_prior_version_line(line):
            new_line = line
            if any(seg in line for seg in segments):
                # IRI form: rewrite the version inside the owned segment
                for seg in segments:
                    new_line = re.sub(
                        rf"({re.escape(seg)})(\d+\.\d+\.\d+)(/)",
                        rf"\g<1>{old_ver}\3",
                        new_line,
                    )
            elif '"' in line:
                # String-literal form
                new_line = re.sub(
                    rf'((?:{"|".join(PRIOR_PROPS)})\s+)"[^"]+"',
                    rf'\g<1>"{old_ver}"',
                    line,
                )
        elif update_dates and ("dcterms:issued" in line or "dcterms:modified" in line):
            new_line = re.sub(
                r'((?:dcterms:issued|dcterms:modified)\s+)"\d{4}-\d{2}-\d{2}"',
                rf'\g<1>"{today}"',
                line,
            )
        else:
            new_line = line
            for seg in segments:
                new_line = new_line.replace(f"{seg}{old_ver}/", f"{seg}{new_ver}/")
            new_line = new_line.replace(
                f'owl:versionInfo "{old_ver}"',
                f'owl:versionInfo "{new_ver}"',
            )

        if new_line != line:
            changes.append((i, line.rstrip("\n"), new_line.rstrip("\n")))
        out.append(new_line)

    return "".join(out), changes


def process_file(
    repo_root: Path,
    rel_path: str,
    old_ver: str,
    new_ver: str,
    segments: list[str],
    dry_run: bool,
    update_dates: bool,
    today: str,
) -> list[tuple[int, str, str]]:
    path = repo_root / rel_path
    if not path.exists():
        print(f"  WARNING: {rel_path} not found — skipping.", file=sys.stderr)
        return []

    content = path.read_text(encoding="utf-8")
    # Only TTLs carry dates; never touch dates in XML catalogs.
    dates = update_dates and rel_path.endswith(".ttl")
    new_content, changes = update_content(content, old_ver, new_ver, segments, dates, today)

    if changes and not dry_run:
        path.write_text(new_content, encoding="utf-8")

    return changes


# ── check mode ───────────────────────────────────────────────────────────────

def run_check(repo_root: Path, cfg: dict, current: str) -> int:
    """Verify that every owned versioned URI and versionInfo agrees with the
    canonical version. priorVersion/backwardCompatibleWith lines are exempt
    (they legitimately hold the previous version). Exit code 0 = consistent."""
    segments: list[str] = cfg["uri_segments"]
    problems: list[str] = []

    for rel_path in [*cfg["ttl_files"], *cfg["catalog_files"]]:
        path = repo_root / rel_path
        if not path.exists():
            problems.append(f"{rel_path}: listed in config.yml but not found")
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if _is_prior_version_line(line):
                continue
            for seg in segments:
                for m in re.finditer(rf"{re.escape(seg)}(\d+\.\d+\.\d+)/", line):
                    if m.group(1) != current:
                        problems.append(
                            f"{rel_path}:{i}: {seg}{m.group(1)}/ != current {current}"
                        )
            m = re.search(r'owl:versionInfo\s+"(\d+\.\d+\.\d+)"', line)
            if m and m.group(1) != current:
                problems.append(
                    f"{rel_path}:{i}: owl:versionInfo \"{m.group(1)}\" != current {current}"
                )

    if problems:
        print(f"VERSION DRIFT against canonical {current}:")
        for p in problems:
            print(f"  {p}")
        return 1
    print(f"OK: all owned version references agree with {current}.")
    return 0


# ── CLI entry point ──────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="bump-version",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            File lists are read from the version_tooling section of config.yml.
            Generated artifacts (*-inferred.ttl) must not be listed there — CI owns them.
        """),
    )
    bump_group = parser.add_mutually_exclusive_group(required=False)
    bump_group.add_argument("--major", action="store_true", help="X.y.z -> X+1.0.0")
    bump_group.add_argument("--minor", action="store_true", help="x.Y.z -> x.Y+1.0")
    bump_group.add_argument("--patch", action="store_true", help="x.y.Z -> x.y.Z+1")
    bump_group.add_argument("--version", metavar="X.Y.Z", help="Set an explicit target version")
    parser.add_argument("--check", action="store_true",
                        help="Verify version consistency across all listed files; exit 1 on drift")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print planned changes without writing any files")
    parser.add_argument("--no-dates", action="store_true",
                        help="Do not update dcterms:issued / dcterms:modified")

    args = parser.parse_args(argv)

    repo_root = find_repo_root()
    cfg = load_config(repo_root)
    old_ver = get_current_version(repo_root, cfg["main_ttl"])

    if args.check:
        sys.exit(run_check(repo_root, cfg, old_ver))

    if args.version:
        if not SEMVER.fullmatch(args.version):
            sys.exit(f"Error: --version must be X.Y.Z (e.g. 1.2.3), got {args.version!r}")
        new_ver = args.version
    elif args.major:
        new_ver = calc_new_version(old_ver, "major")
    elif args.minor:
        new_ver = calc_new_version(old_ver, "minor")
    elif args.patch:
        new_ver = calc_new_version(old_ver, "patch")
    else:
        parser.error("one of --major/--minor/--patch/--version/--check is required")

    if old_ver == new_ver:
        print(f"Version is already {new_ver} — nothing to do.")
        return

    today = datetime.date.today().isoformat()
    mode = "DRY RUN" if args.dry_run else "BUMPING"
    print(f"{mode}: {old_ver} -> {new_ver}\n")

    total_lines_changed = 0
    files_changed = 0

    for rel_path in [*cfg["ttl_files"], *cfg["catalog_files"]]:
        changes = process_file(
            repo_root, rel_path, old_ver, new_ver, cfg["uri_segments"],
            args.dry_run, not args.no_dates, today,
        )
        if not changes:
            continue
        files_changed += 1
        total_lines_changed += len(changes)
        n = len(changes)
        print(f"  {rel_path}  ({n} line{'s' if n != 1 else ''}):")
        for lineno, old_line, new_line in changes:
            print(f"    L{lineno}  {old_line.strip()}")
            print(f"        -> {new_line.strip()}")
        print()

    if total_lines_changed == 0:
        print("No version references found — nothing to update.")
        return

    if args.dry_run:
        print(
            f"Dry run complete: {total_lines_changed} line(s) in {files_changed} file(s) "
            "would be changed.\nRe-run without --dry-run to apply."
        )
    else:
        print(f"Done: {total_lines_changed} line(s) updated across {files_changed} file(s).\n")
        print("Suggested next steps:")
        print("  bump-version --check")
        print("  git add -u")
        print(f"  git commit -m 'chore: bump ontology version to {new_ver}'")
        print(f"  git tag v{new_ver}")


if __name__ == "__main__":
    main()
