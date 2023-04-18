#!/usr/bin/python3
""""""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        aux = head

        while aux:
            seek = aux.next
            while seek and seek.val == aux.val:
                seek = seek.next
            aux.next = seek
            aux = aux.next
        return head


