import networkx as nx
import matplotlib.pyplot as plt
 
g = nx.Graph()
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
 
nx.draw(g)
plt.show()
#plt.savefig("filename.png")
