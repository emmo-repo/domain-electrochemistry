# ontology_config.py - Central place for ontology-specific settings

ontology_name = "Domain Electrochemistry"
ontology_uri = "https://w3id.org/emmo/domain/electrochemistry"
ontology_prefix = "https://w3id.org/emmo/domain/electrochemistry#"
ontology_description = "Ontology for describing electrochemical systems."

# List of TTL files that are part of this ontology (paths relative to repo root)
ttl_files = [
    "reference/electrochemistry-reference.ttl",
    "reference/electrochemistry-quantities.ttl",
    "modules/electrochemistry-manufacturing.ttl",
    "modules/electrochemistry-testing.ttl",
    "electrochemistry.ttl"
]

# Output filenames
inferred_ttl_filename = "electrochemistry-inferred.ttl"
rst_output_filename = "docs/electrochemistry.rst"

# Classes to check in EMMOCheck
emmocheck_classes = [
    "electrochemistry.ElectrochemicalQuantity",
    "electrochemistry.ElectrochemicalKineticQuantity",
    "electrochemistry.ElectrochemicalTransportQuantity",
    "electrochemistry.ElectrochemicalThermodynamicQuantity",
    "electrochemistry.ElectrochemicalConstant",
    "electrochemistry.ReactionRateConstant",
    "electrochemistry.PercentUnit"
]
