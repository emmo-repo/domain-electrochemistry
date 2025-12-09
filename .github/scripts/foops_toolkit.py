import argparse
import json
import logging
import os
import sys
from typing import Tuple

import requests
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDFS, SKOS

from ontology_toolkit import load_ontology_config

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
LOGGER = logging.getLogger(__name__)


def add_foops_recommendations(input_file: str, output_file: str) -> None:
    """Add FOOPS-friendly annotations and write to a new TTL."""
    emmo = Namespace("https://w3id.org/emmo#")

    with open(input_file, "r", encoding="utf-8") as file:
        ttl_content = file.read()

    graph = Graph()
    graph.parse(data=ttl_content, format="turtle")

    new_triples: list[Tuple] = []

    # Duplicate skos:prefLabel as rdfs:label
    for subj, _, obj in graph.triples((None, SKOS.prefLabel, None)):
        if isinstance(obj, Literal):
            new_triples.append((subj, RDFS.label, obj))

    # Duplicate EMMO-specific elucidation annotations as rdfs:comment
    for subj, _, obj in graph.triples((None, emmo.EMMO_967080e5_2f42_4eb2_a3a9_c58143e835f9, None)):
        if isinstance(obj, Literal):
            new_triples.append((subj, RDFS.comment, obj))

    for triple in new_triples:
        graph.add(triple)

    graph.serialize(destination=output_file, format="turtle")
    LOGGER.info("FOOPS recommendations applied to %s -> %s", input_file, output_file)


def update_readme_badge(repo_root: str, score: float) -> None:
    """Update the FOOPS badge in README.md with the latest score."""
    readme_path = os.path.join(repo_root, "README.md")

    color = "brightgreen" if score >= 80 else "yellow" if score >= 60 else "red"
    new_badge = (
        f"[![FOOPS Score](https://img.shields.io/badge/FOOPS%20Score-{score}%25-{color})]"
        "(https://foops.linkeddata.es/FAIR_validator.html)"
    )

    if not os.path.exists(readme_path):
        LOGGER.warning("README.md not found at %s, skipping badge update.", readme_path)
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    import re

    badge_regex = re.compile(r"\[!\[FOOPS Score\]\([^\)]+\)\]\([^\)]+\)")

    if badge_regex.search(readme_content):
        updated_content = badge_regex.sub(new_badge, readme_content)
        LOGGER.info("Updated existing FOOPS badge in README.md")
    else:
        updated_content = new_badge + "\n\n" + readme_content
        LOGGER.info("Added new FOOPS badge to top of README.md")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)


def fetch_foops_score(ontology_uri: str) -> float:
    """Fetch FOOPS score for the given ontology URI."""
    try:
        response = requests.post(
            "https://foops.linkeddata.es/assessOntology",
            headers={"accept": "application/json;charset=UTF-8", "Content-Type": "application/json;charset=UTF-8"},
            data=json.dumps({"ontologyUri": ontology_uri}),
            timeout=60,
        )
        response.raise_for_status()
    except Exception as exc:
        LOGGER.error("Failed to fetch FOOPS score: %s", exc)
        sys.exit(1)

    try:
        score_value = float(response.json()["overall_score"])
    except Exception as exc:
        LOGGER.error("Failed to parse FOOPS score from response: %s", exc)
        sys.exit(1)

    return round(score_value * 100, 2)


def generate_foops_badge() -> None:
    """Fetch FOOPS score, generate a badge, and update README.md."""
    config = load_ontology_config()
    ontology_uri = config["ontology_uri"]
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    badge_path = os.path.join(repo_root, "docs/assets/foops_badge.svg")

    score = fetch_foops_score(ontology_uri)
    LOGGER.info("FOOPS score: %s", score)

    color = "brightgreen" if score >= 80 else "yellow" if score >= 60 else "red"
    badge_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
    <rect width="150" height="20" fill="#555"/>
    <rect x="80" width="70" height="20" fill="{color}"/>
    <text x="5" y="14" fill="#fff" font-family="Arial" font-size="11">FOOPS Score</text>
    <text x="85" y="14" fill="#fff" font-family="Arial" font-size="11">{score}%</text>
</svg>
"""

    os.makedirs(os.path.dirname(badge_path), exist_ok=True)
    with open(badge_path, "w", encoding="utf-8") as f:
        f.write(badge_svg)

    LOGGER.info("FOOPS badge generated at %s", badge_path)
    update_readme_badge(repo_root, score)


def main() -> None:
    parser = argparse.ArgumentParser(description="FOOPS Toolkit for applying recommendations and generating badges.")
    parser.add_argument("--apply-to-file", nargs=2, metavar=("INPUT", "OUTPUT"),
                        help="Apply FOOPS recommendations to a single TTL file.")
    parser.add_argument("--generate-badge", action="store_true", help="Fetch FOOPS score and generate badge.")

    args = parser.parse_args()

    if args.apply_to_file:
        add_foops_recommendations(args.apply_to_file[0], args.apply_to_file[1])
        return

    if args.generate_badge:
        generate_foops_badge()
        return

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
