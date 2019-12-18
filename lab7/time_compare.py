from matplotlib import pyplot as plt
import bm as bm_search
import kmp as kmp_search
import random
random.seed(0)  # For repeatability
import string
import time


alphabet = list(string.ascii_lowercase)
bm_meas = []
kmp_meas = []
k = 1000
x = [i for i in range(10 * k, 1 * k * k + 1, 10 * k)]
needle_len = k

for hs_len in x:
    haystack = random.choices(alphabet, k=hs_len)
    entry_index = hs_len // 2
    needle = haystack[entry_index:entry_index + needle_len]

    # Measure KMP
    start = time.time()
    kmp_search.kmp(needle, haystack)
    kmp_meas.append(time.time() - start)

    # Measure BM
    start = time.time()
    bm_search.search(haystack, needle)
    bm_meas.append(time.time() - start)

plt.grid(True)
plt.ylabel("Время, сек.")
plt.xlabel("Длина текста для поиска паттерна")
plt.plot(x, kmp_meas, "o--")
plt.plot(x, bm_meas, "o--")
plt.legend(["Алгоритм Кнута-Морриса-Пратта", "Алгоритм Бойера-Мура"])
plt.show()