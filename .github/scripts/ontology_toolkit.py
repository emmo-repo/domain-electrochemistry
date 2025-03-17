import json
import os
import sys
import subprocess
import yaml
import rdflib
from rdflib.namespace import RDF, OWL, SKOS, RDFS
from urllib.parse import urljoin
from urllib.request import pathname2url
from rdflib import Graph
import logging
from owlrl import DeductiveClosure, OWLRL_Semantics
from ontopy.ontology import Ontology
import owlready2

def print_ttl_files():
    config = load_ontology_config()
    print(" ".join([file['path'] for file in config['ttl_files']]))

def find_repo_root_with_config():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        config_path = os.path.join(current_dir, "config.yml")
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
                "ontology_noun": config.get("ontology_noun"),
                "ontology_adjective": config.get("ontology_adjective"),
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
    from ontopy import get_ontology
    onto = get_ontology(filepath).load()
    return onto

def _extract_all_annotations(value_list):
    '''Help Function to extract both the text of a locstr and just str
    from annotations. For now only choosing english. Note that this is a bit of a hack since not all annotations
    are implemented as a locstr as they should. Perhaps this should be fixed in 
    emmocheck instead?'''
    result = []
    for elem in value_list:
        # For plain strings: only include if its type is exactly str.
        if type(elem) is str:
            result.append(elem)
        # For locstr strings: include if its language is English.
        elif hasattr(elem, "lang") and elem.lang == "en":
            result.append(elem)
    return result


def extract_terms_info_sparql(onto: Ontology) -> list:
    """Extracts terms from the TTL graph using SPARQL, including parent, subclass, and restriction links."""
    text_entities = []

    list_entity_types = [
        "IRI", "prefLabel", "Elucidation", "Alternative Label(s)",
        "IEC Reference", "IUPAC Reference", "Wikipedia Reference",
        "Wikidata Reference", "Comment", 
        "Tip", "Caution", "Important", "Note", "Danger", "Error",
        "Warning", "Admonition"
    ]

    config = load_ontology_config()

    for entity in onto.get_entities(imported=False):
        hit_dict = {'IRI': entity.iri}
        # This is a bit of a hack, need to have a better way to be sure that we only 
        # consider terms defined in the current ontology (and not just referenes here)
        if not entity.iri.split('#')[0] == config["ontology_prefix"].rstrip('#/'):
            continue
 

        #if not (isinstance(entity, owlready2.ThingClass) or isinstance(entity, owlready2.PropertyClass)):
        #    continue

        annotations = entity.get_annotations()
        annotations_en = {
                key: '; '.join(_extract_all_annotations(item))
            for key, item in annotations.items()
        }

        hit_dict.update(annotations_en)

        parents = [ent for ent in entity.is_a if (isinstance(ent, owlready2.ThingClass) or isinstance(ent, owlready2.PropertyClass))]
        hit_dict["Parent Classes"] = parents

        # Fetch direct subclasses
        subclasses = list(entity.subclasses())

        # Fetch OWL Restrictions (object property + someValuesFrom)
        restrictions = [restriction for restriction in entity.is_a if isinstance(restriction, owlready2.Restriction)]
        hit_dict["Restrictions"] = restrictions

        text_entities.append(hit_dict)

    text_entities.sort(key=lambda e: e["prefLabel"])
    return text_entities


def render_rst_top() -> str:
    config = load_ontology_config()

    ontology_name = config["ontology_name"]
    ontology_description = config["ontology_description"]
    ontology_adjective = config["ontology_adjective"]
    ontology_noun = config["ontology_noun"]

    title = f"{ontology_name} Terms"
    underline = "=" * len(title)

    return f"""
:html_theme.sidebar_secondary.remove:

{underline}
{title}
{underline}

**{ontology_description}**

The {ontology_name} is a domain of the Elementary Multiperspective Materials Ontology (EMMO), for describing {ontology_adjective} systems, materials, methods, and data. Its primary objective is to support the creation of FAIR, Linked Data within the field of {ontology_noun}. This ontology serves as a foundational resource for harmonizing {ontology_adjective} knowledge representation, enhancing data interoperability, and accelerating progress in electroc{ontology_adjective}hemical research and development.

This page lists all terms extracted from the {ontology_name.lower()} ontology. It is intended to serve as a reference resource. 

"""


