from networkx.algorithms.centrality.betweenness import edge_betweenness_centrality
from networkx.algorithms.community.centrality import girvan_newman

def highest_valuable_edge(graph, k):
    betweenness = edge_betweenness_centrality(graph, k=k)
    return max(betweenness, key=betweenness.get)

def girvan_newman_algorithm(graph, k=None):
    if k is not None:
        return girvan_newman(graph, lambda g: highest_valuable_edge(g, k))

    return girvan_newman(graph)

