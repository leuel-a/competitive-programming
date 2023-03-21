#!/usr/bin/python3
"""HackerRank Problem --> Counting Sort 1"""

def countingSort(arr):
    count_array = [0] * 100

    for i in arr:
        count_array[i] += 1
    return count_array
