#!/usr/bin/python3
"""LeetCode Problem #1019 --> Next Greater Node in a Linked List"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: 'ListNode') -> list[int]:
        stack, prev = [], None

        next_larger_nodes, idx = [], 0
        while head:
            next_larger_nodes.append(0)
            while stack and stack[-1][1] < head.val:
                next_larger_nodes[stack[-1][0]] = head.val
                stack.pop()
            stack.append((idx, head.val))
            head = head.next
            idx += 1
        return next_larger_nodes
