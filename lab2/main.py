from classic import classic_matrix_mult
from winograd import classic_winograd, optimized_winograd
from matplotlib import pyplot as plt
import time, sys # Internal libraries
import numpy

def measure_time(times, f, *args):
    """
    Sum of the kernel and user-space CPU time will be measured
    Returned number is average running time in seconds
    """

    time_start = time.process_time()
    for i in range(times):
        f(*args)
    time_end = time.process_time() - time_start)
    avg_time = time_end / times

    return avg_time

def plot_results():
    pass

def test():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
