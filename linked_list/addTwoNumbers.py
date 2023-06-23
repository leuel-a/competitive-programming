#!/usr/bin/python3
"""LeetCode Problem #2 --> Add Two Numbers"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        last = None

        carry = 0
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry

            new_node = ListNode(curr_sum % 10)

            if head == None:
                head = new_node
                last = new_node
            else:
                last.next = new_node
                last = new_node

            carry = curr_sum // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_sum = carry + l1.val

            new_node = ListNode(curr_sum % 10)

            if head == None:
                head = new_node
                last = new_node
            else:
                last.next = new_node
                last = new_node
            carry = curr_sum // 10
            l1 = l1.next

        while l2:
            curr_sum = carry + l2.val

            new_node = ListNode(curr_sum % 10)

            if head == None:
                head = new_node
                last = new_node
            else:
                last.next = new_node
                last = new_node
            carry = curr_sum // 10
            l2 = l2.next

        if carry != 0:
            new_node = ListNode(carry)
            last.next = new_node
            last = new_node
        return head
