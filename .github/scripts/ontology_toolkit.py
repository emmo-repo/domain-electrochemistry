import json
import os
import sys
import re
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
from ontopy.utils import asstring
from ontopy.patch import get_preferred_label
import owlready2

import re

def _linkify_value(val: str) -> str:
    """
    If `val` contains one or more IRIs, return them as separate links.
    - If exactly one IRI and it's an image, embed the image.
    - Otherwise, link each IRI separately and join with '; '.
    """
    if not isinstance(val, str):
        return val

    # find IRIs (separated by ; , or whitespace)
    urls = re.findall(r'https?://[^\s;,]+', val)
    if not urls:
        return val

    # single image → embed
    if len(urls) == 1 and urls[0].lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg")):
        u = urls[0]
        return (f'<a href="{u}"><img src="{u}" alt="{u}" '
                f'style="max-width:400px; max-height:300px;"/></a>')

    # otherwise, link each separately, showing full IRI as label
    links = []
    for u in urls:
        links.append(_html_links(u, u))  # use full IRI as label
    return '; '.join(links)


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

    # Manual additions for deprecated or external terms
    manual_additions = {
        "hasNumericalValue": "https://w3id.org/emmo#EMMO_faf79f53_749d_40b2_807c_d34244c192f4",
        "hasNext": {
            "@id": "https://w3id.org/emmo#EMMO_499e24a5_5072_4c83_8625_fe3f96ae4a8d",
            "@type": "@id"
        },
    }

    # Inject manual additions into context
    context["@context"].update(manual_additions)

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



# Standard IRIs for the built‑in annotation properties
ANNOTATION_RANK = {
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "altLabel":  "http://www.w3.org/2004/02/skos/core#altLabel",
    "elucidation": "https://w3id.org/emmo#EMMO_967080e5_2f42_4eb2_a3a9_c58143e835f9",  
    "comment": "http://www.w3.org/2000/01/rdf-schema#comment",
    "example": "http://www.w3.org/2004/02/skos/core#example",
    "seeAlso": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "isDefinedBy": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy",
}


def _sorted_annotations(onto: Ontology):
    # Resolve IRIs → AnnotationProperty instances (in defined order)
    priorities = [
        onto[iri]
        for iri in ANNOTATION_RANK.values()
        if onto[iri] is not None
    ]

    def rank(prop):
        # Exact match for the first three anchors
        if prop in priorities[:3]:

            return priorities.index(prop)

        # Otherwise find the earliest anchor among its ancestors
        ancestors = set(prop.ancestors())
        for idx, anchor in enumerate(priorities[3:], start=3):
            if anchor in ancestors:
                return idx

        # Anything else falls to the bottom
        return len(priorities)

    all_props = list(onto.annotation_properties(imported=True))
    return sorted(all_props, key=rank)



def extract_terms_info_sparql(onto: Ontology) -> list:
    """Extracts terms from the TTL graph using SPARQL, including parent, subclass, and restriction links."""
    text_entities = []

    config = load_ontology_config()

    all_annotations = _sorted_annotations(onto)
    for entity in onto.get_entities(imported=False):
        hit_dict = {'IRI': entity.iri}
        # This is a bit of a hack, need to have a better way to be sure that we only 
        # consider terms defined in the current ontology (and not just referenes here)
        if not entity.iri.split('#')[0] == config["ontology_prefix"].rstrip('#/'):
            continue
            

        #if not (isinstance(entity, owlready2.ThingClass) or isinstance(entity, owlready2.PropertyClass)):
        #    continue

        annotations = {a: a._get_values_for_class(entity) for a in all_annotations if a._get_values_for_class(entity)}
        #annotations=entity.get_annotations()
        long_annotations = ['http://www.w3.org/2004/02/skos/core#example', 'https://w3id.org/emmo#EMMO_c7b62dd7_063a_4c2a_8504_42f7264ba83f']
        annotations_en = {
            key: _extract_all_annotations(item) if key.iri in long_annotations 
            else '; '.join(_extract_all_annotations(item))
            for key, item in annotations.items()
        }

        hit_dict.update(annotations_en)


        parents = [ent for ent in entity.is_a if (isinstance(ent, owlready2.ThingClass) or isinstance(ent, owlready2.PropertyClass))]
        hit_dict["subclassOf"] = parents

        # Fetch direct subclasses
        subclasses = list(entity.subclasses())
        hit_dict["subclasses"] = subclasses

        # Fetch OWL restrictions (object property + someValuesFrom)
        restrictions = [restriction for restriction in entity.is_a if isinstance(restriction, owlready2.Restriction)]
        hit_dict["restrictions"] = restrictions

        text_entities.append(hit_dict)

    text_entities.sort(key=lambda e: e[onto.prefLabel])
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

