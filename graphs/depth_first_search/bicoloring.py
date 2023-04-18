#!/usr/bin/python3
""""""
from collections import defaultdict

while True:
    nodes = int(input())
    if nodes == 0:
        sys.exit()
    else:
        graph = defaultdict(list)

        n = int(input())
        for _ in range(n):
            i, j = map(int, input().split())
            graph[i].append(j)
            graph[j].append(i)

        color = [-1 for i in range(n)]
        def depth_first_search(node: int) -> bool:

            for neighbour in graph[node]:
                if color[neighbour - 1] == -1:
                    color[neighbour - 1] = 1 - color[node - 1]
                    return depth_first_search(neighbour)
                else:
                    if color[neighbour - 1] == color[node - 1]:
                        return False
            return True
        print(graph)

