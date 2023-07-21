#!/usr/bin/python3
"""LeetCode Problem #21 --> Merge Two Sorted Lists"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head, tail = None, None

        while list1 and list2:
            if list1.val >= list2.val:
                if head is None:
                    head = ListNode(list2.val)
                    tail = head
                else:
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                    print('here')
                list2 = list2.next
            else:
                if head is None:
                    head = ListNode(list1.val)
                    tail = head
                else:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                list1 = list1.next

        while list1:
            if head is None:
                head = ListNode(list1.val)
                tail = head
            else:
                tail.next = ListNode(list1.val)
                tail = tail.next
            list1 = list1.next

        while list2:
            if head is None:
                head = ListNode(list2.val)
                tail = head
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
            list2 = list2.next
        return head
