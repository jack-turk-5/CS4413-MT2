import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

distances = {
    ('a', 'b'): sqrt(2), ('a', 'c'): 3, ('a', 'd'): 2, ('a', 'e'): sqrt(5), ('a', 'f'): sqrt(10),
    ('b', 'c'): sqrt(5), ('b', 'd'): sqrt(5), ('b', 'e'): sqrt(2), ('b', 'f'): 1, ('c', 'd'): sqrt(13),
    ('c', 'e'): sqrt(8), ('c', 'f'): 1, ('d', 'e'): 1, ('d', 'f'): sqrt(10), ('e', 'f'): sqrt(5)
}

G = nx.Graph()

for edge, weight in distances.items():
    G.add_edge(*edge, weight=weight)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('City Graph')
plt.show()

# Compute MST using Prim's algorithm
mst_prim = nx.minimum_spanning_tree(G, algorithm='prim')
print("MST using Prim's algorithm:")
print(mst_prim.edges(data=True))

# Compute MST using Kruskal's algorithm
mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal')
print("\nMST using Kruskal's algorithm:")
print(mst_kruskal.edges(data=True))

# Compute all pair shortest paths
shortest_paths = dict(nx.all_pairs_shortest_path(G))
print("\nAll pair shortest paths:")
for source, paths in shortest_paths.items():
    print(f"From {source}:")
    for target, path in paths.items():
        print(f"To {target}: {path}, Length: {nx.shortest_path_length(G, source, target, weight='weight')}")

