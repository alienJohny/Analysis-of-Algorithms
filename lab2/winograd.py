import numpy as np

def classic_winograd(A, B):
    M = len(A)
    N = len(B)
    Q = len(B[0])
    
    C = np.zeros((M, Q)) # Will be result

    if N != len(A[0]):
        print("Different dimension of the matrics")
        return None

    MulB = np.zeros((M))
    MulV = np.zeros((Q))

    for i in range(M):
        for j in range(N // 2):
            MulB[i] += A[i][2 * j] * A[i][2 * j + 1]

    for i in range(Q):
        for j in range(N // 2):
            MulV[i] += B[2 * j][i] * B[2 * j + 1][i]

    for i in range(M):
        for j in range(Q):
            C[i][j] = - MulB[i] - MulV[j]
            for k in range(N // 2):
                C[i][j] += ((A[i][2 * k] + B[2 * k + 1][j]) * (A[i][2 * k + 1] + B[2 * k][j]))

    if N % 2 != 0:
        for i in range(M):
            for j in range(Q):
                C[i][j] += A[i][N - 1] * B[N - 1][j]

    return np.array(C)

def optimized_winograd(A, B):
    M = len(A)
    N = len(B)
    Q = len(B[0])
    
    C = np.zeros((M, Q)) # Will be result

    if N != len(A[0]):
        print("Different dimension of the matrics")
        return None

    d = N // 2

    MulB = np.zeros((M))
    MulV = np.zeros((Q))

    for i in range(M):
        MulB[i] = sum(A[i][2 * j] * A[i][2 * j + 1] for j in range(d))

    for i in range(Q):
        MulV[i] = sum(B[2 * j][i] * B[2 * j + 1][i] for j in range(d))

    for i in range(M):
        for j in range(Q):
            C[i][j] = sum((A[i][2 * k] + B[2 * k + 1][j]) * (A[i][2 * k + 1] + B[2 * k][j]) for k in range(d)) - MulB[i] - MulV[j]

    if N % 2 != 0:
        for i in range(M):
            C[i][j] = sum(A[i][N - 1] * B[N - 1][j] for j in range(Q))

    return C





















