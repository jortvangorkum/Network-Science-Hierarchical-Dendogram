import pandas as pd

def generate_latex_table(clusters_sizes, values, values_name):
    labels = clusters_sizes
    d = {'Number of clusters': labels, values_name: values}
    df_values = pd.DataFrame(d)

    print(f"\n{df_values.to_latex(index=False)}\n")