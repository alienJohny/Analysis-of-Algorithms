from classic import classic_matrix_mult
from winograd import classic_winograd, optimized_winograd
from matplotlib import pyplot as plt
import time, sys # Internal libraries
import numpy as np


def generate_matrixes(down_size, up_size, step):
    matrixes = []
    for i in range(down_size, up_size + step, step):
        matrixes.append(np.random.randint(-150, 150, size=(i, i)))

    return np.array(matrixes)


def measure_time(times, f, *args):
    """
    Sum of the kernel and user-space CPU time will be measured
    Returned number is average running time in seconds
    """

    time_start = time.process_time()
    for i in range(times):
        f(*args)
    time_end = time.process_time() - time_start
    avg_time = time_end / times

    return avg_time


def plot_results(x, title, xlabel, ylabel, legend, *args):
    print(args)
    
    plt.title(title)
    plt.grid(True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for arg in args:
        print(args)
        plt.plot(x, arg, "o--")

    plt.legend(legend)
    plt.show()


def test():
    plot_results([1, 2, 3, 4], "", "", "", 


def main():
    pass


if __name__ == "__main__":
    main()
