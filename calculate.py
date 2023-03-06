#!/usr/bin/python3

class Solution:
    def calculate(self, s: str) -> int:
        sum = []
        s = self.toPostfix(s.replace(' ', ''))
        for char in s:
            if char in ['*', '/', '+', '-']:
                firstOperand = int(sum.pop())
                secondOperand = int(sum.pop())
                if char == '*':
                    sum.append(firstOperand * secondOperand)
                elif char == '/':
                    sum.append(secondOperand // firstOperand)
                elif char == '+':
                    sum.append(secondOperand + firstOperand)
                elif char == '-':
                    sum.append(secondOperand - firstOperand)
                continue
            sum.append(int(char))

        return sum.pop()

    def toPostfix(self, s: str) -> str:
        stack, operand = [], ['+', '-', '*', '/']
        postfix = []
        prev = ""
        for char in s:
            if char in operand:
                postfix.append(prev)
                prev = ""
                if stack and self.has_higher_precedence(stack[-1]) >= \
                    self.has_higher_precedence(char):
                    while stack:
                        postfix.append(stack.pop())
                stack.append(char)
            else:
                prev += char

        if prev:
            postfix.append(prev)

        while stack:
            postfix.append(stack.pop())
        print(postfix)
        return postfix

    def has_higher_precedence(self, operator: str):
        if operator in ['*', '/']:
            return 1
        elif operator in ['+', '-']:
            return 0
        return -1

sol = Solution()
print(sol.calculate("1+2*5/3+6/4*2"))
