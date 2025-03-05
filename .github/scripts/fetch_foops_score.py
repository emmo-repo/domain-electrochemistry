import requests
import json
import sys
import os
import yaml

def load_ontology_metadata():
    """Load ontology metadata (name, uri) from ontology_config.yml."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ontology_config.yml")

    if not os.path.isfile(config_path):
        print(f"❌ ontology_config.yml not found at: {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            ontology = config.get("ontology", {})
            ontology_uri = ontology.get("uri")
            ontology_name = ontology.get("name")

            if not ontology_uri or not ontology_name:
                print("❌ ontology_name or ontology_uri missing from ontology_config.yml.")
                sys.exit(1)

            return ontology_uri, ontology_name
    except Exception as e:
        print(f"❌ Failed to load ontology_config.yml: {e}")
        sys.exit(1)

def fetch_foops_score(ontology_uri):
    url = "https://foops.linkeddata.es/assessOntology"
    headers = {
        "accept": "application/json;charset=UTF-8",
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = {
        "ontologyUri": ontology_uri
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        score = result['overall_score']
        return round(score, 2)
    else:
        raise Exception(f"Failed to fetch FOOPS score: {response.status_code}")

if __name__ == "__main__":
    # Load ontology metadata at the top of the script
    ontology_uri, ontology_name = load_ontology_metadata()
    if not ontology_uri:
        print("Error: ontology_uri is not defined in ontology_config.py")
        sys.exit(1)

    try:
        score = fetch_foops_score(ontology_uri)
        print(f"FOOPS score for {ontology_name} ({ontology_uri}): {score}")
    except Exception as e:
        print(f"Error fetching FOOPS score: {e}")
        sys.exit(1)
