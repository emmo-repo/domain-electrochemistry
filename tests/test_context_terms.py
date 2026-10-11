"""Guard the generated JSON-LD context against label leaks and lost terms.

``context/context.json`` is generated from the prefLabels in the import
closure (``generate_jsonld_context`` in ``.github/scripts/ontology_toolkit.py``),
plus the values of the domain's ``formerLabel`` annotation property so that
data written against a spelling that was later corrected keeps expanding
(issue #193).

Three things must hold:

- every ``formerLabel`` value is a context term that maps to the same IRI as
  the class's current prefLabel;
- no raw cycler column name leaks into the context, whether it is carried by
  a plain ``skos:hiddenLabel`` or by one of the vendor label properties
  (``maccorLabel``, ``newareLabel``, ...), all of which are sub-properties of
  ``skos:hiddenLabel`` and must stay out (issue #194);
- every prefLabel declared in this domain's own source files is a context term.

The hidden-label check compares raw column names against context keys, so a
vendor column that happens to be spelled like a real prefLabel (``Voltage``)
would trip it; none does today. If that happens, the column name is the thing
to question, not the test.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import rdflib
from rdflib import OWL, RDF, RDFS, SKOS

REPO = Path(__file__).parents[1]
CONTEXT_FILE = REPO / "context" / "context.json"
SOURCE_TTL = (
    [REPO / "electrochemistry.ttl"]
    + sorted((REPO / "reference").glob("electrochemistry-*.ttl"))
    + sorted((REPO / "modules").glob("electrochemistry-*.ttl"))
)


def _source_graph() -> rdflib.Graph:
    g = rdflib.Graph()
    for rel in SOURCE_TTL:
        g.parse(rel, format="turtle")
    return g


def _context() -> dict:
    return json.load(CONTEXT_FILE.open(encoding="utf-8"))["@context"]


def _iri_of(entry) -> str:
    return entry["@id"] if isinstance(entry, dict) else entry


SRC = _source_graph()
CTX = _context()


def _props_with_label(label: str):
    for lit in (rdflib.Literal(label, lang="en"), rdflib.Literal(label)):
        yield from SRC.subjects(SKOS.prefLabel, lit)


FORMER_LABEL_PROPS = list(_props_with_label("formerLabel"))
FORMER_LABELS = sorted(
    (str(o), str(s)) for p in FORMER_LABEL_PROPS for s, o in SRC.subject_objects(p)
)

HIDDEN_PROPS = [SKOS.hiddenLabel] + [
    p for p in SRC.subjects(RDFS.subPropertyOf, SKOS.hiddenLabel) if p not in FORMER_LABEL_PROPS
]
HIDDEN_VALUES = sorted(
    {str(o) for p in HIDDEN_PROPS for o in SRC.objects(None, p)}
)

PREF_LABELS = sorted(
    (str(o), str(s))
    for s, o in SRC.subject_objects(SKOS.prefLabel)
    if (s, RDF.type, OWL.Class) in SRC or (s, RDF.type, OWL.ObjectProperty) in SRC
)


def test_former_label_property_declared():
    assert len(FORMER_LABEL_PROPS) == 1, "exactly one formerLabel annotation property expected"
    prop = FORMER_LABEL_PROPS[0]
    assert (prop, RDFS.subPropertyOf, SKOS.hiddenLabel) in SRC


def test_scan_found_labels():
    assert FORMER_LABELS, "no formerLabel values found - scan is broken"
    assert HIDDEN_VALUES, "no hidden labels found - scan is broken"


@pytest.mark.parametrize("label, iri", FORMER_LABELS, ids=[l for l, _ in FORMER_LABELS])
def test_former_label_resolves_in_context(label: str, iri: str):
    assert label in CTX, f"former label {label!r} missing from context - old data stops expanding"
    assert _iri_of(CTX[label]) == iri, f"former label {label!r} maps to a different IRI than its class"


@pytest.mark.parametrize("value", HIDDEN_VALUES)
def test_hidden_label_not_in_context(value: str):
    """Raw cycler column names must never become JSON-LD terms."""
    assert value not in CTX, f"hidden label {value!r} leaked into the context"


def test_every_pref_label_in_context():
    """Adding or renaming a term means updating context/context.json in the same PR.

    CI regenerates the context only on master, so a PR to dev that adds a class
    without adding its prefLabel to the context would publish a term that does
    not expand. Add the entry by hand in sorted position, or regenerate with
    ``python .github/scripts/ontology_toolkit.py --generate-context`` against a
    squashed build (see CONTRIBUTING).
    """
    missing = sorted(label for label, _ in PREF_LABELS if label not in CTX)
    assert not missing, (
        f"{len(missing)} prefLabel(s) are not context terms: " + ", ".join(missing)
    )
