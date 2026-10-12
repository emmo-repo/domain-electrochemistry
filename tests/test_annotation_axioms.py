"""Every owl:Axiom reification must annotate a triple that exists in the sources.

The modules carry ``dcterms:source`` on elucidations and comments through
OWL 2 annotation axioms (``owl:Axiom`` with ``annotatedSource`` /
``annotatedProperty`` / ``annotatedTarget``). When the annotated literal is
edited but the reification is not, the reification is orphaned: rdflib and
owlready2 ignore it, but the OWL API (ROBOT, Protégé) rebuilds the old triple
from it, so the retired text reappears in the inferred release asset and in
Protégé next to the new one. This happened to OpenCircuitVoltage in the 0.39.0
release candidate.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import rdflib
from rdflib import OWL, RDF, SKOS

REPO = Path(__file__).parents[1]
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
AXIOMS = sorted(SRC.subjects(RDF.type, OWL.Axiom), key=str)


def _label(s) -> str:
    return str(SRC.value(s, SKOS.prefLabel) or s)


def test_scan_found_axioms():
    assert AXIOMS, "no owl:Axiom reifications found - scan is broken"


def test_no_orphaned_annotation_axioms():
    orphans = []
    for ax in AXIOMS:
        s = SRC.value(ax, OWL.annotatedSource)
        p = SRC.value(ax, OWL.annotatedProperty)
        o = SRC.value(ax, OWL.annotatedTarget)
        if (s, p, o) not in SRC:
            orphans.append(f"{_label(s)} / {str(p).split('#')[-1]} / {str(o)[:60]!r}")
    assert not orphans, (
        f"{len(orphans)} owl:Axiom reification(s) annotate a triple that no longer exists; "
        "retarget or delete them: " + "; ".join(orphans)
    )
