from sklearn.metrics.cluster import pair_confusion_matrix, silhouette_score, adjusted_rand_score, calinski_harabasz_score, davies_bouldin_score

def calculate_fscore(true_labels, pred_labels):
    (tn, fp, fn, tp) = pair_confusion_matrix(true_labels, pred_labels).ravel()

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1 = (2 * precision * recall) / (precision + recall)

    print("Confusion Matrix:")
    print(f"TP: {tp} FP: {fp}")
    print(f"FN: {fn} TN: {tn}")

    return f1

# The higher the score is, the better the clustering
def calculate_silhouette_score(adj_matrix, pred_labels):
    try:
        return silhouette_score(adj_matrix, pred_labels)
    except:
        return None  

# The higher the score is, the better the clustering
def calculate_calinksi_harabsz_score(adj_matrix, pred_labels):
    try:
        return calinski_harabasz_score(adj_matrix, pred_labels)
    except:
        return None

# The lower the score is, the better the clustering
def calculate_davies_bouldin_score(adj_matrix, pred_labels):
    try:
        return davies_bouldin_score(adj_matrix, pred_labels)
    except:
        return None

def calculate_quality_measures(adj_matrix, pred_labels, n, cluster_sizes, sil_scores, cal_har_scores, dav_bou_scores):
    sil_score     = calculate_silhouette_score(adj_matrix, pred_labels)
    cal_har_score = calculate_calinksi_harabsz_score(adj_matrix, pred_labels)
    dav_bou_score = calculate_davies_bouldin_score(adj_matrix, pred_labels)
    if sil_score is not None and cal_har_score is not None and dav_bou_score is not None:
        sil_scores.append(sil_score)
        cal_har_scores.append(cal_har_score)
        dav_bou_scores.append(dav_bou_score)
        cluster_sizes.append(n)

def calculate_adjust_rand_score(true_labels, pred_labels):
    return adjusted_rand_score(true_labels, pred_labels)
