import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

adjacency = {
    "A": ["B", "C", "D", "F"],
    "B": ["A", "C", "H"],
    "C": ["A", "B", "E", "G", "H", "I"],
    "D": ["A", "E", "F", "G", "K", "L"],
    "E": ["C", "D", "F"],
    "F": ["A", "D", "E"],
    "G": ["C", "D", "I", "K"],
    "H": ["B", "C", "I"],
    "I": ["C", "G", "H", "J", "M"],
    "J": ["I", "K", "M"],
    "K": ["D", "G", "J", "L"],
    "L": ["D", "K", "M"],
    "M": ["I", "J", "L"]
}

for node, neighbors in adjacency.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

print("Jumlah Node:", G.number_of_nodes())
print("Jumlah Edge:", G.number_of_edges())

plt.figure(figsize=(9, 7))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_size=1500,
    font_size=10
)

plt.show()
