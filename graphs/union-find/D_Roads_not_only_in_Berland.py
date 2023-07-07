#!/usr/bin/python3
"""CodeForces Problem --> D. Roads not only in Berland"""
from collections import Counter
from typing import List, Optional


class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find_set(self, a: int) -> int:
        if a == self.parent[a]:
            return a

        p = self.find_set(self.parent[a])
        self.parent[a] = p
        return p

    def union_sets(self, a: int, b: int) -> None:
        a_parent = self.find_set(a)
        b_parent = self.find_set(b)

        if a_parent == b_parent:
            return

        greater = a_parent if self.size[a_parent] >= self.size[b_parent] else b_parent
        smaller = b_parent if greater == a_parent else a_parent

        self.parent[smaller] = greater
        self.size[greater] += self.size[smaller]

    def connected(self, a: int, b: int) -> bool:
        return self.find_set(a) == self.find_set(b)


def solution():
    n = int(input())
    uF = DSU(n)

    count, already_connected = 0, []
    for _ in range(n - 1):
        a, b = map(int, input().split())

        if uF.connected(a - 1, b - 1):
            already_connected.append([a - 1, b - 1])
            count += 1
        uF.union_sets(a - 1, b - 1)

    result = []
    for pair in already_connected:
        first = pair[0]
        for i in range(n):
            if not uF.connected(first, i):
                result.append([first, i])
                uF.union_sets(first, i)

    print(count)
    for i in range(len(result)):
        print(' '.join(str(val + 1) for val in already_connected[i]), ' '.join(str(val + 1) for val in result[i]))


if __name__ == '__main__':
    solution()
