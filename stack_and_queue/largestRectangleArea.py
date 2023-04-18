#!/usr/bin/python3
"""LeetCode #84 --> Largest Rectangle in Histogram"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        _max = 0
        heights.append(float('-inf'))

        for idx, elem in enumerate(heights):
            if len(stack) == 0 or elem >= heights[stack[-1][0]]:
                if idx == 0:
                    stack.append((idx, -1))
                else:
                    stack.append((idx, stack[-1][0]))
            else:
                while stack and heights[stack[-1][0]] > elem:
                    leftBound = stack[-1][1]
                    _max = max(_max, (idx - stack[-1][1] - 1) * heights[stack[-1][0]])
                    stack.pop()
                stack.append((idx, leftBound))

        return _max

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
