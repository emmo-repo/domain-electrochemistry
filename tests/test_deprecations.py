"""Deprecated terms must leave nobody without a successor.

CONTRIBUTING (Term Lifecycle) asks that a deprecated term carries
``owl:deprecated true`` plus ``dcterms:isReplacedBy`` when a replacement exists,
or an ``rdfs:comment`` starting ``Deprecated in X.Y.Z:`` explaining why not.
Terms deprecated before that convention are listed in ``deprecated_baseline.txt``
and tolerated; the baseline may only shrink.

Deprecated terms keep their prefLabel (so the IRI stays in the JSON-LD context
and existing data keeps resolving) and, when they are defined classes, their
``owl:equivalentClass`` must be an intersection that includes the replacement,
so old data still classifies under the successor (issue #192).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import rdflib
from rdflib import OWL, RDFS, SKOS, URIRef
from rdflib.namespace import DCTERMS

REPO = Path(__file__).parents[1]
# CONTRIBUTING: rdfs:comment "Deprecated in X.Y.Z: <reason>"
DEPRECATION_COMMENT_RE = re.compile(r"^Deprecated in \d+\.\d+\.\d+:")
BASELINE_FILE = Path(__file__).parent / "deprecated_baseline.txt"
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
BASELINE = {
    line.strip()
    for line in BASELINE_FILE.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
}
DEPRECATED = sorted(
    s
    for s in SRC.subjects(OWL.deprecated, None)
    if isinstance(s, URIRef) and str(SRC.value(s, OWL.deprecated)).lower() in ("true", "1")
)


def _label(s: URIRef) -> str:
    return str(SRC.value(s, SKOS.prefLabel) or s)


def _has_successor_or_reason(s: URIRef) -> bool:
    if list(SRC.objects(s, DCTERMS.isReplacedBy)):
        return True
    return any(DEPRECATION_COMMENT_RE.match(str(c)) for c in SRC.objects(s, RDFS.comment))


def _members_of_intersection(expr) -> set:
    members = set()
    for inter in SRC.objects(expr, OWL.intersectionOf):
        for item in SRC.items(inter):
            members.add(item)
    return members


def test_scan_found_deprecations():
    assert DEPRECATED, "no deprecated terms found - scan is broken"


def test_baseline_only_shrinks():
    still_needed = {str(s) for s in DEPRECATED if not _has_successor_or_reason(s)}
    stale = BASELINE - still_needed
    assert not stale, (
        "these baseline entries are no longer needed (fixed or no longer deprecated); "
        "remove them from tests/deprecated_baseline.txt: " + ", ".join(sorted(stale))
    )


@pytest.mark.parametrize("term", DEPRECATED, ids=[_label(s) for s in DEPRECATED])
def test_deprecated_term_has_successor_or_reason(term: URIRef):
    if str(term) in BASELINE:
        pytest.skip("legacy deprecation, tolerated by baseline")
    assert _has_successor_or_reason(term), (
        f"{_label(term)} is deprecated without dcterms:isReplacedBy or an "
        "rdfs:comment starting 'Deprecated in X.Y.Z:'"
    )


@pytest.mark.parametrize("term", DEPRECATED, ids=[_label(s) for s in DEPRECATED])
def test_deprecated_term_keeps_pref_label(term: URIRef):
    assert SRC.value(term, SKOS.prefLabel) is not None, (
        f"{term} lost its prefLabel; the IRI would drop out of the JSON-LD context"
    )


DEFINED_DEPRECATED = [s for s in DEPRECATED if list(SRC.objects(s, OWL.equivalentClass))]


@pytest.mark.parametrize(
    "term", DEFINED_DEPRECATED, ids=[_label(s) for s in DEFINED_DEPRECATED]
)
def test_defined_deprecated_term_is_subsumed_by_its_replacement(term: URIRef):
    """The defining intersection must name the replacement, so old data classifies under it."""
    replacements = set(SRC.objects(term, DCTERMS.isReplacedBy))
    assert replacements, f"{_label(term)} has a defining axiom but no dcterms:isReplacedBy"
    for expr in SRC.objects(term, OWL.equivalentClass):
        members = _members_of_intersection(expr)
        assert members & replacements, (
            f"{_label(term)}: owl:equivalentClass intersection does not include its replacement"
        )
    # CONTRIBUTING: deprecated classes also subclass their replacements, so
    # existing uses still classify without a reasoner.
    assert replacements & set(SRC.objects(term, RDFS.subClassOf)), (
        f"{_label(term)} does not rdfs:subClassOf its replacement"
    )
