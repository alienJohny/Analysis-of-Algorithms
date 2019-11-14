import threading
import numpy as np
import time
from matplotlib import pyplot as plt

def classic_winograd_mult(A, B, C, k1, k2):
    M = len(A)
    N = len(B)
    Q = len(B[0])

    MulH = np.zeros(M)
    MulV = np.zeros(Q)

    for i in range(M):
        for j in range(N // 2):
            MulH[i] += A[i][2 * j] * A[i][2 * j + 1]

    for i in range(k1, k2):
        for j in range(N // 2):
            MulV[i] += B[2 * j][i] * B[2 * j + 1][i]

    for i in range(M):
        for j in range(k1, k2):
            C[i][j] = - MulH[i] - MulV[j]
            for k in range(N // 2):
                C[i][j] += (A[i][2 * k] + B[2 * k + 1][j]) * (A[i][2 * k + 1] + B[2 * k][j])

    if N % 2:
        for i in range(M):
            for j in range(k1, k2):
                C[i][j] = C[i][j] + A[i][N - 1] * B[N - 1][j]

def parallel(a, b, f, num):
    n = len(a)
    m = len(b[0])
    c = np.zeros((n, m))

    k = n / num
    tmp = k
    pr_tmp = 0
    threads = []

    for i in range(num):
        threads.append(threading.Thread(target=f, args=(a, b, c, int(pr_tmp), int(tmp))))
        tmp += k
        pr_tmp += k

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    return c

threads_n = [1, 2, 4, 8]
k = 5
p = 0
test_matrix = np.random.randint(5, size=(100 * k + p, 100 * k + p))
time_measurement = {}
rng = threads_n
for n_threads in rng:
    time_start = time.time()
    parallel(test_matrix, test_matrix, classic_winograd_mult, n_threads)
    end_time = time.time() - time_start
    time_measurement[n_threads] = end_time
[print(time_measurement[i]) for i in time_measurement]
x = rng
y = [time_measurement[i] for i in rng]

plt.title("Windograd algorithm performance depending on number of threads")
plt.grid(True)
plt.ylabel("Seconds")
plt.xlabel("Number of threads")
plt.bar(x, y, width=0.2)
plt.plot(x, y, 'ro--')
plt.show()




