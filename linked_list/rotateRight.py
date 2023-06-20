#!/usr/bin/python3
"""LeetCode Problem #61 --> Rotate List"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, aux = 0, head
        while aux:
            count += 1
            aux = aux.next

        if count == 0 or count == 1:
            return head

        k %= count
        if k == 0:
            return head
        prev, aux = None, head
        while aux and count > k:
            prev = aux
            aux = aux.next
            count -= 1

        while aux.next:
            aux = aux.next

        aux.next = head
        head = prev.next
        prev.next = None
        return head
