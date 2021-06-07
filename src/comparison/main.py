import numpy as np
from scipy.cluster.hierarchy import fcluster
from .memory_usage import determine_memory_usage
from .quality import calculate_silhouette_score, calculate_adjust_rand_score  
from .running_time import determine_running_time
from ..algorithms.ravasz import get_labels_ravasz
from ..algorithms.girvan_newman import convert_clusters_to_labels

def determine_measures(graph, adj_matrix, alg, alg_name):
    ((res, duration), mem_usage) = determine_memory_usage(lambda: determine_running_time(alg))

    best_sil_score = None

    if alg_name == "Ravasz":
        for n in range(len(graph.nodes)):
            pred_labels = get_labels_ravasz(res, n)
            sil_score = calculate_silhouette_score(adj_matrix, pred_labels)
            if (sil_score is not None and (best_sil_score is None or sil_score > best_sil_score)):
                best_sil_score = sil_score

    elif alg_name == "Girvan-Newman":
        for clusters in res:
            pred_labels = convert_clusters_to_labels(clusters, len(graph.nodes))
            sil_score = calculate_silhouette_score(adj_matrix, pred_labels)
            if (sil_score is not None and (best_sil_score is None or sil_score > best_sil_score)):
                best_sil_score = sil_score

    return (res, mem_usage, duration, best_sil_score)
