#!/usr/bin/python3
"""GeeksForGeeks Problem --> Selection Sort"""


class Solution:
    def select(self, arr, i):
        _min = i

        for j in range(i + 1, len(arr)):
                if arr[j] < arr[_min]:
                    _min = j
        return _min


    def selectionSort(self, arr,n):
        i = 0

        while i < len(arr):
            jMin = self.select(arr, i)

            if jMin != i:
                arr[jMin], arr[i] = arr[i], arr[jMin]
            i += 1

        return arr
