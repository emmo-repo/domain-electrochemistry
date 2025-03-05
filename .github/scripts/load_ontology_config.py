import json
from config_loader import load_ontology_config

def main():
    # Load full ontology config
    config = load_ontology_config()

    ontology_name = config['ontology']['name']
    rst_output_filename = config['output']['rst_file']
    ttl_files = config['ttl_files']

    # Print environment variables for GitHub Actions
    print(f"ONTOLOGY_NAME={ontology_name}")

    # Prepare JSON version of ttl_files paths only (used by run_emmocheck.py)
    ttl_paths = [f["path"] for f in ttl_files]
    print(f"TTL_FILES_JSON={json.dumps(ttl_paths)}")


if __name__ == "__main__":
    main()
