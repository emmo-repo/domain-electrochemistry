"""bump_version — bump the version of the domain-electrochemistry ontology.

Updates all owl:versionIRI, owl:imports, owl:versionInfo, and XML catalog entries
that reference the current ontology version, and advances owl:priorVersion /
owl:backwardCompatibleWith to point at the version being superseded.

Usage (after pip install -e .):
    bump-version --minor             # 0.33.0 → 0.34.0
    bump-version --patch             # 0.33.0 → 0.33.1
    bump-version --major             # 0.33.0 → 1.0.0
    bump-version --version 0.35.0    # set explicit target version
    bump-version --minor --dry-run   # preview changes without writing
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path


# ── file lists ──────────────────────────────────────────────────────────────

# TTL files that carry versioned URIs (owl:versionIRI, owl:imports) and/or
# an owl:versionInfo literal for the electrochemistry domain version.
TTL_FILES = [
    "electrochemistry.ttl",
    "electrochemistry-dependencies.ttl",
    "modules/electrochemistry-manufacturing.ttl",
    "modules/electrochemistry-testing.ttl",
    "reference/electrochemistry-reference.ttl",
    "reference/electrochemistry-quantities.ttl",
]

# OASIS XML catalog files that map versioned IRIs to local paths.
CATALOG_FILES = [
    "catalog-v001.xml",
    "application/catalog-v001.xml",
]

# electrochemistry-inferred.ttl is auto-generated — skip it.
_SKIPPED = ["electrochemistry-inferred.ttl"]

# URI segment that identifies electrochemistry domain version paths.
_ECHEM_SEGMENT = "emmo/domain/electrochemistry/"


# ── helpers ──────────────────────────────────────────────────────────────────

def find_repo_root() -> Path:
    """Walk up from cwd until we find the directory containing electrochemistry.ttl."""
    for directory in [Path.cwd(), *Path.cwd().parents]:
        if (directory / "electrochemistry.ttl").exists():
            return directory
    raise RuntimeError(
        "Cannot locate repository root.\n"
        "Run bump-version from within the domain-electrochemistry repository."
    )


def get_current_version(repo_root: Path) -> str:
    ttl = (repo_root / "electrochemistry.ttl").read_text(encoding="utf-8")
    m = re.search(r'owl:versionInfo\s+"(\d+\.\d+\.\d+)"', ttl)
    if not m:
        raise RuntimeError(
            "Could not determine the current version from electrochemistry.ttl.\n"
            "Expected a line like: owl:versionInfo \"X.Y.Z\""
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


def _is_prior_version_line(line: str) -> bool:
    """True for owl:priorVersion and owl:backwardCompatibleWith triples in domain TTL files."""
    return (
        ("owl:priorVersion" in line or "owl:backwardCompatibleWith" in line)
        and _ECHEM_SEGMENT in line
    )


def update_content(
    content: str, old_ver: str, new_ver: str
) -> tuple[str, list[tuple[int, str, str]]]:
    """Apply version substitutions to *content*, returning (new_content, changes).

    Per-line strategy
    -----------------
    owl:priorVersion / owl:backwardCompatibleWith lines
        Replace *any* existing version segment with ``old_ver``.
        Rationale: these triples record provenance (the release being superseded),
        so after a bump they should always point at the version we're replacing,
        regardless of what they pointed to before.

    All other lines
        Replace ``electrochemistry/{old_ver}/`` with ``electrochemistry/{new_ver}/``.
        Replace ``owl:versionInfo "{old_ver}"`` with ``owl:versionInfo "{new_ver}"``.
    """
    changes: list[tuple[int, str, str]] = []
    out: list[str] = []

    for i, line in enumerate(content.splitlines(keepends=True), 1):
        if _is_prior_version_line(line):
            new_line = re.sub(
                r"(emmo/domain/electrochemistry/)([^/\"'>]+)(/)",
                rf"\g<1>{old_ver}\3",
                line,
            )
        else:
            new_line = line.replace(
                f"electrochemistry/{old_ver}/",
                f"electrochemistry/{new_ver}/",
            )
            new_line = new_line.replace(
                f'owl:versionInfo "{old_ver}"',
                f'owl:versionInfo "{new_ver}"',
            )

        if new_line != line:
            changes.append((i, line.rstrip("\n"), new_line.rstrip("\n")))
        out.append(new_line)

    return "".join(out), changes


def process_file(
    repo_root: Path, rel_path: str, old_ver: str, new_ver: str, dry_run: bool
) -> list[tuple[int, str, str]]:
    path = repo_root / rel_path
    if not path.exists():
        print(f"  WARNING: {rel_path} not found — skipping.", file=sys.stderr)
        return []

    content = path.read_text(encoding="utf-8")
    new_content, changes = update_content(content, old_ver, new_ver)

    if changes and not dry_run:
        path.write_text(new_content, encoding="utf-8")

    return changes


# ── CLI entry point ──────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="bump-version",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Files updated
            -------------
            TTL ontology files  : electrochemistry.ttl, electrochemistry-dependencies.ttl,
                                  modules/electrochemistry-{manufacturing,testing}.ttl,
                                  reference/electrochemistry-{reference,quantities}.ttl
            XML catalog files   : catalog-v001.xml, application/catalog-v001.xml
            Skipped (generated) : electrochemistry-inferred.ttl
        """),
    )
    bump_group = parser.add_mutually_exclusive_group(required=True)
    bump_group.add_argument("--major", action="store_true", help="X.y.z → X+1.0.0")
    bump_group.add_argument("--minor", action="store_true", help="x.Y.z → x.Y+1.0")
    bump_group.add_argument("--patch", action="store_true", help="x.y.Z → x.y.Z+1")
    bump_group.add_argument("--version", metavar="X.Y.Z", help="Set an explicit target version")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing any files",
    )

    args = parser.parse_args(argv)

    repo_root = find_repo_root()
    old_ver = get_current_version(repo_root)

    if args.version:
        if not re.fullmatch(r"\d+\.\d+\.\d+", args.version):
            sys.exit(f"Error: --version must be X.Y.Z (e.g. 1.2.3), got {args.version!r}")
        new_ver = args.version
    elif args.major:
        new_ver = calc_new_version(old_ver, "major")
    elif args.minor:
        new_ver = calc_new_version(old_ver, "minor")
    else:
        new_ver = calc_new_version(old_ver, "patch")

    if old_ver == new_ver:
        print(f"Version is already {new_ver} — nothing to do.")
        return

    mode = "DRY RUN" if args.dry_run else "BUMPING"
    print(f"{mode}: {old_ver} → {new_ver}\n")

    total_lines_changed = 0
    files_changed = 0

    for rel_path in [*TTL_FILES, *CATALOG_FILES]:
        changes = process_file(repo_root, rel_path, old_ver, new_ver, args.dry_run)
        if not changes:
            continue
        files_changed += 1
        total_lines_changed += len(changes)
        n = len(changes)
        print(f"  {rel_path}  ({n} line{'s' if n != 1 else ''}):")
        for lineno, old_line, new_line in changes:
            print(f"    L{lineno}  {old_line.strip()}")
            print(f"        → {new_line.strip()}")
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
        print(
            f"Done: {total_lines_changed} line(s) updated across {files_changed} file(s).\n"
        )
        print("Suggested next steps:")
        print(f"  git add -u")
        print(f"  git commit -m 'chore: bump ontology version to {new_ver}'")
        print(f"  git tag v{new_ver}")


if __name__ == "__main__":
    main()
