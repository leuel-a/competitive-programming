#!/usr/bin/python3
"""Eolymp Problem --> Operations On Graph"""
from collections import defaultdict


n = int(input())
adjacency_list = defaultdict(list)

k = int(input())
for _ in range(k):
    operation = list(map(int, input().split()))

    if operation[0] == 1:
        adjacency_list[operation[1]].append(operation[2])
        adjacency_list[operation[2]].append(operation[1])
    elif operation[0] == 2:
        if len(adjacency_list[operation[1]]) != 0:
            print(' '.join(str(val) for val in adjacency_list[operation[1]]))
