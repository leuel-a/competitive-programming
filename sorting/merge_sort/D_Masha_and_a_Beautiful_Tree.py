#!/usr/bin/python3
"""Codeforces  Problem --> Masha and a Beautiful Tree"""
from typing import List


def mashaAndBeautifulTree():
    t = int(input())

    for _ in range(t):
        m = int(input())
        p = list(map(int, input().split()))

        count = 0
        def makeBeautiful(array: List[int]) -> List[int]:

            def divide(left: int, right: int) -> List[int]:
                if left == right:
                    return [array[left]]

                mid = left + (right - left) // 2

                leftSide = divide(left, mid)
                rightSide = divide(mid + 1, right)
                return conquer(leftSide, rightSide)

            def conquer(left: List[int], right: List[int]) -> List[int]:
                nonlocal count
                result = []

                if left[0] > right[0]:
                    result.extend(right)
                    result.extend(left)
                    count += 1
                else:
                    result.extend(left)
                    result.extend(right)
                return result
            return divide(0, len(array) - 1)
        result = makeBeautiful(p)
        print(count if result == sorted(result) else -1)



if __name__ == '__main__':
    mashaAndBeautifulTree()