{underline}
{title}
{underline}

"""

def render_rst_abstract(onto) -> str:

    return f"""

{onto.metadata.abstract.en[0]}

"""

def _get_links(item, key): 
    """Get HTML links for a list of entitities that
    can be fetched from the ontology as keys."""
    links = []
    for ent in item[key]:
        full_iri = ent.iri
        try:
            val = ent.prefLabel.get_lang('en')[0]
        except (IndexError, AttributeError):
            val = ent
        links.append(_html_links(full_iri, display_text=val))

    return links

def _linkify_manchester(text: str, onto) -> str:
   """
   Convert manchester notation as string to HTML links.
   """
   def _replace(match):
       word = match.group(0)
       try:
           full = onto[word].iri
           return _html_links(full, word)
       except (KeyError, AttributeError):
           return word

   return re.sub(r"\w+", _replace, text)

def _html_links(full_iri, display_text):
    """Create the HTML code so that links lead to 
    the correct fragment in the same document if possibe, 
    otherwise link to the full IRI"""
    fragment_iri = full_iri.split('#')[-1]
    return (
        f"<a href='#{fragment_iri}' "
        f"onclick=\""
        f"if(!document.getElementById('{fragment_iri}'))"
        f"{{window.location.href='{full_iri}'; return false;}}"
        f"\">"
        f"{display_text}</a>"
    )

def _add_table_row(rst, key, value):
    try:
        key = get_preferred_label(key)
    except AttributeError:
        key = key
    rst += "  <tr>\n"
    rst += f"    <td class=\"element-table-key\"><span class=\"element-table-key\">{key}</span></td>\n"
    rst += "    <td class=\"element-table-value\">"
    rst += value
    rst += "</td>\n"
    rst += "  </tr>\n"
    return rst


def entities_to_rst(entities: list[dict], onto: Ontology) -> str:
    """Converts extracted ontology terms into an RST format (with proper callouts)."""
    rst = ""
    IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".svg")

    # ---------- helpers ----------
    def _pref_label(obj) -> str | None:
        try:
            lbl = get_preferred_label(obj)
            return str(lbl).strip() if lbl else None
        except Exception:
            return None

    def _norm(s: str) -> str:
        # normalize to test categories: lowercase, remove non-alphanum
        import re
        return re.sub(r"[^a-z0-9]+", "", s.lower())

    def _canon_key(k) -> str:
        """Canonical key for logic (derived from preferred label; fallback to IRI/name)."""
        if isinstance(k, str):
            return _norm(k)
        lbl = _pref_label(k)
        if lbl:
            return _norm(lbl)
        iri = getattr(k, "iri", None)
        if iri:
            frag = iri.split("#")[-1].split("/")[-1]
            return _norm(frag)
        name = getattr(k, "name", None)
        return _norm(name or str(k))

    def _display_key(k) -> str:
        """Pretty label for table left column (use preferred label if available)."""
        lbl = _pref_label(k)
        if lbl:
            return lbl
        # fallbacks: IRI fragment, name, or str
        iri = getattr(k, "iri", None)
        if iri:
            return iri.split("#")[-1].split("/")[-1]
        return getattr(k, "name", None) or str(k)

    def _txt(val) -> str:
        if val is None:
            return ""
        if isinstance(val, (list, tuple)):
            return "\n\n".join(str(x).strip() for x in val if str(x).strip()).strip()
        return str(val).strip()

    def _indent(block: str, n: int = 3) -> str:
        pad = " " * n
        return "\n".join((pad + ln) if ln.strip() else "" for ln in block.splitlines())

    # normalized (via _norm) labels that should render as admonitions
    CALLOUTS = {
        # admonition type -> (directive, optional title)
        # "elucidation": ("admonition", "Elucidation"),
        "note":        ("note", None),
        "comment":     ("note", None),       # treat rdfs:comment as a note (optional)
        "scopenote":   ("note", None),
        "example":     ("admonition", "Example"),
        "tip":         ("tip", None),
        "caution":     ("caution", None),
        "warning":     ("warning", None),
        "important":   ("important", None),
        "danger":      ("danger", None),
        "error":       ("error", None),
    }

    # keys (normalized) never shown in the table
    TABLE_SKIP_BASE = {"iri", "preflabel", "subclassof", "subclasses", "restrictions"}

    for item in entities:
        if '#' not in item['IRI']:
            continue

        iri_prefix, iri_suffix = item['IRI'].split("#")

        # ---- section header
        rst += "\n----\n\n"
        rst += ".. raw:: html\n\n"
        rst += f"   <div id=\"{iri_suffix}\"></div>\n\n"
        title = item[onto.prefLabel]
        rst += f"{title}\n{'-' * len(title)}\n\n"
        rst += f"IRI: {item['IRI']}\n\n"

        # ---- normalize keys once (and keep pretty display names)
        norm = {}          # canonical key -> value
        display_name = {}  # canonical key -> pretty label for table
        for k, v in item.items():
            ck = _canon_key(k)
            norm[ck] = v
            display_name[ck] = _display_key(k)

        # - skip table fields: base + all callouts
        TABLE_SKIP = set(TABLE_SKIP_BASE) | set(CALLOUTS.keys())

        # ---- table (non-callout props)
        rst += ".. raw:: html\n\n"
        rst += "  <table class=\"element-table\">\n"

        for ck, value in norm.items():
            if ck in TABLE_SKIP or value in ("None", "", None):
                continue

            vals = value if isinstance(value, list) else [value]
            for val in vals:
                val = _linkify_value(val)
                rst = _add_table_row(rst, display_name.get(ck, ck), val)

        # ---- restrictions (single row, plain list; safe HTML)
        if item.get("restrictions"):
            restr_strings = []
            for r in item["restrictions"]:
                original = asstring(r)
                restr_strings.append(_linkify_manchester(original, onto))

            # de-duplicate but keep order
            restr_strings = list(dict.fromkeys(restr_strings))

            # build a self-contained snippet to prevent table misalignment
            items_html = "".join(f"<li>{s}</li>" for s in restr_strings)
            val_html = f"<div class=\"restriction-list\"><ul>{items_html}</ul></div>"

            label = "restrictions"
            rst = _add_table_row(rst, label, val_html)


        # ---- subclassOf / subclasses
        if norm.get("subclassof"):
            rst = _add_table_row(rst, 'subclassOf', ", ".join(_get_links(item, "subclassOf")))
        if norm.get("subclasses"):
            rst = _add_table_row(rst, 'subclasses', ", ".join(_get_links(item, "subclasses")))

        rst += "  </table>\n\n"

        # ---- callouts (admonitions) after the table
        for ck, (directive, title_txt) in CALLOUTS.items():
            raw = norm.get(ck)
            if not raw:
                continue

            # normalize to a list of “items to render”
            if isinstance(raw, (list, tuple)):
                items = [str(x).strip() for x in raw if str(x).strip()]
            else:
                # split a single string on blank lines into separate items
                items = [p.strip() for p in str(raw).split("\n\n") if p.strip()]

            if not items:
                continue

            for item_text in items:
                if directive == "admonition":
                    hdr = title_txt or (display_name.get(ck, ck).capitalize())
                    rst += f".. admonition:: {hdr}\n\n"
                else:
                    rst += f".. {directive}::\n\n"
                rst += _indent(item_text) + "\n\n"

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
            rst_content += render_rst_abstract(onto)
            rst_content += entities_to_rst(entities, onto)

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
