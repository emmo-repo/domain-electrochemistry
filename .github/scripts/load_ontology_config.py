import json
from config_loader import load_ontology_config

def main():
    config = load_ontology_config()

    # ✅ Only output valid `key=value` lines for GitHub Actions
    print(f"ONTOLOGY_NAME={config['ontology_name']}")
    print(f"ONTOLOGY_URI={config['ontology_uri']}")
    print(f"RST_FILE={config['rst_output_filename']}")
    print(f"INFERRED_TTL_FILENAME={config['inferred_ttl_filename']}")

    ttl_files_json = json.dumps([f['path'] for f in config['ttl_files']])
    print(f"TTL_FILES_JSON={ttl_files_json}")

if __name__ == "__main__":
    main()
