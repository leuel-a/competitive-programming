#!/usr/bin/python3
"""CodeForces Problem #26A --> Almost Prime"""


def main() -> None:
    n = int(input())
    almost = 0

    for i in range(6, n + 1):
        d, _set = 2, set()

        while d * d <= i:
            while i % d == 0:
                _set.add(d)
                i //= d
            d += 1
        if i > 1:
            _set.add(i)

        almost += 1 if len(_set) == 2 else 0
    print(almost)


if __name__ == '__main__':
    main()
