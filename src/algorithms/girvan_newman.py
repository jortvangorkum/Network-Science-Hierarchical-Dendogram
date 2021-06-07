from networkx.algorithms.centrality.betweenness import edge_betweenness_centrality
from networkx.algorithms.community.centrality import girvan_newman
import numpy as np

def highest_valuable_edge(graph, k):
    betweenness = edge_betweenness_centrality(graph, k=k)
    return max(betweenness, key=betweenness.get)

def create_list_of_iterator(iterator):
    return np.array(list(iterator), dtype=object)

def girvan_newman_algorithm(graph, k=None):
    if k is not None:
        return create_list_of_iterator(girvan_newman(graph, lambda g: highest_valuable_edge(g, k)))

    return create_list_of_iterator(girvan_newman(graph))

def convert_clusters_to_labels(clusters, n_nodes):
    pred_labels = np.empty(n_nodes)
    for (i, cluster) in enumerate(clusters):
        for x in cluster:
            pred_labels[int(x) - 1] = i
    return pred_labels