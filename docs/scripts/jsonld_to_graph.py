import json
import networkx as nx
from pyvis.network import Network
import requests
import matplotlib.pyplot as plt


def fetch_context(context_url):
    try:
        response = requests.get(context_url)
        if response.status_code == 200:
            temp = response.json()
            context = temp['@context']
            return context
        else:
            return {}
    except requests.RequestException:
        return {}

def parse_node(graph, data, context, parent=None, relation=None):
    node_type = data.get('@type', 'Unknown')
    if isinstance(node_type, list):
        node_type = ', '.join(node_type)
    
    node_id = f"{node_type} ({id(data)})"
    node_label = node_type
    node_url = context.get(node_type, '') if isinstance(context, dict) else ''
    
    graph.add_node(node_id, label=node_label, url=node_url)

    if parent:
        graph.add_edge(parent, node_id, label=relation)

    for key, value in data.items():
        if key not in ['@type', '@context', 'rdfs:comment']:
            if isinstance(value, dict):
                parse_node(graph, value, context, node_id, key)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        parse_node(graph, item, context, node_id, key)

def visualize_graph_from_jsonld(jsonld):
    data = json.loads(jsonld)
    context_data = data.get('@context', {})

    # Handle context if it's a URL
    context = fetch_context(context_data) if isinstance(context_data, str) else context_data

    G = nx.DiGraph()
    parse_node(G, data, context)
    
    net = Network(height="800px", width="1000px", directed=True, bgcolor="#ffffff", font_color="black")
    # Adjusting the physics for better layout
    net.barnes_hut(gravity=-8000, central_gravity=0.3, spring_length=200, spring_strength=0.05, damping=0.09, overlap=0)

    for node, node_attrs in G.nodes(data=True):
        net.add_node(node, label=node_attrs['label'], title=node_attrs['url'], url=node_attrs.get('url', '#'))

    for src, dst, data in G.edges(data=True):
        net.add_edge(src, dst, label=data['label'], font={'align': 'top'}, smooth={'type': 'horizontal'})

    net.write_html("network_graph.html")
    
    # Create the static graph using matplotlib
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.savefig("network_graph.png")


# Example JSON-LD data
jsonld_description = """
{
    "@context": "https://w3id.org/emmo/domain/battery/context/context",
    "@type": "BatteryCell",
    "hasPositiveElectrode":{
        "@type": "CoatedElectrode",
        "hasCoating": {
            "@type": "ElectrodeCoating",
            "hasActiveMaterial": {
                "@type": "LithiumIronPhosphate",
                "rdfs:comment": "for example"
            },
            "hasConstituent": [
                {
                    "@type": "Binder"
                },
                {
                    "@type": "ConductiveAdditive"
                }
            ]
        },
        "hasCurrentCollector": {
            "@type": ["CurrentCollector", "Aluminium"],
            "rdfs:comment": "for example"
        }
    }
}
"""

# Run the function with the provided JSON-LD
visualize_graph_from_jsonld(jsonld_description)
