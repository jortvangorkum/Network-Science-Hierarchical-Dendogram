from scipy.cluster.hierarchy import linkage, fcluster

def ravasz_algorithm(adj_matrix, method = 'average'):
    Z = linkage(adj_matrix, method=method)
    return Z

def get_labels_ravaz(Z, max_clusters):
    l = fcluster(Z, max_clusters, criterion='maxclust')
    return l