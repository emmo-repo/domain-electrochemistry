import networkx as nx
from pyvis.network import Network

# Create a graph
G = nx.Graph()
G.add_nodes_from(["Electrode", "ActiveMaterial", "ClassC", "ClassD"])
G.add_edges_from([("Electrode", "ActiveMaterial"), ("Electrode", "ClassC"), ("ActiveMaterial", "ClassD")])

# Define URLs for each node
node_urls = {
    "Electrode": "https://example.com/Electrode",
    "ActiveMaterial": "https://example.com/ActiveMaterial",
    "ClassC": "https://example.com/classC",
    "ClassD": "https://example.com/classD",
}

# Define labels for specific edges
edge_labels = {
    ("Electrode", "ActiveMaterial"): "hasActiveMaterial",
    ("Electrode", "ClassC"): "label2",
    ("ActiveMaterial", "ClassD"): "label3"
}

fac = 150

# Define manual initial positions for nodes in a top-down tree configuration
node_positions = {
    "Electrode": (0, 0),
    "ActiveMaterial": (1*fac, 1*fac),
    "ClassC": (-1*fac, 1*fac),
    "ClassD": (0, 2*fac)
}

# Create a pyvis network
net = Network(height="1000px", width="1000px", bgcolor="#222222", font_color="white")

# Add nodes with hyperlinks and manual positions
for node, position in node_positions.items():
    net.add_node(node, label=node, title=node_urls[node], link=None, x=position[0], y=position[1])  # Increase font size to 20

# Add edges with arrows, labels, and thicker width
for edge in G.edges:
    net.add_edge(edge[0], edge[1], arrows="to", label=edge_labels.get(edge, ""), length=fac*2, width=5, font={"size": 18})  # Increase font size to 16

# Show the network
net.write_html("graph.html")