def entities_to_rst(entities: list[dict]) -> str:
    """Converts extracted ontology terms into an RST format."""
    rst = ""

    callout_keys = {"Tip", "Caution", "Important", "Note", "Danger", "Warning", "Error", "Admonition"}

    for item in entities:
        if '#' not in item['IRI']:
            continue

        iri_prefix, iri_suffix = item['IRI'].split("#")

        # Horizontal line for visual separation
        rst += "\n----\n\n"

        # Create a target anchor so the right-side TOC can link here
        #rst += f".. _{item['prefLabel']}:\n\n"

        rst += ".. raw:: html\n\n"
        rst += f"   <div id=\"{iri_suffix}\"></div>\n\n"
        rst += f"{item['prefLabel']}\n"
        rst += "-" * len(item['prefLabel']) + "\n\n"
        rst += f"IRI: {item['IRI']}\n\n"

        rst += ".. raw:: html\n\n"
        indent = "  "
        rst += indent + "<table class=\"element-table\">\n"

        # Normal properties (skip callouts and special lists handled later)
        for key, value in item.items():
            if key in ['IRI', 'prefLabel', 'Parent Classes', 'Subclasses', 'Restrictions'] or key in callout_keys or value in ["None", ""]:
                continue

            rst += "  <tr>\n"
            rst += f"    <td class=\"element-table-key\"><span class=\"element-table-key\">{key}</span></td>\n"

            #print(value)
            if value.startswith("http"):
                value = f"<a href='{value}'>{value}</a>"

            rst += f"    <td class=\"element-table-value\">{value}</td>\n"
            rst += "  </tr>\n"
        # Add parent classes section
        if item.get("Parent Classes"):
            rst += "  <tr>\n"
            rst += "    <td class=\"element-table-key\"><span class=\"element-table-key\">Parent Classes</span></td>\n"
            rst += "    <td class=\"element-table-value\">"

            parent_links = []
            for parent in item["Parent Classes"]:
                try:
                    parent_links.append(f"<a href='#{parent.iri.split('#')[-1]}'>{parent.prefLabel.get_lang('en')[0]}</a>")
                except:
                    parent_links.append(f"<a href='#{parent.iri.split('#')[-1]}'>{parent}</a>")

            
            rst += ", ".join(parent_links)
            rst += "</td>\n"
            rst += "  </tr>\n"

        # Add subclasses section
        if item.get("Subclasses"):
            rst += "  <tr>\n"
            rst += "    <td class=\"element-table-key\"><span class=\"element-table-key\">Subclasses</span></td>\n"
            rst += "    <td class=\"element-table-value\">"
            subclass_links = [f"<a href='#{iri.split('#')[-1]}'>{label}</a>" for iri, label in item["Subclasses"]]
            rst += ", ".join(subclass_links)
            rst += "</td>\n"
            rst += "  </tr>\n"

        # Add restrictions section - each restriction gets its own row
        if item.get("Restrictions"):
            # Group restrictions by property_label for cleaner table (optional, but nice)
            grouped_restrictions = {}
            for restriction in item["Restrictions"]:
                try:
                    target_link = f"<a href='#{restriction.value.iri.split('#')[-1]}'>{restriction.value}</a>"
                except AttributeError:
                    target_link = f"<a href='#{restriction.value}'>{restriction.value}</a>"

                if restriction.property not in grouped_restrictions:
                    grouped_restrictions[restriction.property] = []
                grouped_restrictions[restriction.property].append(target_link)

            for prop_label, target_links in grouped_restrictions.items():
                rst += "  <tr>\n"
                rst += f"    <td class=\"element-table-key\"><span class=\"element-table-key\">{restriction.property}</span></td>\n"
                rst += "    <td class=\"element-table-value\">"
                rst += ", ".join(target_links)
                rst += "</td>\n"
                rst += "  </tr>\n"

        rst += "  </table>\n\n"


        # Add callouts (admonitions) below the table
        callout_mapping = {
            "Tip": "tip",
            "Caution": "caution",
            "Important": "important",
            "Note": "note",
            "Danger": "danger",
            "Warning": "warning",
            "Error": "error",
            "Admonition": "admonition"
        }

        callout_rst = ""
        for callout, admonition in callout_mapping.items():
            callout_value = item.get(callout, "").strip()
            if callout_value and callout_value.lower() != "none":
                callout_rst += f".. {admonition}::\n\n"
                for line in callout_value.splitlines():
                    callout_rst += f"   {line}\n"
                callout_rst += "\n"

        rst += callout_rst

    return rst


