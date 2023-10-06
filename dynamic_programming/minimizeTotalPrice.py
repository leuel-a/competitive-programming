"""Leetcode Problem #2646 --> Minimize the Total Price of the Trips"""
from typing import List
from collections import defaultdict

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # buiding the graph
        d = defaultdict(list)
        for src, des in edges:
            d[src].append(des)
            d[des].append(src)

        #counting the contribution of each node in the trips
        contribution = defaultdict(int)
        def count_cont(start, end, path):
            path.add(start)
            visited.add(start)
            if start == end:
                for node in path:
                    contribution[node] += 1
                return True
            for nei in d[start]:
                if nei not in visited and count_cont(nei, end, path):
                    return True
            path.remove(start)
            return False
        for start, end in trips:
            visited = set()
            count_cont(start, end, set())  

        @cache
        def dp(node, parent, halve):
            res1 = inf
            if not halve:
                res1 = price[node] // 2 * contribution[node]
                for nei in d[node]:
                    if nei != parent:
                        res1 += dp(nei, node, not halve)

            res2 = price[node] * contribution[node]
            for nei in d[node]:
                if nei != parent:
                    res2 += dp(nei, node, False)
            return min(res1, res2)
        return dp(0, -1, False)