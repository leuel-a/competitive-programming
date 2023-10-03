#!/usr/bin/env python3
from typing import List, Tuple
from collections import defaultdict


def main():
    n, m, q = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b, weight = map(int, input().split())

        graph[a - 1].append((b - 1, weight))
        graph[b - 1].append((a - 1, weight))

    queries = []
    for _ in range(q):
        a, b = map(int, input().split())
        queries.append((a - 1, b - 1))

    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for key, value in graph.items():
        a = key
        for b, w in value:
            dist[a][b] = w
            dist[b][a] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for a, b in queries:
        print(dist[a][b] if dist[a][b] != float('inf') else -1)


if __name__ == '__main__':
    main()
