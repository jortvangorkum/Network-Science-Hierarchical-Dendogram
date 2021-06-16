import numpy as np
from scipy.cluster.hierarchy import fcluster
from .memory_usage import determine_memory_usage
from .quality import calculate_calinksi_harabsz_score, calculate_quality_measures, calculate_silhouette_score, calculate_adjust_rand_score  
from .running_time import determine_running_time
from ..algorithms.ravasz import get_labels_ravasz
from ..algorithms.girvan_newman import convert_clusters_to_labels

def determine_measures(graph, adj_matrix, alg, alg_name):
    ((res, duration), mem_usage) = determine_memory_usage(lambda: determine_running_time(alg))

    sil_scores     = []
    cal_har_scores = []
    dav_bou_scores = []
    clusters_sizes = []

    if alg_name == "Ravasz":
        for n in range(2, len(graph.nodes)):
            pred_labels = get_labels_ravasz(res, n)
            calculate_quality_measures(adj_matrix, pred_labels, n, clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)

    elif alg_name == "Girvan-Newman":
        n = len(graph.nodes)
        for clusters in res:
            pred_labels = convert_clusters_to_labels(clusters, n)
            calculate_quality_measures(adj_matrix, pred_labels, len(clusters), clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)

    return (res, mem_usage, duration, clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)
