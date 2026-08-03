"""check_iri_resolution -- verify the ontology's public IRIs dereference.

This script is IDENTICAL across the EMMO domain repos (domain-chemical-substance,
domain-electrochemistry, domain-battery).  Domain-specific knowledge lives in
``config.yml`` at the repository root (``ontology_uri`` and
``version_tooling.main_ttl``).

Checks, in order:

1. The unversioned ontology IRI resolves with ``Accept: text/turtle``
   (via the w3id.org redirect) and the response parses as Turtle.
2. The ``owl:versionIRI`` declared by the LIVE ontology fetched in (1)
   also resolves and parses.  Using the live document's own version (rather
   than the local checkout's) keeps the check green in the window between a
   version-bump merge and its release.
3. Every ``owl:imports`` of the live ontology (the versioned dependencies
   module) resolves and parses.
4. Warn-only: the unversioned IRI with ``Accept: text/html`` returns a
   document (the human-facing docs routing).

The local checkout's version is compared against the live one and reported;
a mismatch is a notice, not a failure (expected pre-release).

Exit status: 0 if all hard checks pass, 1 otherwise.
"""

from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import rdflib
import yaml

USER_AGENT = "emmo-domain-iri-check/1.0 (+https://github.com/emmo-repo)"
RETRIES = 3
BACKOFF_SECONDS = 10
TIMEOUT_SECONDS = 60


def fetch(url: str, accept: str) -> bytes:
    """GET *url* with an Accept header, following redirects, with retries."""
    last_error: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        request = urllib.request.Request(
            url, headers={"Accept": accept, "User-Agent": USER_AGENT}
        )
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < RETRIES:
                time.sleep(BACKOFF_SECONDS * attempt)
    raise RuntimeError(f"{url} did not resolve after {RETRIES} attempts: {last_error}")


def parse_turtle(data: bytes, source: str) -> rdflib.Graph:
    graph = rdflib.Graph()
    try:
        graph.parse(data=data, format="turtle")
    except Exception as exc:
        raise RuntimeError(f"{source}: response is not parseable Turtle: {exc}") from exc
    return graph


def ontology_subject(graph: rdflib.Graph, source: str) -> rdflib.URIRef:
    for subject in graph.subjects(rdflib.RDF.type, rdflib.OWL.Ontology):
        return subject
    raise RuntimeError(f"{source}: no owl:Ontology declaration found")


def ontology_info(graph: rdflib.Graph, source: str) -> dict:
    subject = ontology_subject(graph, source)
    version_iri = graph.value(subject, rdflib.OWL.versionIRI)
    version_info = graph.value(subject, rdflib.OWL.versionInfo)
    imports = sorted(str(o) for o in graph.objects(subject, rdflib.OWL.imports))
    return {
        "subject": str(subject),
        "version_iri": str(version_iri) if version_iri else None,
        "version_info": str(version_info) if version_info else None,
        "imports": imports,
    }


def main() -> int:
    config = yaml.safe_load(Path("config.yml").read_text(encoding="utf-8"))
    ontology_uri = config["ontology_uri"]
    main_ttl = config["version_tooling"]["main_ttl"]

    failures: list[str] = []

    # 1. Unversioned IRI -> Turtle.
    print(f"Checking {ontology_uri} (text/turtle) ...")
    try:
        live_graph = parse_turtle(fetch(ontology_uri, "text/turtle"), ontology_uri)
        live = ontology_info(live_graph, ontology_uri)
        print(f"  OK: parses; live version {live['version_info']}")
    except RuntimeError as exc:
        failures.append(str(exc))
        live = None
        print(f"  FAIL: {exc}")

    if live is not None:
        # 2. The live document's own versionIRI.
        if live["version_iri"]:
            print(f"Checking {live['version_iri']} (text/turtle) ...")
            try:
                parse_turtle(
                    fetch(live["version_iri"], "text/turtle"), live["version_iri"]
                )
                print("  OK: versioned IRI parses")
            except RuntimeError as exc:
                failures.append(str(exc))
                print(f"  FAIL: {exc}")
        else:
            failures.append(f"{ontology_uri}: live ontology declares no owl:versionIRI")

        # 3. Versioned imports (dependencies module).
        for import_iri in live["imports"]:
            print(f"Checking import {import_iri} (text/turtle) ...")
            try:
                parse_turtle(fetch(import_iri, "text/turtle"), import_iri)
                print("  OK: import parses")
            except RuntimeError as exc:
                failures.append(str(exc))
                print(f"  FAIL: {exc}")

        # Local-vs-live version notice (informational only).
        local_graph = rdflib.Graph()
        local_graph.parse(main_ttl, format="turtle")
        local = ontology_info(local_graph, main_ttl)
        if local["version_info"] != live["version_info"]:
            print(
                f"NOTICE: local checkout is {local['version_info']} but the live "
                f"ontology serves {live['version_info']} (expected between a "
                "version-bump merge and its release)."
            )

    # 4. HTML routing (warn-only).
    print(f"Checking {ontology_uri} (text/html, warn-only) ...")
    try:
        fetch(ontology_uri, "text/html")
        print("  OK: HTML routing responds")
    except RuntimeError as exc:
        print(f"  WARN (not fatal): {exc}")

    if failures:
        print(f"\n{len(failures)} hard failure(s):")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("\nOK: all hard IRI resolution checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
