import os
import json
import sys
import requests
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, SKOS
from ontology_toolkit import load_ontology_config


def add_foops_recommendations(input_file, output_file):
    """
    Reads an ontology from a TTL file, adds extra relationships to comply with FOOPS recommendations,
    and writes the updated ontology to a new TTL file.

    Args:
        input_file (str): Path to the input TTL file.
        output_file (str): Path to the output TTL file where updated ontology will be saved.
    """
    EMMO = Namespace("https://w3id.org/emmo#")

    with open(input_file, 'r', encoding='utf-8') as file:
        ttl_content = file.read()

    graph = Graph()
    graph.parse(data=ttl_content, format='turtle')

    new_triples = []

    # Duplicate skos:prefLabel as rdfs:label
    for subj, pred, obj in graph.triples((None, SKOS.prefLabel, None)):
        if isinstance(obj, Literal):
            new_triples.append((subj, RDFS.label, obj))

    # Duplicate EMMO-specific elucidation annotations as rdfs:comment
    for subj, pred, obj in graph.triples((None, EMMO.EMMO_967080e5_2f42_4eb2_a3a9_c58143e835f9, None)):
        if isinstance(obj, Literal):
            new_triples.append((subj, RDFS.comment, obj))

    for triple in new_triples:
        graph.add(triple)

    graph.serialize(destination=output_file, format='turtle')
    print(f"✅ FOOPS recommendations applied to {input_file}, saved as {output_file}")


def apply_foops_to_file(input_file, output_file):
    """Wrapper to apply FOOPS directly within the toolkit (no subprocess)."""
    add_foops_recommendations(input_file, output_file)


def generate_foops_badge():
    """Fetches FOOPS score and generates a badge."""
    config = load_ontology_config()
    ontology_uri = config["ontology_uri"]
    repo_root = config["repo_root"]

    badge_path = os.path.join(repo_root, "docs/assets/foops_badge.svg")

    response = requests.post(
        "https://foops.linkeddata.es/assessOntology",
        headers={"accept": "application/json;charset=UTF-8", "Content-Type": "application/json;charset=UTF-8"},
        data=json.dumps({"ontologyUri": ontology_uri}),
    )

    if response.status_code != 200:
        print(f"❌ Failed to fetch FOOPS score (HTTP {response.status_code})")
        sys.exit(1)

    score = round(response.json()["overall_score"], 2)
    print(f"✅ FOOPS score: {score}")

    color = "green" if score >= 80 else "yellow" if score >= 60 else "red"
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

    print(f"✅ FOOPS badge generated at {badge_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="FOOPS Toolkit for applying recommendations and generating badges.")
    parser.add_argument("--apply-to-file", nargs=2, metavar=("INPUT", "OUTPUT"),
                        help="Apply FOOPS recommendations to a single TTL file.")
    parser.add_argument("--generate-badge", action="store_true", help="Fetch FOOPS score and generate badge.")

    args = parser.parse_args()

    if args.apply_to_file:
        apply_foops_to_file(args.apply_to_file[0], args.apply_to_file[1])

    elif args.generate_badge:
        generate_foops_badge()

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
