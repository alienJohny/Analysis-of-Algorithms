import itertools
import numpy as np

def gen_all_perm(n_nodes):
    perms = []
    tmp = [list(i) for i in itertools.permutations([i for i in range(1, n_nodes + 1)], n_nodes)]
    for l in tmp:
        if l[0] == 1:
            l.append(1)
            perms.append(l)
    return np.array(perms)

def get_way_len(dist_m, nodes):
    n_i = nodes[0] - 1
    n_j = nodes[1] - 1
    return dist_m[n_i][n_j]

def get_pher(pm, nodes):
    n_i = nodes[0] - 1
    n_j = nodes[1] - 1
    return pm[n_i][n_j]

def find_best_way(dist_m):
    n_nodes = len(dist_m)
    perms = gen_all_perm(n_nodes)

    comb = {}  # Storing all existed ways

    for i in range(len(perms)):
        current_comb_length = 0
        for j in range(len(perms[i]) - 1):
            current_comb_length += get_way_len(dist_m, [perms[i][j], perms[i][j + 1]])

        way = "-".join([str(c) for c in perms[i]])  # Just a string visualization like '1-2-4-3-1'
        comb[way] = current_comb_length

    best_way = [[k, v] for k, v in sorted(comb.items(), key=lambda item: item[1])][0]

    return best_way