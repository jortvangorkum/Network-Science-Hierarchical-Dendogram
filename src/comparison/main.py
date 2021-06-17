from .memory_usage import determine_memory_usage
from .quality import calculate_quality_measures
from .running_time import determine_running_time
from ..algorithms.ravasz import get_labels_ravasz
from ..algorithms.girvan_newman import convert_clusters_to_labels

def determine_measures(graph, adj_matrix, alg, alg_name):
    durations =  []
    mem_usages = []

    res = alg()

    for _ in range(100):
        ((_, duration), mem_usage) = determine_memory_usage(lambda: determine_running_time(alg))
        durations.append(duration.total_seconds() * 1000)
        mem_usages.append(mem_usage * 1.048576)


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
        for clusters in res[:-1]:
            pred_labels = convert_clusters_to_labels(clusters, n)
            calculate_quality_measures(adj_matrix, pred_labels, len(clusters), clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)

    return (res, mem_usages, durations, clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)
