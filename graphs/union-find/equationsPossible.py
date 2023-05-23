#!/usr/python3
"""LeetCode Problem #990 --> Satisfiability of Equality Equations"""
from typing import List


class DisJointSet:
    def __init__(self):
        self.rep = {char: char for char in string.ascii_lowercase}
        self.size = {char: 1 for char in string.ascii_lowercase}

    def representative(self, node: str) -> int:
        parent = node
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != parent:
            prev = self.rep[node]
            self.rep[node] = parent
            node = prev
        return parent

    def union(self, a: str, b: str) -> None:
        arep = self.representative(a)
        brep = self.representative(b)

        if arep == brep:
            return

        greater = arep if self.size[arep] >= self.size[brep] else brep
        smaller = brep if greater == arep else arep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]

    def connected(self, a: str, b: str) -> bool:
        return self.representative(a) == self.representative(b)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uF = DisJointSet()

        for equation in equations:
            val = list(equation)
            if val[1] + val[2] == '==':
                uF.union(val[0], val[3])

        for equation in equations:
            val = list(equation)
            if val[1] + val[2] == '!=':
                if uF.connected(val[0], val[3]):
                    return False
        return True
