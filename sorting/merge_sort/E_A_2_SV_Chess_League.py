#!/usr/bin/python3
"""CodeForces Problem #E --> A2SV Chess League"""
from typing import List


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ratings = [(i, a[i]) for i in range(pow(2, n))]

    def solve(n: int, k: int) -> int:
        def divide(left: int, right: int) -> List[int]:
            if left == right:
                return [ratings[left]]
            mid = left + (right - left) // 2
            left_half = divide(left, mid)
            right_half = divide(mid + 1, right)
            return conquer(left_half, right_half)

        def conquer(leftSide: List[int], rightSide: List[int]):
            result = []
            leftIdx, rightIdx = 0, 0
            while leftIdx < len(leftSide) and rightIdx < len(rightSide):
                if leftSide[leftIdx][1] <= rightSide[rightIdx][1]:
                    if leftSide[leftIdx][1] + k >= rightSide[rightIdx][1]:
                        result.append(leftSide[leftIdx])
                    leftIdx += 1
                else:
                    if rightSide[rightIdx][1] + k >= leftSide[leftIdx][1]:
                        result.append(rightSide[rightIdx])
                    rightIdx += 1
            result.extend(leftSide[leftIdx:])
            result.extend(rightSide[rightIdx:])
            return result
        return divide(0, pow(2, n) - 1)
    final_result = solve(n, k)
    print(*sorted([x[0] + 1 for x in final_result]))


main()
