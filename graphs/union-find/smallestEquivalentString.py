#!/usr/bin/python3
"""LeetCode Problem #1061 --> Lexographically Smallest Equivalent String"""
import string
from typing import List


class DisJointSet:
    def __init__(self):
        self.rep = {char: char for char in string.ascii_lowercase}

    def representative(self, x: int) -> int:
        parent = x
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev = self.rep[x]
            self.rep[x] = parent
            x = prev
        return parent

    def union(self, x: int, y: int) -> None:
        xrep = self.representative(x)
        yrep = self.representative(y)

        if xrep > yrep:
            self.rep[xrep] = yrep
        else:
            self.rep[yrep] = xrep


    def connected(self, x: int, y: int) -> bool:
        return self.representative(x) == self.representative(y)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dis = DisJointSet()

        for i in range( len(s1) ):
            dis.union(s1[i], s2[i])

        answer = ""
        for b in baseStr:
            answer += dis.representative(b)
        return answer
