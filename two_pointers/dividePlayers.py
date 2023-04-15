#!/usr/bin/python3
"""LeetCode Problem #2491 --> Divide Players Into Teams of Equal Skill"""


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        groups = []

        i, j = 0, len(skill) - 1
        while i <= j:
            groups.append([skill[i], skill[j]])
            i += 1
            j -= 1

        skill_of_groups = groups[0][0] + groups[0][1]
        for a, b in groups[1:]:
            if a + b != skill_of_groups:
                return -1

        chemistry = 0
        for a, b in groups:
            chemistry += a * b
        return chemistry
