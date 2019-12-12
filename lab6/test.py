from aco import AntColony
from tools import *
from matplotlib import pyplot as plt
import full_search
import time
random.seed(0)  # For repeatability

max_cities = 10
cities_range = [i for i in range(1, max_cities + 1)]
aco_time_mes = []
full_search_time_mes = []

for cities in cities_range:
    print("Cities:", cities)

    am = get_adjacency_matrix(cities)
    dist_m = fill_dis_matr(cities)  # Generate distances matrix

    # Measure time for full search
    start = time.time()
    full_search_result = full_search.find_best_way(dist_m)
    print("Solved by full search")
    end = time.time()
    full_search_time_mes.append(end - start)

    # Measure time for full search
    start = time.time()
    ac = AntColony(distances=dist_m, n_ants=cities, n_best=2, n_iterations=100, decay=0.5, alpha=1, beta=1)
    aco_result = ac.run()
    print("Solved by ACO", end='\n\n')
    end = time.time()
    aco_time_mes.append(end - start)

plt.grid(True)
plt.xlabel("Количество городов")
plt.ylabel("Время, сек.")
plt.plot(cities_range, aco_time_mes, "o--")
plt.plot(cities_range, full_search_time_mes, "o--")
plt.legend(["Муравьиный алгоритм", "Полный перебор"])
plt.show()