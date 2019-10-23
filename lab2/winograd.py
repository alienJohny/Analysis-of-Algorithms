import numpy as np

def classic_winograd(A, B):
    M = len(A)
    N = len(B)
    Q = len(B[0])
    
    C = np.zeros((M, Q)) # Will be result

    if N != len(A[0]):
        print("Different dimension of the matrics")
        return None

    MulH = np.zeros((M))
    MulV = np.zeros((Q))

    for i in range(M):
        for j in range(N // 2):
            MulH[i] += A[i][2 * j] * A[i][2 * j + 1]

    for i in range(Q):
        for j in range(N // 2):
            MulV[i] += B[2 * j][i] * B[2 * j + 1][i]

    for i in range(M):
        for j in range(Q):
            C[i][j] = - MulH[i] - MulV[j]
            for k in range(N // 2):
                C[i][j] += ((A[i][2 * k] + B[2 * k + 1][j]) * (A[i][2 * k + 1] + B[2 * k][j]))

    if N % 2:
        for i in range(M):
            for j in range(Q):
                C[i][j] += A[i][N - 1] * B[N - 1][j]

    return np.array(C)

def optimized_winograd():
    return 0

if __name__ == "__main__":
    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    print(classic_winograd(A, B))

    """
    [[ 30.  40.  50.  60.  70.]
     [ 40.  54.  68.  82.  96.]
     [ 50.  68.  86. 104. 122.]]
    """
