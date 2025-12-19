import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = {
    'source_user':[
        'andi', 'budi', 'citra', 'andi', 'dina',
        'eko', 'budi', 'citra', 'dina', 'andi'
    ],
    'target_user':[
        'budi', 'andi', 'andi', 'citra', 'andi',
        'andi', 'dina', 'eko', 'citra', 'eko'
    ],
    'interaction':[
        'like', 'comment', 'mention', 'comment', 'like',
        'mention', 'comment', 'like', 'mention', 'comment'
    ]
}
df = pd.DataFrame(data)
print("=== DATA INTERAKSI MEDIA SOSIAL ===")
print(df)

# 2. Membuat Graph dari Data

G = nx.DiGraph()

# Menambahkan edge berdasarkan interaksi
for idx, row in df.iterrows():
  G.add_edge(row['source_user'], row['target_user'], interaction=row['interaction'])
  print("\nJumlah Node:", G.number_of_nodes())
  print("Jumlah Edge:", G.number_of_edges())

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [
    ["A", "B"],
    ["A", "D"],
    ["B", "C"],
    ["C", "E"],
    ["D", "E"]
]
G.add_edges_from(edges)

# Menghitung centrality
degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
closeness = nx.closeness_centrality(G)

print("Degree Centrality", degree)
print("Betweenness Centrality", betweenness)
print("Closeness Centrality", closeness)

# Visualisasi
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

# 4. Analisis SNA (Centrality)

# Re-create G as a directed graph from social media data to ensure in_degree can be calculated.
# This section assumes the user wants to analyze the social media network.
G = nx.DiGraph()
for idx, row in df.iterrows():
  G.add_edge(row['source_user'], row['target_user'], interaction=row['interaction'])

# Degree Centrality
degree_centrality = nx.degree_centrality(G)

# In-Degree Centrality (Siapa paling banyak mendapat interaksi)
indegree = G.in_degree()
in_centrality = {node: val for node, val in indegree}

# Betweenness Centrality (penghubung antar pengguna)
betweenness = nx.betweenness_centrality(G)

print("\n=== DEGREE CENTRALITY ===")
print(degree_centrality)

print("\n=== IN-DEGREE CENTRALITY (POPULARITAS) ===")
print(in_centrality)

print("\n=== BETWEENNESS CENTRALITY (INFLUENCE) ===")
print(betweenness)

# 5. Mendeteksi Influecer

# Influencer = pengguna dengan betweenness atau indegree tertinggi 
influencer_by_popularity = max(in_centrality, key = in_centrality.get)
influencer_by_influence = max(betweenness, key = betweenness.get)

print("Influencer Berdasarkan Banyaknya Interaksi (Indegree):", influencer_by_popularity)
print("Influencer Berdasarkan Posisi Jaringan (Betweenness):", influencer_by_influence)

# 6. Deteksi Komunitas (Girvan-Newman)

from networkx.algorithms.community import girvan_newman
communities = girvan_newman(G)
top_level_communities = tuple(sorted(c) for c in next(communities))

print("\n=== KOMUNITAS TERDETEKSI ===")
print(top_level_communities)
