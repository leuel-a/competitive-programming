#!/usr/bin/python3
"""CodeForces Problem --> Less or Equal"""
from typing import List, Optional


def lessOrEqual():
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))
    nums.sort()

    if k == 0:
        if nums[0] == 1:
            print(-1)
        else:
            print(1)
    else:
        if k == n:
            print(nums[k - 1])
        elif nums[k - 1] == nums[k]:
            print(-1)
        else:
            print(nums[k - 1])
            
if __name__ == "__main__":
    lessOrEqual()
