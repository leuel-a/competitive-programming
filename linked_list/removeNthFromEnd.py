#!/usr/bin/python3
"""LeetCode Problem #19 --> Remove Nth Node From End of List"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, prev = head, None
        sizeOfList, nth, i = 0, 0, 0

        # Calculate the size of the linked list
        while curr is not None:
            curr = curr.next
            sizeOfList += 1

        # Calculate the position of the node to remove from the beginning
        nth = sizeOfList - n + 1

        curr = head
        # Traverse to the node before the node to be removed
        while curr is not None and i != nth - 1:
            prev = curr
            curr = curr.next
            i += 1

        # Remove the node from the linked list
        if prev is None:
            head = curr.next
        else:
            if curr.next:
                prev.next = curr.next
            else:
                prev.next = None

        return head
