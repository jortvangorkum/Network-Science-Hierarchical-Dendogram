import pandas as pd
import numpy as np

def generate_latex_table(clusters_sizes, values, values_name):
    labels = clusters_sizes
    d = {'Number of clusters': labels, values_name: values}
    df_values = pd.DataFrame(d)

    print(f"\n{df_values.to_latex(index=False)}\n")

def generate_latex_information(dataset_name, ravasz_values, girvan_newman_values):
    d = {
        'Dataset': dataset_name,
        'Algorithm': ['Ravasz', 'Girvan Newman'],
        'Memory Usage': [np.mean(ravasz_values[0]), np.mean(girvan_newman_values[0])],
        'Duration': [np.mean(ravasz_values[1]), np.mean(girvan_newman_values[1])],
        'Silhouette Coefficient': [np.mean(ravasz_values[2]), np.mean(girvan_newman_values[2])],
        'Calinksi-Harabasz Index': [np.mean(ravasz_values[3]), np.mean(girvan_newman_values[3])],
        'Davies-Bouldin Index': [np.mean(ravasz_values[4]), np.mean(girvan_newman_values[4])]
    }
    df_values = pd.DataFrame(d)

    print(f"\n{df_values.to_latex(index=False)}\n")