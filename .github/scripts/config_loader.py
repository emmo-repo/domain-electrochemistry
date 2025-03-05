import os
import sys
import yaml

def find_repo_root_with_config():
    """Recursively search upward from the current script location until ontology_config.yml is found."""
    current_dir = os.path.abspath(os.path.dirname(__file__))

    while True:
        config_path = os.path.join(current_dir, "ontology_config.yml")
        if os.path.isfile(config_path):
            return config_path

        # Move up to the parent directory
        parent_dir = os.path.dirname(current_dir)

        # Stop if we've reached the filesystem root
        if parent_dir == current_dir:
            print("❌ ontology_config.yml not found in any parent directory.")
            sys.exit(1)

        current_dir = parent_dir

def load_ontology_config():
    """Load all configuration values from ontology_config.yml."""
    config_path = find_repo_root_with_config()

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

            ontology_name = config.get("ontology_name")
            ontology_uri = config.get("ontology_uri")
            ontology_prefix = config.get("ontology_prefix")
            ontology_description = config.get("ontology_description")
            ttl_files = config.get("ttl_files", [])
            inferred_ttl_filename = config.get("output", {}).get("inferred_ttl")
            rst_output_filename = config.get("output", {}).get("rst_file")
            emmo_classes = config.get("emmocheck_classes", [])

            if not ontology_name or not ttl_files:
                print("❌ ontology_name or ttl_files missing from ontology_config.yml.")
                sys.exit(1)

            print(f"✅ Loaded ontology_config.yml from: {config_path}")
            return {
                "ontology_name": ontology_name,
                "ontology_uri": ontology_uri,
                "ontology_prefix": ontology_prefix,
                "ontology_description": ontology_description,
                "ttl_files": ttl_files,
                "inferred_ttl_filename": inferred_ttl_filename,
                "rst_output_filename": rst_output_filename,
                "emmocheck_classes": emmo_classes,
            }

    except Exception as e:
        print(f"❌ Failed to load ontology_config.yml: {e}")
        sys.exit(1)
