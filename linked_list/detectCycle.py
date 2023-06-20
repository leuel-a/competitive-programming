#!/usr/bin/python3
"""LeetCode Problem #142 --> Linked List Cycle II"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = haire = head

        while haire:
            haire = haire.next
            tortoise = tortoise.next

            if haire:
                haire = haire.next

            if haire == tortoise:
                break

        tortoise = head
        while haire:
            if tortoise == haire:
                return tortoise
            haire = haire.next
            tortoise = tortoise.next
        return None
