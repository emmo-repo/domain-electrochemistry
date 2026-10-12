"""Every deprecated term must keep its entry in the generated class index.

A term IRI such as https://w3id.org/emmo/domain/electrochemistry#electrochemistry_...
resolves through the w3id 303 to the class index page, and the fragment is the
term's element id on that page. Dropping deprecated terms from the index would
therefore break dereferencing for every one of them while the request still
returns 200. The generator keeps them (flagged and sorted last); this test
checks the generated file that CI commits.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import rdflib
from rdflib import OWL, SKOS, URIRef

REPO = Path(__file__).parents[1]
INDEX_RST = REPO / "docs" / "electrochemistry.rst"
SOURCE_TTL = (
    [REPO / "electrochemistry.ttl"]
    + sorted((REPO / "reference").glob("electrochemistry-*.ttl"))
    + sorted((REPO / "modules").glob("electrochemistry-*.ttl"))
)


def _graph() -> rdflib.Graph:
    g = rdflib.Graph()
    for path in SOURCE_TTL:
        g.parse(path, format="turtle")
    return g


SRC = _graph()
INDEX = INDEX_RST.read_text(encoding="utf-8")
DEPRECATED = sorted(
    s
    for s in SRC.subjects(OWL.deprecated, None)
    if isinstance(s, URIRef) and "#" in str(s)
    and str(SRC.value(s, OWL.deprecated)).lower() in ("true", "1")
)


def _label(s: URIRef) -> str:
    return str(SRC.value(s, SKOS.prefLabel) or s)


def test_index_present():
    assert INDEX.count('<div id="') > 100, "class index looks empty - scan is broken"


@pytest.mark.parametrize("term", DEPRECATED, ids=[_label(s) for s in DEPRECATED])
def test_deprecated_term_keeps_its_anchor(term: URIRef):
    fragment = str(term).split("#", 1)[1]
    assert f'<div id="{fragment}">' in INDEX, (
        f"{_label(term)} has no entry in docs/electrochemistry.rst; its IRI no longer dereferences to a description"
    )
