#!/usr/bin/python3
"""LeetCode Problem #206 --> Reverse Linked List"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseHelper(prev, head):
            if not head:
                return prev

            next = head.next
            head.next = prev
            return reverseHelper(head, next)
        return reverseHelper(None, head)
