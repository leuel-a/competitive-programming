"""Leetcode Problem #227 --> Basic Calculator II"""
from typing import List


class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace('-', '+-')
        s = s.split('+')
        answer = 0
        for term in s:
            term = term.strip()
            factor = []
            stack = []
            for i in range(len(term)):
                if term[i] == ' ':
                    continue

                if term[i] in "0123456789-":
                    factor.append(term[i])

                else:
                    cur_term = int("".join(factor))
                    factor = []
                    if len(stack) == 2:
                        op = stack.pop()
                        prev_term = stack.pop()
                        if op == "*":
                            stack.append(prev_term*cur_term)
                        else:
                            stack.append(
                                int(str(prev_term/cur_term).split('.')[0]))
                    else:
                        stack.append(cur_term)
                    stack.append(term[i])
            cur_term = int("".join(factor))
            if len(stack) == 2:
                op = stack.pop()
                prev_term = stack.pop()
                if op == "*":
                    stack.append(prev_term*cur_term)
                else:
                    stack.append(int(str(prev_term/cur_term).split('.')[0]))
            else:
                stack.append(cur_term)
            answer += stack[0]

        return answer
