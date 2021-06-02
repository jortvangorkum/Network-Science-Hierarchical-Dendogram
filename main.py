import numpy as np
import networkx as nx
import pandas as pd
import time

from datetime import timedelta as td
from networkx.algorithms.community.centrality import girvan_newman as gn
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.datasets import load_wine
from sklearn.metrics import rand_score

def load_data(loader):
    dataset = loader(as_frame=True)
    G = dataset.data
    cluster_amount = len(dataset.target_names)
    return (G, dataset.target, cluster_amount)

def hierarchical_algorithm(alg, name):
    print(f"Executing {name} algorithm...")
    start_time = time.monotonic()
    model = alg()
    end_time = time.monotonic()
    print(f"Duration {name}: {td(seconds=end_time - start_time)}")
    return model

def plot_target_trained(actual_values, preds, name):
    _, axes = plt.subplots(1, 2)
    axes[0].scatter(G.iloc[:,0], G.iloc[:,1], c=actual_values)
    axes[1].scatter(G.iloc[:,0], G.iloc[:,1], c=preds, cmap=plt.cm.Set1)
    axes[0].set_title('Actual', fontsize=18)
    axes[1].set_title(name, fontsize=18)

""" Load Data """

(G, actual_values, cluster_amount) = load_data(load_wine)

""" Divisive """


# comp = gn(G)

# dn = dendrogram(list(comp))


""" Agglomerative """

model = hierarchical_algorithm(lambda: linkage(G, 'average'), 'Agglomerative[Linkage = Average]')

preds = fcluster(model, cluster_amount, criterion='maxclust')

plot_target_trained(actual_values, preds, "Agglomerative[Linkage = Average]")

r_score = rand_score(actual_values, preds)

print(f"Rand Score: {r_score}")

# dn = dendrogram(model)

plt.show()