#!/usr/bin/python3
"""CodeForces Problem #https://codeforces.com/contest/664/problem/A --> Complicated GCD"""


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