def render_rst_bottom():
    return "End of Document.\n"

def generate_rst_documentation():
    config = load_ontology_config()
    rst_filename = config["rst_output_filename"]

    rst_content = render_rst_top()

    for module in config["ttl_files"]:
        filepath = module["path"]
        if os.path.isfile(filepath):
            onto = load_ttl_from_file(filepath)
            entities = extract_terms_info_sparql(onto)
            rst_content += f"\n{module['section_title']}\n{'=' * len(module['section_title'])}\n\n"
            rst_content += entities_to_rst(entities)

    rst_content += render_rst_bottom()

    with open(rst_filename, "w+", encoding="utf-8") as f:
        f.write(rst_content)

    print(f"RST file generated: {rst_filename}")

########## Check EMMO Conventions ##########

def run_emmocheck():
    """Run EMMOCheck on all configured TTL files."""
    config = load_ontology_config()
    ttl_files = config["ttl_files"]

    if not ttl_files:
        print("No TTL files found in config.yml.")
        sys.exit(1)

    for entry in ttl_files:
        title = entry["section_title"]
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

########## Check Reasoner ##########

def run_reasoner_check():
    """Load the ontology, run OWL 2 RL reasoning, and check for inferred triples."""
    config = load_ontology_config()

    ttl_files = config["ttl_files"]
    ontology_name = config["ontology_name"]

    # Find the main ontology file (core or main ontology fallback)
    main_ontology_file = None
    for ttl_file in ttl_files:
        if "core" in ttl_file["section_title"].lower() or ttl_file["section_title"].lower() == "main ontology":
            main_ontology_file = ttl_file["path"]
            break

    if not main_ontology_file and ttl_files:
        main_ontology_file = ttl_files[0]["path"]

    if not main_ontology_file:
        print("❌ No ontology file found in config.yml")
        sys.exit(1)

    # Resolve full path to the ontology file
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    ontology_path = os.path.join(repo_root, main_ontology_file)

    if not os.path.isfile(ontology_path):
        print(f"❌ Ontology file not found at {ontology_path}")
        sys.exit(1)

    # Load the ontology
    g = rdflib.Graph()
    try:
        g.parse(ontology_path, format='ttl')
        print(f"✅ Ontology '{ontology_name}' loaded successfully from {ontology_path}")
    except Exception as e:
        print(f"❌ Error loading ontology: {e}")
        sys.exit(1)

    # Perform reasoning
    try:
        DeductiveClosure(OWLRL_Semantics).expand(g)
        print("✅ Reasoning completed successfully")
    except Exception as e:
        print(f"❌ Reasoning error: {e}")
        sys.exit(1)

    # Basic inferred triples check
    inferred_triples = len(g)
    if inferred_triples > 0:
        print(f"✅ Inferred {inferred_triples} triples.")
    else:
        print("⚠️ No triples inferred, something might be wrong.")
        sys.exit(1)

########## Main Entry Point ##########

#def run_ontodoc():


def main():
    config = load_ontology_config()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--print-ttl-files", action="store_true", help="Prints space-separated TTL files.")
    parser.add_argument("--generate-context", action="store_true", help="Generate JSON-LD context.")
    parser.add_argument("--generate-rst", action="store_true", help="Generate RST documentation.")
    parser.add_argument("--run-emmocheck", action="store_true", help="Run EMMOCheck on all TTL files.")
    parser.add_argument("--run-reasoner-check", action="store_true", help="Run OWL 2 RL reasoner check.")
    args = parser.parse_args()

    if args.print_ttl_files:
        print_ttl_files()

    if args.generate_context:
        create_jsonld_context_file()

    if args.generate_rst:
        generate_rst_documentation()

    if args.run_emmocheck:
        run_emmocheck()

    if args.run_reasoner_check:
        run_reasoner_check()

    print(f"ONTOLOGY_NAME={config['ontology_name']}")
    print(f"ONTOLOGY_URI={config['ontology_uri']}")
    print(f"RST_FILE={config['rst_output_filename']}")
    print(f"INFERRED_TTL_FILENAME={config['inferred_ttl_filename']}")

    ttl_files_json = json.dumps([f['path'] for f in config['ttl_files']])
    print(f"TTL_FILES_JSON={ttl_files_json}")


if __name__ == "__main__":
    main()
