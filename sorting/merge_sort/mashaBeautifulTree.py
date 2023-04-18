#!/usr/bin/python3
"""CodeForces Problem --> Masha and Beautiful Tree"""


def main() -> None:
    test_cases = int(input())
    swap_count = 0

    def merge_sort(nums: list[int]) -> list[int]:

        def divide(start: int, end: int) -> list[int]:
            if start == end:
                return [nums[start]]

            mid = start + (end - start) // 2
            left_side = divide(start, mid)
            right_side = divide(mid + 1, end)
            return merge(left_side, right_side)

        def merge(left_side: list[int], right_side: list[int]) -> list[int]:
            global swap_count

            res = []
            

        return divide(0, len(nums) - 1)


    for _ in range(test_cases):
        m = int(input())
        nums = map(int, input().split())



