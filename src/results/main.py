import matplotlib.pyplot as plt

def print_information(mem_usage, duration, sil_scores, cal_har_scores, dav_bou_scores):
    print(f"Memory Usage: {mem_usage * 1.048576}MB")
    print(f"Execution Algorithm: {duration.total_seconds()}s")
    print(f"Best Silhouette Score: {max(sil_scores)}")
    print(f"Best Calinksi-Harabasz Index: {max(cal_har_scores)}")
    print(f"Best Davies-Bouldin Index: {min(dav_bou_scores)}")

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