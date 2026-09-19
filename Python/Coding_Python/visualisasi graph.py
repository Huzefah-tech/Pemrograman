import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# 4.Visualisasi graph

plt.figure(figsize=(10, 7))

# Memisahkan node customer dan product
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos,
with_labesl=True,
node_color=['lightblue' if node in customers else 'orange' for node in G.nodes()],
node_size=1500,
font_size=10)

plt.title("Customer-Product Network (ANS Bisnis)")
plt.show()

# 5. 

# 1.. Visualisasi Jaringan Pelanggan Produk

Node biru = Pelanggan
Node oranye = Produk