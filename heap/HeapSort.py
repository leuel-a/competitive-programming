#!/usr/bin/python3
"""GeeksForGeeks Problem --> Heap Sort"""


class Solution:
    def heapify(self,arr, n, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        max_val = i
        if left_child < n and arr[left_child] > arr[max_val]:
            max_val = left_child

        if right_child < n and arr[right_child] > arr[max_val]:
            max_val = right_child

        if max_val != i:
            arr[max_val], arr[i] = arr[i], arr[max_val]
            self.heapify(arr, n, max_val)

    def buildHeap(self,arr,n):

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)

        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])  # swap
            self.heapify(arr, i, 0)
