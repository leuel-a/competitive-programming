#!/usr/bin/python3
"""LeetCode Problem #2115 --> Find All Possible Recipes from Given Supplies"""


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        recipes_made = []

        for idx, val in enumerate(ingredients):
            for ingredient in val:
                graph[ingredient].append(recipes[idx])
            indegree[recipes[idx]] += len(val)


        recipes = set(recipes)
        queue = deque(supplies)
        while queue:
            val = queue.popleft()
            if val in recipes:
                recipes_made.append(val)
            
            for neighbour in graph[val]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return recipes_made
