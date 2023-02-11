#!/usr/bin/python3
from itertools import accumulate

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        arr = [0]*(n+1)
        for lv, ar, seats in bookings:
            arr[lv-1]+= seats
            arr[ar]-= seats
        return list(accumulate(arr[:-1]))

