"""Leetcode Problem #155 --> Min Stack"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            _, currMin = self.stack[-1]

            if val > currMin:
                self.stack.append((val, currMin))
            else:
                self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        top, _ = self.stack[-1]
        return top

    def getMin(self) -> int:
        _, currMin = self.stack[-1]
        return currMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
