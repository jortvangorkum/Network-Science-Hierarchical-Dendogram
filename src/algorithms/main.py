import matplotlib.pyplot as plt

from src.results.latex import generate_latex_table
from src.results.dendrogram import networkx_to_dendrogram, scipy_to_dendrogram
from src.results.main import graph_quality_measures, print_information
from src.algorithms.girvan_newman import girvan_newman_algorithm
from src.algorithms.ravasz import ravasz_algorithm
from src.comparison.main import determine_measures
from src.data import get_data_from_path

def execute_ravasz_algorithm(file_path, delimiter):
    (G, A, L, label_count) = get_data_from_path(file_path, delimiter)

    (Z, mem_usages, durations, clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores) = determine_measures(G, A, lambda: ravasz_algorithm(A), "Ravasz")

    print("Ravasz:")
    print_information(mem_usages, durations, sil_scores, cal_har_scores, dav_bou_scores)
    graph_quality_measures(clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)
    scipy_to_dendrogram(Z)

    return (mem_usages, durations, sil_scores, cal_har_scores, dav_bou_scores)
    
def execute_girvan_newman_algorithm(file_path, delimiter):
    (G, A, L, label_count) = get_data_from_path(file_path, delimiter)

    (clusters, mem_usages, durations, clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores) = determine_measures(G, A, lambda: girvan_newman_algorithm(G), "Girvan-Newman")

    print("\nGirvan-Newman:")
    print_information(mem_usages, durations, sil_scores, cal_har_scores, dav_bou_scores)
    graph_quality_measures(clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores)
    networkx_to_dendrogram(G, clusters)

    return (mem_usages, durations, sil_scores, cal_har_scores, dav_bou_scores)

def execute_algorithms(file_path, delimiter):
    ravasz = execute_ravasz_algorithm(file_path, delimiter)
    girvan_newman = execute_girvan_newman_algorithm(file_path, delimiter)
    return (ravasz, girvan_newman)

