#!/usr/bin/python3
"""LeetCode Problem #876 --> Middle Node"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast is not None:
            fast = fast.next

            if fast is not None:
                slow = slow.next
                fast = fast.next
        return slow
