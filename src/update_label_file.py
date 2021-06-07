import numpy as np

def update_label_file(filePath):
    L = np.loadtxt(f"{filePath}.txt", dtype=int, delimiter=" ")
    L = np.array(list(map(lambda x: x[1], sorted(L, key=lambda x: x[0]))))
    label_count = len(np.unique(L))

    np.savetxt(f"{filePath}_sorted.txt", L, fmt='%i', delimiter=" ", header=f"{label_count}")

update_label_file("./datasets/email-Eu-core/email-Eu-core_Communities_all")