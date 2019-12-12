from aco import AntColony
import random
from tools import *
import full_search
random.seed(0)  # For repeatability

M = 4  # number of cities
alpha = 1  # Pheromone factor
beta = 2  # Visibility factor
e = .5   # Evaporation rate
el = 2  # Amount of elite ants

# Matrices
am = get_adjacency_matrix(M)
dist_m = fill_dis_matr(M)  # Distances matrix
pheromones = np.ones((M, M))

print_matrix(am, M, "Adjacency Matrix")
print_matrix(pheromones, M, "Pheromones Matrix")
plot_graph(am, dist_m)

full_search_result = full_search.find_best_way(dist_m)

ac = AntColony(distances=dist_m, n_ants=M, n_best=2, n_iterations=100, decay=0.5, alpha=1, beta=1)
aco_result = ac.run()

def main():
    pass

if __name__ == '__main__':
    main()