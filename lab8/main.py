import csv
import random
from itertools import groupby
import collections


class EffectiveDict:
    def __init__(self, data):
        self.data = data

    def find(self, item):
        pass
    

names = []

with open('names.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if row[0] != "first_name" and i % 2 == 0:
            names.append(row[0])
        i += 1

names_sorted = sorted(names, reverse=True, key=lambda x: len(x))
biggest_word = names_sorted[0]

# [(key, len(list(group))) for key, group in groupby(a)]


for i in range(len(biggest_word)):

    cs = []
    for j in range(len(names)):
        cs.append(names[j][i:i + 1])

    counter = collections.Counter(cs)
    print(counter)



