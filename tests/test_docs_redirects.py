"""Validate the redirect stubs under ``docs/_redirects``.

Pages that once existed on the published site (``pages/electrochemistry.html``,
``pages/get-started.html``, ...) are still linked from outside the repository.
Sphinx copies everything under ``docs/_redirects`` (``html_extra_path``) into
the build root, so each stub keeps the old URL alive with a meta-refresh to the
new location (issue #186).

This test checks that every stub is wired into ``conf.py``, carries a
meta-refresh, and points at a page that a docs source will actually produce -
otherwise the redirect would just move the 404 one hop further.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS_DIR = Path(__file__).parents[1] / "docs"
REDIRECTS_DIR = DOCS_DIR / "_redirects"

REFRESH_RE = re.compile(
    r'<meta\s+http-equiv="refresh"\s+content="0;\s*url=(?P<url>[^"]+)"', re.IGNORECASE
)

SOURCE_SUFFIXES = (".rst", ".ipynb")

STUBS = sorted(REDIRECTS_DIR.rglob("*.html"))


def test_extra_path_configured():
    conf = (DOCS_DIR / "conf.py").read_text(encoding="utf-8")
    assert re.search(r"^html_extra_path\s*=\s*\[.*'_redirects'.*\]", conf, re.MULTILINE), (
        "docs/conf.py must list '_redirects' in html_extra_path, "
        "otherwise the stubs never reach the built site"
    )


def test_stubs_exist():
    assert STUBS, "no redirect stubs found under docs/_redirects - scan is broken"


@pytest.mark.parametrize(
    "stub", STUBS, ids=[s.relative_to(REDIRECTS_DIR).as_posix() for s in STUBS]
)
def test_stub_target_exists(stub: Path):
    match = REFRESH_RE.search(stub.read_text(encoding="utf-8"))
    assert match, f"{stub.name} has no meta-refresh"
    url = match.group("url").split("#", 1)[0]
    assert url.endswith(".html"), f"{stub.name} redirects to a non-page target {url!r}"
    # The stub sits at <build>/<relpath>; resolve the target relative to the
    # same path inside docs/, where the sources live.
    site_path = stub.relative_to(REDIRECTS_DIR)
    resolved = (DOCS_DIR / site_path).parent / url
    stem = resolved.resolve().with_suffix("")
    assert any(stem.with_suffix(s).is_file() for s in SOURCE_SUFFIXES), (
        f"{site_path.as_posix()} redirects to '{url}', which no docs source "
        "(.rst/.ipynb) will produce in the built site"
    )


@pytest.mark.parametrize(
    "stub", STUBS, ids=[s.relative_to(REDIRECTS_DIR).as_posix() for s in STUBS]
)
def test_stub_does_not_shadow_a_real_page(stub: Path):
    """A stub must not sit where Sphinx will also write a real page."""
    site_path = stub.relative_to(REDIRECTS_DIR)
    stem = (DOCS_DIR / site_path).with_suffix("")
    assert not any(stem.with_suffix(s).is_file() for s in SOURCE_SUFFIXES), (
        f"{site_path.as_posix()} is also produced by a docs source; "
        "the stub would overwrite or be overwritten by it"
    )
