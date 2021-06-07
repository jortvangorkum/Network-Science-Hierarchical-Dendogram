from src.algorithms.girvan_newman import girvan_newman_algorithm
from src.algorithms.ravasz import ravasz_algorithm
from src.comparison.main import determine_measures
from src.data import get_data_from_path

def execute_ravasz_algorithm():
    (G, A, L, label_count) = get_data_from_path("download.tsv.dolphins/dolphins/out.dolphins", "\t")

    (Z, mem_usage, duration, sil_score) = determine_measures(G, A, lambda: ravasz_algorithm(A), "Ravasz")

    print("Ravasz:")
    print(f"Memory Usage: {mem_usage * 1.048576}MB")
    print(f"Execution Algorithm: {duration.total_seconds()}s")
    print(f"Silhouette Score: {sil_score}")

def execute_girvan_newman_algorithm():
    (G, A, L, label_count) = get_data_from_path("download.tsv.dolphins/dolphins/out.dolphins", "\t")

    (clusters, mem_usage, duration, sil_score) = determine_measures(G, A, lambda: girvan_newman_algorithm(G), "Girvan-Newman")

    print("\nGirvan-Newman:")
    print(f"Memory Usage: {mem_usage * 1.048576}MB")
    print(f"Execution Algorithm: {duration.total_seconds()}s")
    print(f"Silhouette Score: {sil_score}")

execute_ravasz_algorithm()
execute_girvan_newman_algorithm()
