import yaml
import json
import os

# Path to ontology_config.yml (assumed in repo root)
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ontology_config.yml")

with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Set values for GitHub Actions
ontology_name = config['ontology']['name']
rst_output_filename = config['output']['rst_file']
ttl_files = config['ttl_files']

# Print environment variables for GitHub Actions
print(f"ONTOLOGY_NAME={ontology_name}")

# Prepare JSON version of ttl_files paths only (used by run_emmocheck.py)
ttl_paths = [f["path"] for f in ttl_files]
print(f"TTL_FILES_JSON={json.dumps(ttl_paths)}")
