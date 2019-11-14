from classic import classic_matrix_mult
from winograd import classic_winograd, optimized_winograd
from matplotlib import pyplot as plt
import time, sys # Internal libraries
import numpy as np
from parallel import parallel


def generate_test_data(down_size, up_size, step):
    axes = []
    matrixes = []
    for i in range(down_size, up_size + step, step):
        axes.append(i)
        matrixes.append(np.random.randint(-150, 150, size=(i, i)))

    return axes, np.array(matrixes)


def measure_time(times, f, *args):
    """
    Sum of the kernel and user-space CPU time will be measured
    Returned number is average running time in seconds
    """

    print("Testing function: " + f.__name__, end="")

    time_start = time.process_time()
    for i in range(times):
        f(*args)
    print(" --- DONE")
    time_end = time.process_time() - time_start
    avg_time = time_end / times

    return avg_time


def plot_results(title, xlabel, ylabel, legend, x, *args):
    plt.title(title)
    plt.grid(True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for arg in args[0]:
        plt.plot(x, arg, "o--")

    plt.legend(legend)
    plt.show()


def test(down_size, up_size, step):
    # Test data generating
    axes, test_matrixes = generate_test_data(down_size, up_size, step)

    # Functions which are need to be tested
    f_to_test = [
        # classic_matrix_mult,
        # classic_winograd,
        optimized_winograd
    ]
    measured_time = {}

    for f in f_to_test:
        measured_time[f.__name__] = []
        for matrix in test_matrixes:
            measured_time[f.__name__].append(measure_time(1, f, matrix, matrix))

    plot_results(
        "Matrix multiplication algorithms comparison",
        "Matrix size NxN",
        "Seconds",
        [f.__name__ for f in f_to_test],
        axes,
        [measured_time[f.__name__] for f in f_to_test]
    )


def main():
    test(down_size=5, up_size=30, step=10)
    


if __name__ == "__main__":
    main()
