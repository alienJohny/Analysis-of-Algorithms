import numpy as np
import threading
import time

def classic_winograd(A, B):
    M = len(A)
    N = len(B)
    Q = len(B[0])
    
    C = np.zeros((M, Q)) # Will be result

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

    if N % 2:
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

# ===================================== Parallel Optimized Winograd ==================================

def parallel_thread_1(A, M, d, MulH):
    for i in range(M):
        for j in range(d):
            MulH[i] += A[i][2 * j] * A[i][2 * j + 1]

def parallel_thread_2(B, Q, d, MulV):
    for i in range(Q):
        for j in range(d):
            MulV[i] += B[2 * j][i] * B[2 * j + 1][i]

def optimized_winograd_parallel(A, B):
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

    # Данная оптимизация позволянт увеличить скорость алгоритма на 10%
    # Thread 1, fill MulH
    thread_1 = threading.Thread(target=parallel_thread_1, args=(A, M, d, MulH), daemon=True)
    # Thread 2, fill MulV
    thread_2 = threading.Thread(target=parallel_thread_2, args=(B, Q, d, MulV), daemon=True)
    # Starting
    thread_1.start()
    thread_2.start()

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

n = 2

k = 4
p = 0
m = np.random.randint(5, size=(100 * k + p, 100 * k + p))
start = time.time()
for i in range(n):
    _ = classic_winograd(m, m)
end = time.time() - start
print(end/n)
