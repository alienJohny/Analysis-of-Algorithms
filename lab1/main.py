import numpy as np
import pandas as pd
import time
import sys
from matplotlib import pyplot as plt
from memory_profiler import profile

def levenshtein_matrix(s1, s2, return_matrix=False):
    matrix = alloc_matrix(s1, s2)

    # 1. Simple cases
    for i in range(1, len(s1) + 1): # Fill the first colums
        matrix[i][0] = i
    for i in range(1, len(s2) + 1): # Fill the first row
        matrix[0][i] = i

    # 2. i > 0, j > 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            x = matrix[i - 1][j - 1]
            y = matrix[i - 1][j]
            z = matrix[i][j - 1]
            matrix[i][j] = min(y + 1, z + 1, x + (0 if s1[i - 1] == s2[j - 1] else 1))

    distance = matrix[matrix.shape[0] - 1][matrix.shape[1] - 1]
    
    if return_matrix:
        return matrix, distance
    else:
        return distance

def levenshtein_rec(s1, s2):
    i, j = len(s1), len(s2)

    if i == 0:
        return j
    if j == 0:
        return i
    if i == 0 and j == 0:
        return 0
    return min(levenshtein_rec(s1[0:i], s2[0:j - 1]) + 1,
               levenshtein_rec(s1[0:i - 1], s2[0:j]) + 1,
               levenshtein_rec(s1[0:i - 1], s2[0:j - 1]) + (0 if s1[i - 1] == s2[j - 1] else 1))

def domerau_levenshtein_matrix(s1, s2, return_matrix=False):
    matrix = alloc_matrix(s1, s2)

    # 1. Simple cases
    for i in range(1, len(s1) + 1): # Fill the first colums
        matrix[i][0] = i
    for i in range(1, len(s2) + 1): # Fill the first row
        matrix[0][i] = i

    # 2. i > 0, j > 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            x = matrix[i - 1][j - 1]
            y = matrix[i - 1][j]
            z = matrix[i][j - 1]

            # Domerau method
            if i >= 2 and j >= 2:
                match = matrix[i - 2][j - 2] + \
                        (1 if ((s1[i - 1] == s2[j - 2]) and (s2[j - 1] == s1[i - 2])) else 0)
                matrix[i][j] = min(match, y + 1, z + 1, x + (0 if s1[i - 1] == s2[j - 1] else 1))
            else:
                matrix[i][j] = min(y + 1, z + 1, x + (0 if s1[i - 1] == s2[j - 1] else 1))

    distance = matrix[matrix.shape[0] - 1][matrix.shape[1] - 1]

    if return_matrix:
        return matrix, distance
    else:
        return distance

def domerau_levenshtein_rec(s1, s2):
    i, j = len(s1), len(s2)

    if i == 0:
        return j
    if j == 0:
        return i
    if i == 0 and j == 0:
        return 0
    return min(levenshtein_rec(s1[0:i], s2[0:j - 1]) + 1,
               levenshtein_rec(s1[0:i - 1], s2[0:j]) + 1,
               levenshtein_rec(s1[0:i - 1], s2[0:j - 1]) + (0 if s1[i - 2] == s2[j - 2] else 1),
               levenshtein_rec(s1[0:i - 2], s2[0:j - 2]) + 1,
               0 if ((s1[i - 2] == s2[j - 1]) and (s1[i - 1] == s2[j - 2])) else 1)

def alloc_matrix(s1, s2):
    matrix_shape = (len(s1) + 1, len(s2) + 1)
    return np.zeros(matrix_shape)

def print_result(title, s1, s2, distance, matrix=None):
    print("Distance between \"{0}\" and \"{1}\" according to {2} is {3}".format(s1, s2, title, int(distance)))
    if matrix is not None:
        df = pd.DataFrame(matrix, columns=list(" " + s2))
        df.index = list(" " + s1)
        print(df)
    print()

def measure_time():
    pass

def test_method(method, s1, s2, ntimes=20):
    running_time = 0
    distance = None
    for _ in range(ntimes):
        start_time = time.time()
        distance = method(s1, s2)
        running_time += (time.time() - start_time)

    average_running_time = running_time / ntimes

    return (method.__name__, s1, s2, distance, average_running_time)

def test_all():
    methods = [levenshtein_rec, levenshtein_matrix, domerau_levenshtein_rec, domerau_levenshtein_matrix]
    tests = [["кот", "окт"],
             ["опток", "поток"],
             ["одеть", "надеть"],
             ["gugl", "google"],
             ["gugol", "google"]]

    for word_pair in tests:
        print("\n{0}s1: {1}, s2: {2}{3}".format("\033[1m", word_pair[0], word_pair[1], "\033[0m"))
        for method in methods:
            test_report = test_method(method, word_pair[0], word_pair[1])
            print("Method: {0:26} Distance: {1:<3d} Average running time: {2:3.12f}".format(test_report[0],
                                                                                            int(test_report[3]),
                                                                                            test_report[4]))

def main():
    # Test
    s1, s2 = "скат", "кот"
    
    lm, lm_d = levenshtein_matrix(s1, s2, return_matrix=True)
    print_result("Levenshtein Matrix", s1, s2, lm_d, matrix=lm)

    dlm, dlm_d = domerau_levenshtein_matrix(s1, s2, return_matrix=True)
    print_result("Domerau-Levenshtein Matrix", s1, s2, dlm_d, matrix=dlm)

    lrd = levenshtein_rec(s1, s2) # Levenstein recursion distance
    print_result("Levenstain Recursive Method", s1, s2, lrd)

    dlrd = domerau_levenshtein_rec(s1, s2)
    print_result("Domerau-Levenstain Recursive Method", s1, s2, dlrd)

if __name__ == "__main__":
    main()
    test_all()




