import networkx as nx
import numpy as np
from networkx.linalg.graphmatrix import adjacency_matrix
from scipy.cluster.hierarchy import linkage

# Create data
def get_data_from_path(filePath, delimiter, labelPath = None):
    G = nx.read_edgelist(f"./datasets/{filePath}", delimiter=delimiter, comments="%", create_using=nx.Graph())
    A = adjacency_matrix(G).todense()
    if labelPath is not None:
        L = np.loadtxt(f"./datasets/{labelPath}", dtype=int, delimiter=delimiter, skiprows=1)
        with open(f"./datasets/{labelPath}") as f:
            label_count = int(f.readline())
        
        return (G, A, L, label_count)  
    
    return (G, A, None, None)
