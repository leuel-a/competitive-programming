#!/usr/bin/python3
"""LeetCode Problem #690 --> Employee Importance"""
from collections import defaultdict


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list['Employee'], emp_id: int) -> int:
        visited = set()
        graph = defaultdict(list)

        for employee in employees:
            graph[employee.id] = [employee.importance, employee.subordinates]

        total_importance = graph[emp_id][0]
        def depth_first_search(emp_id: int) -> None:
            nonlocal total_importance
            if emp_id in visited:
                return

            visited.add(emp_id)
            for subordinate in graph[emp_id][1]:
                total_importance += graph[subordinate][0]
                depth_first_search(subordinate)
        depth_first_search(emp_id)
        return total_importance
