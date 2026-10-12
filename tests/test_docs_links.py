"""Validate internal link targets in the Sphinx docs sources.

Grid-card ``:link:`` options (sphinx-design) are emitted into the built HTML
as raw hrefs, so Sphinx never checks them: a card pointing at a page that
does not exist builds cleanly and 404s in production (issue #186). This test
resolves every relative ``:link:`` target against the docs sources and fails
if the target page would not exist in the built site.

Directories named ``_deprecate`` are skipped: their content is unmaintained
and scheduled for removal.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS_DIR = Path(__file__).parents[1] / "docs"

LINK_RE = re.compile(r"^\s*:link:\s*(\S+)\s*$", re.MULTILINE)

# A target like foo.html is produced by foo.rst or foo.ipynb.
SOURCE_SUFFIXES = (".rst", ".ipynb")


def _rst_files():
    for path in sorted(DOCS_DIR.rglob("*.rst")):
        parts = path.relative_to(DOCS_DIR).parts
        if "_build" in parts or "_deprecate" in parts:
            continue
        yield path


def _iter_links():
    for rst in _rst_files():
        for match in LINK_RE.finditer(rst.read_text(encoding="utf-8")):
            yield rst, match.group(1)


def _is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "//"))


def _target_exists(rst: Path, target: str) -> bool:
    # Strip fragment and query before resolving.
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return True  # pure fragment, links within the same page
    resolved = (rst.parent / target).resolve()
    if target.endswith(".html"):
        stem = resolved.with_suffix("")
        return any(stem.with_suffix(s).is_file() for s in SOURCE_SUFFIXES)
    # Non-.html targets (e.g. notebooks or static assets) must exist as files.
    return resolved.is_file()


ALL_LINKS = list(_iter_links())


def test_docs_contain_links():
    """Guard against the scan silently going blind (e.g. docs moved)."""
    assert ALL_LINKS, "no :link: targets found under docs/ - scan is broken"


@pytest.mark.parametrize(
    "rst, target",
    ALL_LINKS,
    ids=[f"{r.relative_to(DOCS_DIR).as_posix()}:{t}" for r, t in ALL_LINKS],
)
def test_link_target_exists(rst, target):
    if _is_external(target):
        pytest.skip("external URL, not checked")
    assert _target_exists(rst, target), (
        f"{rst.relative_to(DOCS_DIR).as_posix()} links to '{target}', "
        "which no docs source (.rst/.ipynb) will produce in the built site"
    )
