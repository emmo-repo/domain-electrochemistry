import os
from rdflib import Graph


########## LOAD TTL ################

def load_ttl_from_file(filepath: str) -> Graph:
    """Loads a TTL file into an RDFLib Graph."""
    g = Graph()
    g.parse(filepath, format="turtle")
    return g


########## QUERY TTL ################

def extract_terms_info_sparql(g: Graph) -> list:
    """Extracts terms from the TTL graph using SPARQL."""
    text_entities = []

    # SPARQL QUERY #
    PREFIXES = """
        PREFIX emmo: <https://w3id.org/emmo#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        """

    list_entity_types = [
        "IRI", "prefLabel", "Elucidation", "Alternative Label(s)", 
        "IEC Reference", "IUPAC Reference", "Wikipedia Reference", 
        "Wikidata Reference", "Comment", 
        "Tip", "Caution", "Important", "Note", "Danger", "Error", 
        "Warning", "Admonition"
    ]

    query = PREFIXES + """
        SELECT ?iri ?prefLabel ?elucidation 
               (GROUP_CONCAT(?altLabel; SEPARATOR=", ") AS ?altLabels) 
               ?iecref ?iupacref ?wikipediaref ?wikidataref 
               ?comment ?tip ?caution ?important ?note ?danger
               ?error ?warning ?admonition
        WHERE {
            ?iri skos:prefLabel ?prefLabel.
            
            OPTIONAL { ?iri emmo:EMMO_967080e5_2f42_4eb2_a3a9_c58143e835f9 ?elucidation . }
            OPTIONAL { ?iri skos:altLabel ?altLabel . }
            OPTIONAL { ?iri emmo:EMMO_50c298c2_55a2_4068_b3ac_4e948c33181f ?iecref . }
            OPTIONAL { ?iri emmo:EMMO_fe015383_afb3_44a6_ae86_043628697aa2 ?iupacref . }
            OPTIONAL { ?iri emmo:EMMO_c84c6752_6d64_48cc_9500_e54a3c34898d ?wikipediaref . }
            OPTIONAL { ?iri emmo:EMMO_26bf1bef_d192_4da6_b0eb_d2209698fb54 ?wikidataref . }
            OPTIONAL { ?iri rdfs:comment ?comment . }

            # Extract callout annotations
            OPTIONAL { ?iri emmo:EMMO_b6730304_cabc_4104_b415_14218466445c ?caution . }
            OPTIONAL { ?iri emmo:EMMO_5f7abc2a_5b50_41c3_8def_c8ba7c3b083e ?tip . }
            OPTIONAL { ?iri emmo:EMMO_4c8480cf_56de_41da_8699_f12a9033313a ?important . }
            OPTIONAL { ?iri skos:note ?note . }
            OPTIONAL { ?iri emmo:EMMO_95317324_4b53_4665_a087_82c3a2a0540b ?danger . }
            OPTIONAL { ?iri emmo:EMMO_32214c66_8bce_40f5_b22d_5059f6cf571b ?error . }
            OPTIONAL { ?iri emmo:EMMO_0fa6566e_500f_4d24_baa9_b2b22c9a0b72 ?warning . }
            OPTIONAL { ?iri emmo:EMMO_709ee08d_76b1_4fee_be22_925412ac313b ?admonition . }
        }
        GROUP BY ?iri ?prefLabel ?elucidation ?caution ?tip ?important ?note ?danger ?error ?warning ?admonition
        """
        
    qres = g.query(query)

    for hit in qres:    
        hit_dict = {entity_type: str(entity) for entity_type, entity in zip(list_entity_types, hit)}
        text_entities.append(hit_dict)

    text_entities.sort(key=lambda e: e["prefLabel"])

    return text_entities


########## RENDER RST HEADER ################

def render_rst_top() -> str:
    return """
===================
Electrochemistry Terms
===================

This page lists all terms extracted from the electrochemistry-related ontologies.
"""


########## RENDER RST CONTENT ################

def entities_to_rst(entities: list[dict]) -> str:
    """Converts extracted ontology terms into an RST format."""
    rst = ""

    for item in entities:
        if '#' not in item['IRI']:
            continue

        iri_prefix, iri_suffix = item['IRI'].split("#")

        rst += ".. raw:: html\n\n"
        rst += "   <div id=\"" + iri_suffix + "\"></div>\n\n"
        
        rst += item['prefLabel'] + "\n"
        rst += "-" * len(item['prefLabel']) + "\n\n"
        rst += "* " + item['IRI'] + "\n\n"

        rst += ".. raw:: html\n\n"
        indent = "  "
        rst += indent + "<table class=\"element-table\">\n"
        
        for key, value in item.items():
            if key not in ['IRI', 'prefLabel'] and value not in ["None", ""]:
                rst += indent + "<tr>\n"
                rst += indent + "<td class=\"element-table-key\"><span class=\"element-table-key\">" + key + "</span></td>\n"
                
                if value.startswith("http"):
                    value = f"""<a href='{value}'>{value}</a>"""
                else:
                    value = value.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    value = value.replace('\n', '\n' + indent)

                rst += indent + "<td class=\"element-table-value\">" + value + "</td>\n"
                rst += indent + "</tr>\n"
        
        rst += indent + "</table>\n\n"

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
                callout_rst += f".. {admonition}::\n\n   {callout_value}\n\n"

        rst += callout_rst

    return rst


########## RENDER RST FOOTER ################

def render_rst_bottom() -> str:
    return """
End of Document.
"""


########### RUN THE RENDERING WORKFLOW ##############

def rendering_workflow():
    """Compiles all extracted terms into a single RST file."""
    ttl_files = [
        {"section title": "Electrochemistry Reference", "path": "./reference/electrochemistry-reference.ttl"},
        {"section title": "Electrochemistry Quantities", "path": "./reference/electrochemistry-quantities.ttl"},
        {"section title": "Electrochemistry Manufacturing", "path": "./modules/electrochemistry-manufacturing.ttl"},
        {"section title": "Electrochemistry Testing", "path": "./modules/electrochemistry-testing.ttl"},
    ]

    rst_filename = "./docs/electrochemistry.rst"
    rst_content = render_rst_top()

    for module in ttl_files:
        filepath = module["path"]
        if os.path.isfile(filepath):
            g = load_ttl_from_file(filepath)
            entities_list = extract_terms_info_sparql(g)

            rst_content += f"\n{module['section title']}\n"
            rst_content += "=" * len(module['section title']) + "\n\n"
            rst_content += entities_to_rst(entities_list)
        else:
            print(f"Warning: {filepath} not found.")

    rst_content += render_rst_bottom()

    with open(rst_filename, "w+", encoding="utf-8") as f:
        f.write(rst_content)

    print(f"RST file generated: {rst_filename}")


if __name__ == "__main__":
    rendering_workflow()
