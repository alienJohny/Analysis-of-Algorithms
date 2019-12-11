import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(0) # For repeatability
from tools import *

def main():
    M = 4 # number of cities
    am = random_adjacency_matrix(M)
    dis_m = fill_dis_matr(M)
    alpha = 0
    ro = 0
    t_max = 0

    print_matrix(am, M, 'am')
    plot_graph(am, dis_m)

if __name__ == "__main__":
    main()
