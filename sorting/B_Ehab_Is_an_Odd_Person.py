#!/usr/bin/python3
"""Codeforces Problem #1174 --> B. Ehab Is an Odd Person"""
from typing import List


def lexicographically_smallest_array() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    ex = [False, False]

    for num in arr:
        ex[num % 2] = True

    if ex[0] and ex[1]:
        arr.sort()

    for num in arr:
        print(num, end=" ")


if __name__ == '__main__':
    lexicographically_smallest_array()
