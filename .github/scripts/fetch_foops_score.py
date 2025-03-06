import requests
import json
import sys
from ontology_toolkit import load_ontology_config

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
    # Load ontology configuration
    config = load_ontology_config()

    ontology_name = config.get("ontology", {}).get("name")
    ontology_uri = config.get("ontology", {}).get("uri")

    if not ontology_uri or not ontology_name:
        print("❌ ontology_name or ontology_uri missing from ontology_config.yml.")
        sys.exit(1)

    try:
        score = fetch_foops_score(ontology_uri)
        print(f"FOOPS score for {ontology_name} ({ontology_uri}): {score}")
    except Exception as e:
        print(f"Error fetching FOOPS score: {e}")
        sys.exit(1)
