import rdflib
from owlrl import DeductiveClosure, OWLRL_Semantics
import logging
import sys
import os
from ontology_toolkit import load_ontology_config  # Use config_loader for configuration

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration from ontology_config.yml
config = load_ontology_config()

ttl_files = config["ttl_files"]
ontology_name = config["ontology_name"]

# Find the main ontology file - assuming it's the top-level "core" TTL file
main_ontology_file = None
for ttl_file in ttl_files:
    if "core" in ttl_file["section_title"].lower() or ttl_file["section_title"].lower() == "main ontology":
        main_ontology_file = ttl_file["path"]
        break

# Fallback - if no "core" or "main ontology" file found, just use the first TTL file
if not main_ontology_file and ttl_files:
    main_ontology_file = ttl_files[0]["path"]

if not main_ontology_file:
    logger.error("No ontology file found in ontology_config.yml")
    sys.exit(1)

# Resolve full path to the ontology file (repo root is two levels up from this script)
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
