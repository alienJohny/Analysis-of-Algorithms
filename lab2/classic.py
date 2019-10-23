import numpy as np

def classic_matrix_mult(A, B):

    A, B = np.array(A), np.array(B)
    
    if len(B) != len(A[0]):
        print("Error! Different dimension!")
        return None

    n = len(A)
    m = len(A[0])
    t = len(B[0])

    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(n):
        for j in range(m):
            for k in range(t):
                C[i][k] += A[i][j] * B[j][k]
    return C

