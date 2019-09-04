import numpy as np
import pandas as pd

def levenshtein_matrix(s1, s2):
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
    
    return matrix, distance

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

def domerau_levenshtein_matrix(s1, s2):
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
    
    return matrix, distance

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
        print(matrix)
    print()

def measure_time():
    pass

def test():
    pass

def test_all():
    pass

def main():
    s1, s2 = "скат", "кот"
    
    lm, lm_d = levenshtein_matrix(s1, s2)
    print_result("Levenshtein Matrix", s1, s2, lm_d, matrix=lm)

    dlm, dlm_d = domerau_levenshtein_matrix(s1, s2)
    print_result("Domerau-Levenshtein Matrix", s1, s2, dlm_d, matrix=dlm)

    lrd = levenshtein_rec(s1, s2) # Levenstein recursion distance
    print_result("Levenstain Recursive Method", s1, s2, lrd)

    dlrd = domerau_levenshtein_rec(s1, s2)
    print_result("Domerau-Levenstain Recursive Method", s1, s2, dlrd)

if __name__ == "__main__":
    main()
