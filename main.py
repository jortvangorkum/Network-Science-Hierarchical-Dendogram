import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

X = nx.read_edgelist("./datasets/networks/protein.edgeslist.txt", delimiter='\t', create_using=nx.Graph())

# setting distance_threshold=0 ensures we compute the full tree.
model = linkage(X, 'average')

dn = dendrogram(model)

plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()