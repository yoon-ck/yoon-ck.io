import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_edges_from([(1,2),(1,3)])
nx.draw(G)
plt.show()
