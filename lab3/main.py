from bubble_sort import bubble_sort
from insert_sort import insert_sort
from quick_sort import quick_sort
from matplotlib import pyplot as plt
import time, sys
import numpy as np
import random


def generate_test_data(_type):
    axes = []
    arrays = []
    step = 100
    max_v = 30000
    for i in range(100, max_v + step, step):
        axes.append(i)
        if _type == "random" or _type == None:
            a = [i for i in range(i + 1)]
            random.shuffle(a)
            arrays.append(a)
        if _type == "up":
            arrays.append([i for i in range(i + 1)])
        if _type == "down":
            arrays.append([max_v - i for i in range(i + 1)])

    return axes, np.array(arrays)


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


def test():
    # Test data generating
    tests = {"random": {}, "up": {}, "down": {}}

    for k in tests:
        axes, data = generate_test_data(k)
        tests[k]["axes"] = axes
        tests[k]["data"] = data

    # Functions which are need to be tested
    f_to_test = [
        insert_sort,
        quick_sort
    ]
    
    measured_time = {}
    type_to_test = "up"

    for f in f_to_test:
        measured_time[f.__name__] = []
        for array in tests[type_to_test]["data"]:
            measured_time[f.__name__].append(measure_time(3, f, array))

    plot_results(
        "Sorting algorithms comparison on " + type_to_test + " data",
        "Array size",
        "Seconds",
        [f.__name__ for f in f_to_test],
        tests["random"]["axes"],
        [measured_time[f.__name__] for f in f_to_test]
    )


def main():
    test()


if __name__ == "__main__":
    main()
