import networkx as nx
from pyvis.network import Network

# Create a directed graph
G = nx.DiGraph()
nodes = [
    "CoatedElectrode", "PositiveElectrode", "ElectrodeCoating",
    "CurrentCollector", "ActiveMaterial", "ConductiveAdditive", "Binder"
]
edges = [
    ("PositiveElectrode", "CoatedElectrode", {"label": "isA"}),
    ("PositiveElectrode", "ElectrodeCoating", {"label": "hasCoating"}),
    ("PositiveElectrode", "CurrentCollector", {"label": "hasCurrentCollector"}),
    ("ElectrodeCoating", "ActiveMaterial", {"label": "hasActiveMaterial"}),
    ("ElectrodeCoating", "ConductiveAdditive", {"label": "hasConstituent"}),
    ("ConductiveAdditive", "Binder", {"label": "hasConstituent"})
]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from([(src, dst, attr) for src, dst, attr in edges])

# Setup network visualization
net = Network(height="800px", width="600px", directed=True, bgcolor="#ffffff", font_color="black")
net.force_atlas_2based(gravity=-800, central_gravity=0.05, spring_length=200, spring_strength=0.05, damping=0.4)

# Manually set initial positions to create a structured tree layout
positions = {
    "PositiveElectrode": (0, 0),
    "CoatedElectrode": (0, -200),
    "ElectrodeCoating": (-300, 100),
    "CurrentCollector": (300, 100),
    "ActiveMaterial": (-450, 200),
    "ConductiveAdditive": (-150, 200),
    "Binder": (-150, 300)
}

# Add nodes with positions and settings for better layout
for node, position in positions.items():
    net.add_node(node, label=node, title=node, x=position[0], y=position[1], color="#f0ad4e", size=35)

# Add edges with specific styles and smooth curves
for src, dst, attr in edges:
    net.add_edge(src, dst, label=attr['label'], color="#007bff", width=2, smooth={'type': 'curved', 'roundness': 0.2})

# Save the network graph as an HTML file
net.write_html("network.html")
