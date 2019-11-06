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
    
    C = np.zeros((M, Q)) # Результирующая матрица

    if N != len(A[0]):
        print("В матрицах А(m, n), B(q, r) n != q")
        return None

    # Оптимизация №1 - избавиться от деления в цикле
    d = N // 2

    MulH = np.zeros((M))
    MulV = np.zeros((Q))

    for i in range(M):
        for j in range(d):
            MulH[i] += A[i][2 * j] * A[i][2 * j + 1]

    for i in range(Q):
        for j in range(d):
            MulV[i] += B[2 * j][i] * B[2 * j + 1][i]

    # Оптимизация №2 накопление результата в буфер
    for i in range(M):
        for j in range(Q):
            buff = -(MulH[i] + MulV[j])
            for k in range(d):
                buff += ((A[i][2 * k + 1] + B[2 * k][j]) * (A[i][2 * k] + B[2 * k + 1][j]))
            # Сброс буфера в ячейку
            C[i][j] = buff
                
    if N % 2 != 0:
        for i in range(M):
            for j in range(Q):
                C[i][j] += A[i][N - 1] * B[N - 1][j]

    # Очистка временных массивов
    del MulH
    del MulV

    return C

a = [[1, 2], [3, 4]]

print(optimized_winograd(a, a))




"""
C[i][j] = sum((A[i][2 * k] + B[2 * k + 1][j]) * (A[i][2 * k + 1] + B[2 * k][j]) for k in range(d)) - MulH[i] - MulV[j]
"""















