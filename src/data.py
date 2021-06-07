import networkx as nx
import numpy as np
from networkx.linalg.graphmatrix import adjacency_matrix

# Create data
def get_data_from_path(filePath, labelPath, delimiter):
    G = nx.read_edgelist(f"./datasets/{filePath}", delimiter=delimiter, create_using=nx.Graph())
    A = adjacency_matrix(G).todense()
    L = np.loadtxt(f"./datasets/{labelPath}", dtype=int, delimiter=delimiter, skiprows=1)
    with open(f"./datasets/{labelPath}") as f:
        label_count = int(f.readline())
    
    return (G, A, L, label_count)

# print("GOT HERE")
# gn_res = np.array(list(comp), dtype=object)
# print(gn_res)
# print("FINISHED")

# print(l_gn[0:10])

# sil_score = silhouette_score(A, l)
# r_score = adjusted_rand_score(L, l)
# f_score = calculate_fscore(L, l)

# print(f"Silhouette Coefficient: {sil_score}")
# print(f"F Score: {f_score}")
# print(f"Adjusted Rand Index: {r_score}")

# Show data
# dn = dendrogram(l)
# nx.draw(G)
# plt.show()
