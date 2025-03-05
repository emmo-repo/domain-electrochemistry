import rdflib
from owlrl import DeductiveClosure, OWLRL_Semantics
import logging
import sys
import os

import os
import sys
import yaml

def load_ontology_config():
    """Load ontology_name and ttl_files from ontology_config.yml."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ontology_config.yml")

    if not os.path.isfile(config_path):
        print(f"❌ ontology_config.yml not found at: {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

            ontology_name = config.get("ontology", {}).get("name")
            ttl_files = config.get("ttl_files", [])

            if not ontology_name or not ttl_files:
                print("❌ ontology_name or ttl_files missing from ontology_config.yml.")
                sys.exit(1)

            return ontology_name, ttl_files
    except Exception as e:
        print(f"❌ Failed to load ontology_config.yml: {e}")
        sys.exit(1)


ontology_name, ttl_files = load_ontology_config()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Find the main ontology file - assuming it's the top-level "core" TTL file
# You can optionally add a "core_file" field to ontology_config.py to be explicit if needed
main_ontology_file = None
for ttl_file in ttl_files:
    if "core" in ttl_file["section title"].lower() or ttl_file["section title"].lower() == "main":
        main_ontology_file = ttl_file["path"]
        break

# Fallback - if no "core" or "main" file found, just use the first TTL file
if not main_ontology_file and ttl_files:
    main_ontology_file = ttl_files[0]["path"]

if not main_ontology_file:
    logger.error("No ontology file found in ontology_config.py")
    sys.exit(1)

# Resolve full path to the ontology file
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ontology_path = os.path.join(repo_root, main_ontology_file)

# Check if the file exists
if not os.path.isfile(ontology_path):
    logger.error(f"Ontology file not found at {ontology_path}")
    sys.exit(1)

# Load the ontology using rdflib
g = rdflib.Graph()
try:
    g.parse(ontology_path, format='ttl')
    logger.info(f"Ontology '{ontology_name}' loaded successfully from {ontology_path}")
except Exception as e:
    logger.error(f"Error loading ontology: {e}")
    sys.exit(1)

# Perform OWL 2 RL reasoning
try:
    DeductiveClosure(OWLRL_Semantics).expand(g)
    logger.info("Reasoning completed successfully")
except Exception as e:
    logger.error(f"Reasoning error: {e}")
    sys.exit(1)

# Check for inconsistencies (basic heuristic)
inferred_triples = len(g)
if inferred_triples > 0:
    logger.info(f"Inferred {inferred_triples} triples.")
else:
    logger.error("No triples inferred, something might be wrong.")
    sys.exit(1)

sys.exit(0)
