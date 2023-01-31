#!/usr/bin/python3
"""Defines the Solution Class"""
from math import floor, ceil


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluates an RPN expression"""
        stack = []
        for token in tokens:
            if token in ["+" , "-", "*", "/"]:
                firstOperand = stack.pop()
                secondOperand = stack.pop()
                if token == "+":
                    stack.append(secondOperand + firstOperand)
                elif token == "-":
                    stack.append(secondOperand - firstOperand)
                elif token == "*":
                    stack.append(secondOperand * firstOperand)
                elif token == "/":
                    dividend = secondOperand / firstOperand
                    if dividend < 0:
                        stack.append(ceil(dividend))
                    else:
                        stack.append(floor(dividend))
            else:
                stack.append(int(token))
        return stack.pop()
