#!/usr/bin/python3
"""Eolymp Problem --> Bicoloring"""
from collections import defaultdict, deque


def checkIfBicolorable() -> None:
    graph = defaultdict(list)
    while True:
        nodes = int(input())
        if nodes == 0:
            break

        graph.clear()
        num_of_edges = int(input())
        for i in range(num_of_edges):
            i, j = map(int, input().split())
            graph[i].append(j)
            graph[j].append(i)

        stack = [1]
        color =[-1 for i in range(nodes)]

        color[0], bicolorable = 0, True
        while stack and bicolorable:
            node = stack.pop()

            for val in graph[node]:
                if color[val - 1] == -1:
                    color[val - 1] = 1 - color[node - 1]
                    stack.append(val)
                elif color[val - 1] == color[node - 1]:
                    bicolorable = False

        print("BICOLOURABLE." if bicolorable else "NOT BICOLOURABLE.")

if __name__ == '__main__':
    checkIfBicolorable()
