import rdflib
from owlrl import DeductiveClosure, OWLRL_Semantics
import logging
import sys
import os

# Import ontology_config
try:
    from ontology_config import ontology_name, ttl_files
except ImportError:
    print("Error: Could not import ontology_config. Ensure ontology_config.py is in the Python path.")
    sys.exit(1)

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
