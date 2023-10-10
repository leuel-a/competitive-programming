"""Leetcode Problem #399 --> Evaluate Division"""
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for (dividend, divisor), value in zip(equations, values):
            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            if value != 0:
                graph[divisor][dividend] = 1 / value

        for intermediate in graph:
            for start in graph:
                for end in graph:
                    if intermediate in graph[start] and end in graph[intermediate]:
                        if end not in graph[start]:
                            graph[start][end] = graph[start][intermediate] * \
                                graph[intermediate][end]

        result = []
        for dividend, divisor in queries:
            if dividend in graph and divisor in graph:
                if divisor in graph[dividend]:
                    result.append(graph[dividend][divisor])
                else:
                    result.append(-1.0)
            else:
                result.append(-1.0)
        return result
