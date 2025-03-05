import json
from config_loader import load_ontology_config

def main():
    # Load configuration from ontology_config.yml
    config = load_ontology_config()

    print(config)

    ttl_files = config["ttl_files"]
    ontology_name = config["ontology_name"]
    rst_output_filename = config["rst_output_filename"]

    # Print environment variables for GitHub Actions
    print(f"ONTOLOGY_NAME={ontology_name}")

    # Prepare JSON version of ttl_files paths only (used by run_emmocheck.py)
    ttl_paths = [f["path"] for f in ttl_files]
    print(f"TTL_FILES_JSON={json.dumps(ttl_paths)}")


if __name__ == "__main__":
    main()
