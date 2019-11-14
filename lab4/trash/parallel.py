import threading
from math import ceil

def parallel(a, b, func, num):
    n = len(a)

    k = n / num
    tmp = k
    pr_tmp = 0
    threads = []

    for i in range(num - 1):
        threads.append(threading.Thread(target=func, args=(a, b)))
        tmp += k
        pr_tmp += k
        
    threads.append(threading.Thread(target=func, args=(a, b)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    return c
