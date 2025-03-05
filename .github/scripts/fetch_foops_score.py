import requests
import json
import sys
import os

# Import ontology_config
try:
    from ontology_config import ontology_uri, ontology_name
except ImportError:
    print("Error: Could not import ontology_config. Ensure ontology_config.py is in the Python path.")
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
    if not ontology_uri:
        print("Error: ontology_uri is not defined in ontology_config.py")
        sys.exit(1)

    try:
        score = fetch_foops_score(ontology_uri)
        print(f"FOOPS score for {ontology_name} ({ontology_uri}): {score}")
    except Exception as e:
        print(f"Error fetching FOOPS score: {e}")
        sys.exit(1)
