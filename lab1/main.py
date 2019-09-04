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

    print_matrix("Levenshtein matrix", s1, s2, matrix)
    distance = matrix[matrix.shape[0] - 1][matrix.shape[1] - 1]

    return distance

def levenshtein_rec(word1, word2):
    pass

def domerau_levenshtein_matrix(word1, word2):
    pass

def domerau_levenshtein_rec(word1, word2):
    pass

def alloc_matrix(word1, word2):
    matrix_shape = (len(word1) + 1, len(word2) + 1)
    return np.zeros(matrix_shape)

def print_matrix(title, word1, word2, matrix):
    print(title)
    print(matrix)

def test():
    pass

def test_all():
    pass

def main():
    levenshtein_matrix("скат", "кот")

if __name__ == "__main__":
    main()
