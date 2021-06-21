import matplotlib.pyplot as plt
import numpy as np

def print_graph_information(name, values):
    avg_mem_usage = np.mean(values)
    min_mem_usage = np.min(values)
    max_mem_usage = np.max(values)
    print(f"{{{name}}} {avg_mem_usage} {max_mem_usage} {min_mem_usage}")

def print_information(mem_usages, durations, sil_scores, cal_har_scores, dav_bou_scores):
    print(f"Average Memory Usage: {np.mean(mem_usages)}MB")
    print(f"Average Execution Algorithm: {np.mean(durations)}ms")
    print(f"Average Silhouette Score: {np.mean(sil_scores)}")
    print(f"Average Calinksi-Harabasz Index: {np.mean(cal_har_scores)}")
    print(f"Average Davies-Bouldin Index: {np.mean(dav_bou_scores)}")

def graph_quality_measures(clusters_sizes, sil_scores, cal_har_scores, dav_bou_scores):
    x = clusters_sizes
    (fig, (ax1, ax2, ax3)) = plt.subplots(1, 3)
    ax1.bar(x, sil_scores)
    ax1.title.set_text("Silhouette Coefficient")
    ax2.bar(x, cal_har_scores)
    ax2.title.set_text("Calinksi-Harabasz Index")
    ax3.bar(x, dav_bou_scores)
    ax3.title.set_text("Davies-Bouldin Index")
    plt.show()

def print_hypothesis_testing(p_value):
    if (p_value > 0.05):
        print(f"Samples are uncorrelated (fail to reject H0) p={p_value}")
    else:
        print(f"Samples are correlated (reject H0) p={p_value}")