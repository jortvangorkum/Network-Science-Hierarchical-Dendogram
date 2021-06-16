from src.algorithms.main import execute_algorithms

files = [
    ("PDZBase", "download.tsv.maayan-pdzbase/maayan-pdzbase/out.maayan-pdzbase", "\t"),
    ("David Copperfield", "download.tsv.adjnoun_adjacency/adjnoun_adjacency/out.adjnoun_adjacency_adjacency", " "),
    ("Dolphins", "download.tsv.dolphins/dolphins/out.dolphins", "\t"),
    ("Contiguous USA", "download.tsv.contiguous-usa/contiguous-usa/out.contiguous-usa", " "),
    ("American Football", "download.tsv.dimacs10-football/dimacs10-football/out.dimacs10-football", "\t")
]

def execute_algorithms_on_files():
    for (name, file_path, delimiter) in files:
        print(f"\n\n{name}\n")
        (ravasz, girvan_newman) = execute_algorithms(file_path, delimiter)


execute_algorithms_on_files()