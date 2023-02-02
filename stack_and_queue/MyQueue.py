#!/usr/bin/python3
"""Defines a queue"""


class MyQueue:
    """Defines a queue using stack"""

    def __init__(self):
        self.s_1 = []
        self.s_2 = []

    def push(self, x: int) -> None:
        """pushes an element to queue"""
        while self.s_1:
            self.s_2.append(self.s_1.pop())
        self.s_1.append(x)
        while self.s_2:
            self.s_1.append(self.s_2.pop())

    def pop(self) -> int:
        """removes an element on the front of the queue"""
        return self.s_1.pop()

    def peek(self) -> int:
        """returns the element on the front of the queue"""
        return self.s_1[-1]

    def empty(self) -> bool:
        """checks whether a queue is empty"""
        if len(self.s_1) > 0:
            return False
        return True
