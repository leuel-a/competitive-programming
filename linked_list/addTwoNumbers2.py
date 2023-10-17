"""Leetcode Problem #445 --> Add Two Numbers II"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum = []
        secondNum = []

        aux = l1
        while aux:
            firstNum.append(aux.val)
            aux = aux.next

        aux = l2
        while aux:
            secondNum.append(aux.val)
            aux = aux.next
        firstNum.reverse()
        secondNum.reverse()

        result = []
        i = j = 0
        carry = 0
        while i < len(firstNum) and j < len(secondNum):
            a = firstNum[i]
            b = secondNum[j]

            curr_val = a + b + carry
            value = curr_val % 10
            carry = curr_val // 10
            result.append(value)

            i += 1
            j += 1

        while i < len(firstNum):
            a = firstNum[i]
            curr_val = a + carry

            value = curr_val % 10
            carry = curr_val // 10
            result.append(value)
            i += 1

        while j < len(secondNum):
            a = secondNum[j]
            curr_val = a + carry

            value = curr_val % 10
            carry = curr_val // 10
            result.append(value)
            j += 1

        if carry > 0:
            result.append(carry)

        head = None
        aux = head
        result = result[::-1]
        for num in result:
            newNode = ListNode(num)
            if head is None:
                head = newNode
                head.next = None
                aux = head
            else:
                newNode = newNode
                aux.next = newNode
                aux = newNode
                aux.next = None
        return head
