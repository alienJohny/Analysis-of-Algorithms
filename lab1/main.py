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
    pass

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
    pass

def alloc_matrix(s1, s2):
    matrix_shape = (len(s1) + 1, len(s2) + 1)
    return np.zeros(matrix_shape)

def print_matrix(title, s1, s2, matrix, distance):
    print(title)
    print(matrix)
    print(distance, end="\n\n")

def test():
    pass

def test_all():
    pass

def main():
    s1, s2 = "кот", "окт"
    
    lm, lm_d = levenshtein_matrix(s1, s2)
    print_matrix("Levenshtein matrix", s1, s2, lm, lm_d)

    dlm, dlm_d = domerau_levenshtein_matrix(s1, s2)
    print_matrix("Domerau-Levenshtein matrix", s1, s2, dlm, dlm_d)

if __name__ == "__main__":
    main()
