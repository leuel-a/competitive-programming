#!/usr/bin/python3
"""HackerRank Problem --> Insertion Sort 1"""

def print_array(arr):
    check = False
    for i in arr:
        if check:
            print(' ', end='')
        print(i, end='')

        if not check:
            check = True
    print()

def insertionSort1(n, arr):
    i = len(arr) - 2
    last_element = arr[-1]

    while i >= 0 and arr[i] > last_element:
        arr[i + 1] = arr[i]
        print_array(arr)
        i -= 1
    arr[i + 1] = last_element
    print_array(arr)

