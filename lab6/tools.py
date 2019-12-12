import numpy as np
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random
random.seed(0) # For repeatability
from tools import *

MAX_DIS = 10  # maximum distance
MIN_DIS = 1  # minimum distance

def print_matrix(am, M, msg):
    print(msg)

    labels = [str(i) for i in range(1, M + 1)]
    df = pd.DataFrame(am, columns=labels)
    df.index = labels
    print(df, end='\n\n')

def plot_graph(am, dis_m):
    g = nx.DiGraph()

    print_matrix(dis_m, len(dis_m), 'Distance Matrix')

    for i in range(len(am)):
        for j in range(i + 1, len(am[0])):
            if am[i][j] == 1:
                g.add_edge(i + 1, j + 1, weight=dis_m[i][j])

    pos = nx.circular_layout(g)
    edge_labels = {(u, v): d['weight'] for u, v, d in g.edges(data=True)}

    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    plt.show()

def P(i, j, nu, beta, tau, alpha, k):
    pass

def get_adjacency_matrix(n):
    matrix = np.array([[1 for i in range(n)] for j in range(n)])

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    return matrix

def fill_dis_matr(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            t = random.randint(MIN_DIS, MAX_DIS)
            m[i][j], m[j][i] = t, t

    m[m == 0] = np.inf

    return m
