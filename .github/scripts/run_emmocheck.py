import json
import os
import subprocess
import sys
import yaml

def load_ttl_files():
    """Load ttl_files from ontology_config.yml."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ontology_config.yml")

    if not os.path.isfile(config_path):
        print(f"❌ ontology_config.yml not found at: {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            ttl_files = config.get("ttl_files", [])

            if not ttl_files:
                print("⚠️ No TTL files found in ontology_config.yml.")
                sys.exit(1)

            return ttl_files
    except Exception as e:
        print(f"❌ Failed to load ontology_config.yml: {e}")
        sys.exit(1)


def main():
    ttl_files = load_ttl_files()

    if not ttl_files:
        print("⚠️ No TTL files found in ontology_config.py.")
        sys.exit(1)

    for entry in ttl_files:
        title = entry["section title"]
        path = entry["path"]

        if not os.path.isfile(path):
            print(f"⚠️ File not found: {path}")
            sys.exit(1)

        print(f"Running EMMO Check for {title} ({path})...")
        cmd = [
            "emmocheck",
            "--verbose", "--url-from-catalog",
            "--skip", "test_namespace",
            "--skip", "test_quantity_dimension",
            "--configfile", ".github/utils/emmocheck_config.yml",
            path
        ]

        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"❌ EMMO Check failed for {title} ({path})")
            sys.exit(result.returncode)

    print("✅ All EMMO checks passed.")

if __name__ == "__main__":
    main()
