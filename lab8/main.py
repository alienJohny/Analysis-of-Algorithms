import csv
import random
from itertools import groupby
import collections
import numpy as np
from tools import getu


class EffectiveDict:
    def __init__(self, data):
        self.data = data

    def find(self, item):
        pass

d = {}
names_all = []

with open('names.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if row[0] != "first_name" and i % 2 == 0:
            names_all.append(row[0])
        i += 1

names = getu(names_all)
values = ['data' for i in range(len(names))]
names = sorted(names, reverse=True, key=lambda x: len(x))
biggest_word = names[0]

f_level = [name[:1] for name in names]
f_level_freq = collections.Counter(f_level)
for k in f_level_freq:
    f_level_freq[k] = [f_level_freq[k], []]

for name in names:
    # if {name[1:2] : []} not in f_level_freq[name[:1]][1]:
    f_level_freq[name[:1]][1].append(name[1:2]) # ({name[1:2] : []})

for k in f_level_freq:
    f_level_freq[k][1] = collections.Counter(f_level_freq[k][1])

f_level_freq = {k: v for k, v in sorted(f_level_freq.items(), key=lambda item: item[1][0], reverse=True)}

# Now all the levels has been sorted

for i in range(len(names)):
    if names[i][2:] == '':
        f_level_freq[names[i][:1]][1][names[i][1:2]] = [f_level_freq[names[i][:1]][1][names[i][1:2]], values[i]]
    else:
        if type(f_level_freq[names[i][:1]][1][names[i][1:2]]) == int:
            f_level_freq[names[i][:1]][1][names[i][1:2]] = (f_level_freq[names[i][:1]][1][names[i][1:2]], [])        
        f_level_freq[names[i][:1]][1][names[i][1:2]][1].append({names[i][2:] : values[i]})
