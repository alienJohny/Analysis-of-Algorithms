import csv
import random
from itertools import groupby
import collections
import numpy as np
from tools import getu
import time
import string
from matplotlib import pyplot as plt

d = {}
names_all = []

def find(item, d):
    found_item = None
    for k in d:
        if k == item:
            found_item = d[item]
    return found_item

with open('names.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if row[0] != "first_name" and i % 2 == 0:
            names_all.append(row[0])
        i += 1


for i in range(10000):
    fc = "".join(random.choices(list(string.ascii_uppercase), k=1))
    scs = "".join(random.choices(list(string.ascii_lowercase), k=8))
    names_all.append(fc + scs)

names = getu(names_all)
values = ['data' for i in range(len(names))]
names = sorted(names, reverse=True, key=lambda x: len(x))
biggest_word = names[0]

f_level = [name[:1] for name in names]
f_level_freq = collections.Counter(f_level)
for k in f_level_freq:
    f_level_freq[k] = [f_level_freq[k], []]

for name in names:
    f_level_freq[name[:1]][1].append(name[1:2])

for k in f_level_freq:
    f_level_freq[k][1] = collections.Counter(f_level_freq[k][1])
    print(f_level_freq[k][1])

f_level_freq = {k: v for k, v in sorted(f_level_freq.items(), key=lambda item: item[1][0], reverse=True)}

# Now all the levels has been sorted

for i in range(len(names)):
    if names[i][2:] == '':
        f_level_freq[names[i][:1]][1][names[i][1:2]] = [f_level_freq[names[i][:1]][1][names[i][1:2]], values[i]]
    else:
        if type(f_level_freq[names[i][:1]][1][names[i][1:2]]) == int:
            f_level_freq[names[i][:1]][1][names[i][1:2]] = (f_level_freq[names[i][:1]][1][names[i][1:2]], {})
        f_level_freq[names[i][:1]][1][names[i][1:2]][1][names[i][2:]] = names[i]

def search(d, item):
    if item[:1] not in d:
        return None
    else:
        if item[1:2] not in d[item[:1]][1]:
            return None
        else: # Found first two chars
            if item[2:] not in d[item[:1]][1][item[1:2]][1]:
                return None
            else:
                return d[item[:1]][1][item[1:2]][1][item[2:]]


d_t = {name : name for name in names}
test = names[:len(names) // 2]
t = {}

opt = []
naive = []
x = []
i = 0

for name in test:
    t[name] = {}
    x.append(i)

    start = time.time()
    search(f_level_freq, name)
    t[name]['opt'] = time.time() - start
    opt.append(t[name]['opt'])

    start = time.time()
    find(name, d_t)
    t[name]['naive'] = time.time() - start
    naive.append(t[name]['naive'])

    i += 1


error = 0
for k in t:
    error += abs(t[k]['naive'] - t[k]['opt'])
error = error / len(t.keys())
print(error)

plt.grid(True)
plt.plot(x, opt, "ro")
plt.xlabel('Случайное слово')
plt.ylabel('Время поиска, сек.')
plt.legend(['Оптимизированный метод'])
plt.show()

plt.grid(True)
plt.plot(x, naive, "go")
plt.xlabel('Случайное слово')
plt.ylabel('Время поиска, сек.')
plt.legend(['Стандартный поиск полным перебором'])
plt.show()
