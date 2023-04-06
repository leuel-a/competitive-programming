#!/usr/bin/python3
"""Eolmpy Problem --> From adjacency matrix to adjacency list"""
from collections import defaultdict


n = int(input())
graph = defaultdict(list)


for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        graph[i].append((j, row[j]))

adjacency_list = defaultdict(list)
for idx, elem in graph.items():
    for val in graph[idx]:
        if val[1] != 0:
            adjacency_list[idx].append(val[0] + 1)

for val in adjacency_list.values():
    print(len(val), ' '.join(str(i) for i in val))
