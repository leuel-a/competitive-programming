#!/usr/bin/python3
"""Eolmpy Problem --> Cities and Roads"""
from collections import defaultdict


n = int(input())

count = 0
for i in range(n):
    row = list(map(int, input().split()))
    for val in row:
        if val == 1:
            count += 1
print(count // 2)
