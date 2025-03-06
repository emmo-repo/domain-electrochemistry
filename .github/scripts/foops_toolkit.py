import os
import subprocess
import json
import sys
import requests
from ontology_toolkit import load_ontology_config


def apply_foops_to_file(input_file, output_file):
    """Applies FOOPS recommendations to a single file."""
    print(f"Applying FOOPS recommendations to {input_file} -> {output_file}")
    subprocess.run(
        ["python", ".github/scripts/apply_foops_recommendations.py", input_file, output_file],
        check=True
    )
    print(f"✅ FOOPS recommendations applied to {input_file}")


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

    parser = argparse.ArgumentParser(description="FOOPS Manager for individual FOOPS tasks.")
    parser.add_argument("--apply-to-file", nargs=2, metavar=("INPUT", "OUTPUT"),
                        help="Apply FOOPS to a single TTL file (input and output file paths).")
    parser.add_argument("--generate-badge", action="store_true", help="Fetch FOOPS score and generate a badge.")

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
