from src.results.latex import generate_latex_information
from src.comparison.testing import tost_test, ttest_paired
from src.results.main import print_hypothesis_testing
from src.algorithms.main import execute_algorithms

files = [
    ("Dolphins", "download.tsv.dolphins/dolphins/out.dolphins", "\t"),
    ("PDZBase", "download.tsv.maayan-pdzbase/maayan-pdzbase/out.maayan-pdzbase", "\t"),
    ("David Copperfield", "download.tsv.adjnoun_adjacency/adjnoun_adjacency/out.adjnoun_adjacency_adjacency", " "),
    ("Contiguous USA", "download.tsv.contiguous-usa/contiguous-usa/out.contiguous-usa", " "),
    ("American Football", "download.tsv.dimacs10-football/dimacs10-football/out.dimacs10-football", "\t")
]

def execute_algorithms_on_files():
    for (name, file_path, delimiter) in files:
        print(f"\n\n{name}\n")
        (ravasz, girvan_newman) = execute_algorithms(file_path, delimiter)

        generate_latex_information(name, ravasz, girvan_newman)
        
        print(f"Mem Usage test")
        (p_value, _, _) = tost_test(ravasz[0], girvan_newman[0], 0.01)
        print_hypothesis_testing(p_value)

        print(f"Duration test")
        (p_value, _, _) = tost_test(ravasz[1], girvan_newman[1], 100)
        print_hypothesis_testing(p_value)

        print(f"Silhouette Coefficient test")
        (p_value, _, _) = tost_test(ravasz[2], girvan_newman[2], 0.01)
        print_hypothesis_testing(p_value)

        print(f"Calinksi-Harabasz Index test")
        (p_value, _, _) = tost_test(ravasz[2], girvan_newman[2], 0.1)
        print_hypothesis_testing(p_value)


        print(f"Davies-Bouldin Index")
        (p_value, _, _) = tost_test(ravasz[2], girvan_newman[2], 0.1)
        print_hypothesis_testing(p_value)



execute_algorithms_on_files()