from sklearn.metrics.cluster import pair_confusion_matrix, silhouette_score, adjusted_rand_score

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

def calculate_silhouette_score(adj_matrix, pred_labels):
    return silhouette_score(adj_matrix, pred_labels)

def calculate_adjust_rand_score(true_labels, pred_labels):
    return adjusted_rand_score(true_labels, pred_labels)
