#!/usr/bin/python3
"""Geeks For Geeks Problem --> Detect cycle in an undirected graph"""
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		color = [0 for _ in range(V)]

		def depth_first_search(node: int, parent) -> bool:
		    color[node] = 1
		    for neighbour in adj[node]:
		        if neighbour == parent:
		            continue

		        if color[neighbour] == 1:
		            return True

		        if depth_first_search(neighbour, node):
    	                return True

		    color[node] = 2
		    return False

		for i in range(V):
		    if color[i] == 0:
		        if depth_first_search(i, None):
		            return True
		return False
