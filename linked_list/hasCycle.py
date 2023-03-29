#!/usr/bin/python3
"""LeetCode Problem #141 --> Linked List Cycle"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tortoise = haire = head

        while haire:
            haire = haire.next

            if haire:
                tortoise = tortoise.next
                haire = haire.next

            if haire is tortoise:
                return True
        return False
