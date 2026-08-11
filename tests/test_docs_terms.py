"""Lint ontology terms used in docs examples against the published context.

Every ``@type`` value, JSON-LD property key, and ``hasMeasurementUnit`` value
that appears in a JSON code block in the docs (or in a notebook source) must
resolve against ``context/context.json`` - otherwise the example silently
produces junk IRIs or drops data on expansion, while still looking correct
to readers.

Existing violations are recorded in ``docs_term_baseline.txt`` and tolerated
until the owning page is rewritten (docs cleanup phases 2-4); the test fails
only on NEW violations, so freshly written examples must be clean. When a
page is fixed, regenerate the baseline with:

    python tests/test_docs_terms.py --update-baseline

Directories named ``_build`` and ``_deprecate`` are skipped.
"""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

REPO = Path(__file__).parents[1]
DOCS_DIR = REPO / "docs"
CONTEXT_FILE = REPO / "context" / "context.json"
BASELINE_FILE = Path(__file__).parent / "docs_term_baseline.txt"

JSON_BLOCK_RE = re.compile(
    r"^(?P<indent>[ \t]*)\.\.\s+code-block::\s*(?:json|jsonld|json-ld)\s*$",
    re.MULTILINE,
)
# @type values and hasMeasurementUnit values inside notebook/python source.
NB_TYPE_RE = re.compile(r"""["']@type["']\s*:\s*(?P<val>\[[^\]]*\]|["'][^"']+["'])""")
NB_UNIT_RE = re.compile(r"""["']hasMeasurementUnit["']\s*:\s*["'](?P<val>[^"']+)["']""")

JSONLD_KEYWORDS = {
    "@context", "@type", "@id", "@value", "@language", "@graph", "@base",
    "@vocab", "@list", "@set", "@reverse", "@index", "@nest", "@none",
    "@container", "@prefix", "@version", "@direction", "@import", "@included",
    "@json", "@propagate", "@protected",
}


def _load_context():
    ctx = json.loads(CONTEXT_FILE.read_text(encoding="utf-8"))["@context"]
    terms = set(ctx)
    prefixes = {k for k, v in ctx.items()
                if isinstance(v, str) and v.endswith(("/", "#"))}
    return terms, prefixes


TERMS, PREFIXES = _load_context()


def _resolves(value: str) -> bool:
    """True if a term/key/CURIE resolves against the context."""
    if value.startswith(("http://", "https://", "urn:")):
        return True
    if ":" in value:
        prefix = value.split(":", 1)[0]
        # A CURIE resolves iff its prefix is defined; the remote vocabulary
        # itself is not validated here.
        return prefix in PREFIXES
    return value in TERMS


def _source_files():
    for pattern in ("*.rst", "*.ipynb"):
        for path in sorted(DOCS_DIR.rglob(pattern)):
            parts = path.relative_to(DOCS_DIR).parts
            if "_build" in parts or "_deprecate" in parts:
                continue
            yield path


def _json_blocks_from_rst(text):
    """Yield (json_text, is_valid) for each json code-block directive."""
    for match in JSON_BLOCK_RE.finditer(text):
        indent = match.group("indent")
        lines = []
        for line in text[match.end():].splitlines()[1:]:
            if line.strip() and not line.startswith(indent + " "):
                break
            lines.append(line)
        block = textwrap.dedent("\n".join(lines)).strip()
        # Drop directive options like :linenos: at the top of the block.
        block = re.sub(r"^(:\w+[^\n]*\n)+", "", block).strip()
        if block:
            yield block


def _check_jsonld_obj(obj, violations):
    """Recursively collect unresolvable @type values, keys, and units."""
    if isinstance(obj, list):
        for item in obj:
            _check_jsonld_obj(item, violations)
        return
    if not isinstance(obj, dict):
        return
    for key, value in obj.items():
        if key == "@type":
            types = value if isinstance(value, list) else [value]
            for t in types:
                if isinstance(t, str) and not _resolves(t):
                    violations.add(f"@type={t}")
        elif key == "hasMeasurementUnit" and isinstance(value, str):
            if not _resolves(value):
                violations.add(f"unit={value}")
        elif key not in JSONLD_KEYWORDS and not _resolves(key):
            violations.add(f"key={key}")
        _check_jsonld_obj(value, violations)


def _scan_file(path: Path) -> set[str]:
    violations: set[str] = set()
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".rst":
        for block in _json_blocks_from_rst(text):
            try:
                data = json.loads(block)
            except json.JSONDecodeError:
                violations.add("INVALID_JSON")
                continue
            # Only lint JSON-LD-shaped blocks; plain JSON snippets are fine.
            if isinstance(data, (dict, list)) and ("@type" in block or "@context" in block):
                _check_jsonld_obj(data, violations)
    else:  # .ipynb
        try:
            nb = json.loads(text)
        except json.JSONDecodeError:
            return {"INVALID_NOTEBOOK_JSON"}
        source = "".join(
            "".join(cell.get("source", []))
            for cell in nb.get("cells", [])
            if cell.get("cell_type") == "code"
        )
        for match in NB_TYPE_RE.finditer(source):
            raw = match.group("val")
            values = re.findall(r"""["']([^"']+)["']""", raw)
            for v in values:
                if not _resolves(v):
                    violations.add(f"@type={v}")
        for match in NB_UNIT_RE.finditer(source):
            if not _resolves(match.group("val")):
                violations.add(f"unit={match.group('val')}")
    return violations


def _all_violations() -> set[str]:
    found: set[str] = set()
    for path in _source_files():
        rel = path.relative_to(DOCS_DIR).as_posix()
        for v in _scan_file(path):
            found.add(f"{rel} :: {v}")
    return found


def _baseline() -> set[str]:
    if not BASELINE_FILE.is_file():
        return set()
    lines = BASELINE_FILE.read_text(encoding="utf-8").splitlines()
    return {ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")}


def test_no_new_unresolvable_terms():
    current = _all_violations()
    baseline = _baseline()
    new = sorted(current - baseline)
    assert not new, (
        "New unresolvable ontology terms in docs examples (not in "
        "context/context.json):\n  " + "\n  ".join(new)
        + "\nFix the term, or if intentional regenerate the baseline: "
        "python tests/test_docs_terms.py --update-baseline"
    )
    fixed = sorted(baseline - current)
    if fixed:
        print(f"\n{len(fixed)} baseline entries are now fixed and can be "
              "removed (run --update-baseline):")
        for entry in fixed[:20]:
            print(f"  {entry}")


if __name__ == "__main__":
    import sys
    if "--update-baseline" in sys.argv:
        entries = sorted(_all_violations())
        BASELINE_FILE.write_text(
            "# Known unresolvable terms in docs examples, tolerated until the\n"
            "# owning page is rewritten. Regenerate with:\n"
            "#   python tests/test_docs_terms.py --update-baseline\n"
            + "\n".join(entries) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {len(entries)} entries to {BASELINE_FILE}")
    else:
        for entry in sorted(_all_violations()):
            print(entry)
