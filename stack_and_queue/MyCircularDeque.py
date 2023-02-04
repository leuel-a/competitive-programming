#!/usr/bin/python3
"""Design my own circular deque"""


class MyCircularDeque:
    """Defines a simple design of a Deque (Circular Queue)"""
    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.size = k
        self.queue = [None] * k

    def insertFront(self, value: int) -> bool:
        """Insert an element to the front of the deque"""
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front - 1
        self.queue[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """Insert an element to the last of the deque"""
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        self.queue[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """Delete an element from the front of the deque"""
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front = self.front + 1
        return True

    def deleteLast(self) -> bool:
        """Delete an element from the last of the deque"""
        if self.isEmpty():
            return False

        if self.rear == self.front:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1
        return True

    def getFront(self) -> int:
        """Returns the front of th deque"""
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        """Returns the rear of the deque"""
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """Checks if a deque is empty"""
        return self.front == -1

    def isFull(self) -> bool:
        """Checks if a deque is full"""
        return (self.front == 0 and self.rear == self.size - 1) or\
            self.front == self.rear + 1
