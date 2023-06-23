#!/usr/bin/python3
"""LeetCode Problem #2130 --> Maximum Twin Sum of a Linked List"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n, aux = 0, head

        while aux:
            n += 1
            aux = aux.next

        i, max_twin = 0, 0
        aux, dict_s = head, {}
        while aux:
            if i >= n // 2:
                twin = n - 1 - i
                max_twin = max(max_twin, dict_s[twin] + aux.val)
            dict_s[i] = aux.val
            i += 1
            aux = aux.next
        return max_twin
