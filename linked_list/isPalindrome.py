#!/usr/bin/python3
"""LeetCode Problem #234 --> Palindrom Linked List"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        aux = head
        stack = []

        while aux is not None:
            stack.append(aux.val)
            aux = aux.next

        while head is not None:
            if head.val != stack.pop():
                return False
            head = head.next
        return True
