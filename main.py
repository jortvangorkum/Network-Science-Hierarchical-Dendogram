from src.results.latex import generate_latex_information
from src.comparison.testing import tost_test, ttest_paired
from src.results.main import print_graph_information, print_hypothesis_testing
from src.algorithms.main import execute_algorithms

import matplotlib.pyplot as plt

dpi = 96
plt.rcParams["figure.figsize"] = (2000 / dpi, 1200 / dpi)
plt.rcParams["figure.dpi"] = dpi

files = [
    ("Contiguous USA", "download.tsv.contiguous-usa/contiguous-usa/out.contiguous-usa", " "),
    ("Dolphins", "download.tsv.dolphins/dolphins/out.dolphins", "\t"),
    ("PDZBase", "download.tsv.maayan-pdzbase/maayan-pdzbase/out.maayan-pdzbase", "\t"),
    ("David Copperfield", "download.tsv.adjnoun_adjacency/adjnoun_adjacency/out.adjnoun_adjacency_adjacency", " "),
    ("American Football", "download.tsv.dimacs10-football/dimacs10-football/out.dimacs10-football", "\t")
]

def execute_algorithms_on_files():
    for (name, file_path, delimiter) in files:
        print(f"\n\n{name}\n")
        (ravasz, girvan_newman) = execute_algorithms(file_path, delimiter)

        generate_latex_information(name, ravasz, girvan_newman)

        print("\nRavasz:")
        print_graph_information(name, ravasz[0])
        print_graph_information(name, ravasz[1])
        
        print("\nGirvan-Newman")
        print_graph_information(name, girvan_newman[0])
        print_graph_information(name, girvan_newman[1])

execute_algorithms_on_files()