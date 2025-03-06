import json
import os
import sys
import yaml
import rdflib
from rdflib.namespace import RDF, OWL, SKOS, RDFS
from urllib.parse import urljoin
from urllib.request import pathname2url

def print_ttl_files():
    config = load_ontology_config()
    print(" ".join([file['path'] for file in config['ttl_files']]))

def find_repo_root_with_config():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        config_path = os.path.join(current_dir, "ontology_config.yml")
        if os.path.isfile(config_path):
            return config_path

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            sys.exit(1)

        current_dir = parent_dir

def load_ontology_config():
    config_path = find_repo_root_with_config()
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

            return {
                "ontology_name": config.get("ontology_name"),
                "ontology_uri": config.get("ontology_uri"),
                "ontology_prefix": config.get("ontology_prefix"),
                "ontology_description": config.get("ontology_description"),
                "ttl_files": config.get("ttl_files", []),
                "inferred_ttl_filename": config.get("output", {}).get("inferred_ttl"),
                "rst_output_filename": config.get("output", {}).get("rst_file"),
                "emmocheck_classes": config.get("emmocheck_classes", []),
            }
    except Exception as e:
        sys.exit(1)


########## JSON-LD Context Generation (ttl_to_context logic) ##########

def generate_jsonld_context(ttl_file, predicate_uri, label_uri='http://www.w3.org/2000/01/rdf-schema#label'):
    g = rdflib.Graph()
    g.parse(ttl_file, format='ttl')

    context = {}
    object_properties = {}
    other_entries = {}
    namespace_prefixes = {}

    predicate = rdflib.URIRef(predicate_uri)

    for s, p, o in g:
        if (s, RDF.type, OWL.ObjectProperty) in g:
            label_value = g.value(s, SKOS.prefLabel)
            if label_value:
                object_properties[str(label_value)] = {"@id": str(s), "@type": "@id"}
        elif p == predicate:
            other_entries[str(o)] = str(s)

    for prefix, uri in g.namespace_manager.namespaces():
        if len(prefix) >= 2:
            namespace_prefixes[prefix] = str(uri)

    context = {
        "@context": {
            **dict(sorted(namespace_prefixes.items())),
            **dict(sorted(object_properties.items())),
            **dict(sorted(other_entries.items()))
        }
    }

    return context


def create_jsonld_context_file():
    config = load_ontology_config()
    filename = config["inferred_ttl_filename"]

    repo_root = os.path.dirname(find_repo_root_with_config())
    file_path = os.path.join(repo_root, filename)

    file_uri = urljoin('file:', pathname2url(file_path))
    context = generate_jsonld_context(file_uri, 'http://www.w3.org/2004/02/skos/core#prefLabel')

    context_dir = os.path.join(repo_root, 'context')
    os.makedirs(context_dir, exist_ok=True)
    context_file_path = os.path.join(context_dir, 'context.json')

    with open(context_file_path, 'w', encoding='utf-8') as f:
        json.dump(context, f, indent=4)

    print(f"✅ JSON-LD context saved to {context_file_path}")


########## RST Documentation Generation (ttl_to_rst logic) ##########

def load_ttl_from_file(filepath):
    g = rdflib.Graph()
    g.parse(filepath, format="turtle")
    return g


def extract_terms_info_sparql(g):
    PREFIXES = """
        PREFIX emmo: <https://w3id.org/emmo#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
    """

    query = PREFIXES + """
        SELECT ?iri ?prefLabel WHERE {
            ?iri skos:prefLabel ?prefLabel.
        }
    """

    return [{"IRI": str(row.iri), "prefLabel": str(row.prefLabel)} for row in g.query(query)]


def render_rst_top(config):
    title = f"{config['ontology_name']} Terms"
    return f"{title}\n{'=' * len(title)}\n\n{config['ontology_description']}\n\n"


def render_rst_bottom():
    return "End of Document.\n"


def entities_to_rst(entities):
    rst = ""
    for item in entities:
        iri_suffix = item['IRI'].split("#")[-1]
        rst += f".. _{iri_suffix}:\n\n{item['prefLabel']}\n{'-' * len(item['prefLabel'])}\n\n"
        rst += f"IRI: {item['IRI']}\n\n"
    return rst


def generate_rst_documentation():
    config = load_ontology_config()
    rst_filename = config["rst_output_filename"]

    rst_content = render_rst_top(config)

    for module in config["ttl_files"]:
        filepath = module["path"]
        if os.path.isfile(filepath):
            g = load_ttl_from_file(filepath)
            entities = extract_terms_info_sparql(g)
            rst_content += f"\n{module['section_title']}\n{'=' * len(module['section_title'])}\n\n"
            rst_content += entities_to_rst(entities)

    rst_content += render_rst_bottom()

    with open(rst_filename, "w+", encoding="utf-8") as f:
        f.write(rst_content)

    print(f"✅ RST file generated: {rst_filename}")


########## Main Entry Point ##########

def main():
    config = load_ontology_config()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--print-ttl-files", action="store_true", help="Prints space-separated TTL files.")
    parser.add_argument("--generate-context", action="store_true", help="Generate JSON-LD context.")
    parser.add_argument("--generate-rst", action="store_true", help="Generate RST documentation.")
    args = parser.parse_args()

    if args.print_ttl_files:
        print_ttl_files()

    if args.generate_context:
        create_jsonld_context_file()

    if args.generate_rst:
        generate_rst_documentation()

    print(f"ONTOLOGY_NAME={config['ontology_name']}")
    print(f"ONTOLOGY_URI={config['ontology_uri']}")
    print(f"RST_FILE={config['rst_output_filename']}")
    print(f"INFERRED_TTL_FILENAME={config['inferred_ttl_filename']}")

    ttl_files_json = json.dumps([f['path'] for f in config['ttl_files']])
    print(f"TTL_FILES_JSON={ttl_files_json}")


if __name__ == "__main__":
    main()
