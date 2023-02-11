#!/usr/bin/python3
"""Defines the Solution class for the LeetCode problem 973

Description:
    Given an array of points where points[i] = [xi, yi] represents
    a point on the X-Y plane and an integer k, return the k closest
    points to the origin (0, 0).

    The distance between two points on the X-Y plane is the
    Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is
    guaranteed to be unique (except for the order that it is in).
"""
from math import sqrt


class Solution:
    """Solution class for the problem"""
    def k_closest(self, points: list[list[int]], k: int) -> list[int]:
        """Finds the k closest points to the origin in a given
        list of points"""

        dict_s = {}
        for point in points:
            dist = sqrt((point[0] ** 2) + (point[1] ** 2))
            dict_s[tuple(dist)] = point

        myKeys = list(dict_s)
        myKeys.sort()
        s_points = []
        for i in myKeys:
            s_points.append(dict_s[i])
        print(dict_s)
        print(s_points)
