import networkx as nx
from pyvis.network import Network

# Create a graph object
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node("ClassA", url="https://example.com/classA")
G.add_node("ClassB", url="https://example.com/classB")
G.add_node("ClassC", url="https://example.com/classC")
G.add_node("ClassD", url="https://example.com/classD")
G.add_edges_from([("ClassA", "ClassB"), ("ClassA", "ClassC"), ("ClassB", "ClassD")])

# Convert to GraphML format
nx.write_graphml(G, "graph.graphml")

# Load the graph into a pyvis network object
net = Network(height="800px", width="100%", notebook=True)
net.from_nx(G)

# Export the interactive visualization to HTML
net.show("graph.html")
