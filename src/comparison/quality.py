import math
from sklearn.metrics.cluster import pair_confusion_matrix, silhouette_score, adjusted_rand_score, calinski_harabasz_score, davies_bouldin_score

# The higher the score is, the better the clustering
def calculate_silhouette_score(adj_matrix, pred_labels):
    try:
        return silhouette_score(adj_matrix, pred_labels)
    except Exception as e:
        print(e)
        return float('nan')
  

# The higher the score is, the better the clustering
def calculate_calinksi_harabsz_score(adj_matrix, pred_labels):
    try:
        return calinski_harabasz_score(adj_matrix, pred_labels)
    except Exception as e:
        print(e)
        return float('nan')


# The lower the score is, the better the clustering
def calculate_davies_bouldin_score(adj_matrix, pred_labels):
    try:
        return davies_bouldin_score(adj_matrix, pred_labels)
    except Exception as e:
        print(e)
        return float('nan')


def calculate_quality_measures(adj_matrix, pred_labels, n, cluster_sizes, sil_scores, cal_har_scores, dav_bou_scores):
    sil_score     = calculate_silhouette_score(adj_matrix, pred_labels)
    cal_har_score = calculate_calinksi_harabsz_score(adj_matrix, pred_labels)
    dav_bou_score = calculate_davies_bouldin_score(adj_matrix, pred_labels)

    if math.isnan(sil_score) or math.isnan(cal_har_score) or math.isnan(dav_bou_score):
        print(n)

    sil_scores.append(sil_score)
    cal_har_scores.append(cal_har_score)
    dav_bou_scores.append(dav_bou_score)
    cluster_sizes.append(n)

def calculate_adjust_rand_score(true_labels, pred_labels):
    return adjusted_rand_score(true_labels, pred_labels)
