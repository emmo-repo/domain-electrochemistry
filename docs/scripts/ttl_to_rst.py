import os
from rdflib import Graph, URIRef, Literal


########## LOAD TTL ################

def load_ttl_from_file(filepath: str) -> Graph:
    """Loads a TTL file into an RDFLib Graph."""
    g = Graph()
    g.parse(filepath, format="turtle")
    return g


########## QUERY TTL ################

def extract_terms_info_sparql(g: Graph) -> list:
    """Extracts terms from the TTL graph using SPARQL, including parent and subclass links."""
    text_entities = []

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

        # Fetch direct parents (rdfs:subClassOf)
        parents = []
        parent_query = PREFIXES + """
            SELECT ?parent ?parentLabel WHERE {
                <%s> rdfs:subClassOf ?parent .
                ?parent skos:prefLabel ?parentLabel .
            }
        """ % hit_dict['IRI']
        for row in g.query(parent_query):
            parent_iri, parent_label = row
            parents.append((str(parent_iri), str(parent_label)))
        hit_dict["Parent Classes"] = parents

        # Fetch direct subclasses
        subclasses = []
        subclass_query = PREFIXES + """
            SELECT ?subclass ?subclassLabel WHERE {
                ?subclass rdfs:subClassOf <%s> .
                ?subclass skos:prefLabel ?subclassLabel .
            }
        """ % hit_dict['IRI']
        for row in g.query(subclass_query):
            subclass_iri, subclass_label = row
            subclasses.append((str(subclass_iri), str(subclass_label)))
        hit_dict["Subclasses"] = subclasses

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
    """Converts extracted ontology terms into an RST format, including parent/subclass links."""
    rst = ""

    for item in entities:
        if '#' not in item['IRI']:
            continue

        iri_prefix, iri_suffix = item['IRI'].split("#")

        # Add Sphinx anchor for permalinks
        rst += f".. _{iri_suffix}:\n\n"
        
        rst += f"{item['prefLabel']}\n"
        rst += "-" * len(item['prefLabel']) + "\n\n"
        rst += f"* {item['IRI']}\n\n"

        rst += ".. raw:: html\n\n"
        rst += "  <table class=\"element-table\">\n"

        for key, value in item.items():
            if key not in ['IRI', 'prefLabel', 'Parent Classes', 'Subclasses'] and value not in ["None", ""]:
                rst += "  <tr>\n"
                rst += f"    <td class=\"element-table-key\"><span class=\"element-table-key\">{key}</span></td>\n"

                if value.startswith("http"):
                    value = f"<a href='{value}'>{value}</a>"
                rst += f"    <td class=\"element-table-value\">{value}</td>\n"
                rst += "  </tr>\n"

        # Add parent classes section
        if item["Parent Classes"]:
            rst += "  <tr>\n"
            rst += "    <td class=\"element-table-key\"><span class=\"element-table-key\">Parent Classes</span></td>\n"
            rst += "    <td class=\"element-table-value\">"
            parent_links = [f"<a href='#{iri.split('#')[-1]}'>{label}</a>" for iri, label in item["Parent Classes"]]
            rst += ", ".join(parent_links)
            rst += "</td>\n"
            rst += "  </tr>\n"

        # Add subclasses section
        if item["Subclasses"]:
            rst += "  <tr>\n"
            rst += "    <td class=\"element-table-key\"><span class=\"element-table-key\">Subclasses</span></td>\n"
            rst += "    <td class=\"element-table-value\">"
            subclass_links = [f"<a href='#{iri.split('#')[-1]}'>{label}</a>" for iri, label in item["Subclasses"]]
            rst += ", ".join(subclass_links)
            rst += "</td>\n"
            rst += "  </tr>\n"

        rst += "  </table>\n\n"

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
