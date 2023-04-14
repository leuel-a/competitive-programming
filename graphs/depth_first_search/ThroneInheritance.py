#!/usr/bin/python3
"""LeetCode Problem #1600 --> Throne Inheritance"""
from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.passed_away = defaultdict(bool)
        self.family_tree = defaultdict(list)


    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.passed_away[name] = True

    def getInheritanceOrder(self) -> list[str]:
        visited, orderOfSuccession = set(), []

        def successor(name: str) -> None:
            visited.add(name)
            if not self.passed_away[name]:
                orderOfSuccession.append(name)

            for child in self.family_tree[name]:
                if child not in visited:
                    successor(child)

        successor(self.king_name)
        return orderOfSuccession



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
