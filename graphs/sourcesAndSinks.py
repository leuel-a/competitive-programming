#!/usr/bin/python3
"""Eolymp Problem --> Sources and Sinks"""
from collections import defaultdict


n = int(input())
graph = defaultdict(list)

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        graph[i].append((j, row[j]))

aux = []
for i in range(n):
    aux.append([0, 0])

for key, val in graph.items():
    for idx, elem in enumerate(val):
        if elem[1] != 0:
            aux[key][0] += 1
            aux[idx][1] += 1

sources, sinks = [], []
for idx, elem in enumerate(aux):
    if elem[0] == 0:
        sinks.append(idx + 1)

    if elem[1] == 0:
        sources.append(idx + 1)

print(len(sources), ' '.join(str(source) for source in sources))
print(len(sinks), ' '.join(str(sink) for sink in sinks))

