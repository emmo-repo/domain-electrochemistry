import json
import os
import subprocess
import sys

def load_ttl_files():
    """Load ttl_files from ontology_config."""
    try:
        from ontology_config import ttl_files
        return ttl_files
    except ImportError as e:
        print(f"❌ Failed to import ontology_config: {e}")
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
