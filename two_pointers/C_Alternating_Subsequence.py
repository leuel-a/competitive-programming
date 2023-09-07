from typing import List


def main():
    t = int(input())

    def oppositeSigns(a: int, b: int) -> bool:
        return (a * b) < 0

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        l_max, max_ = a[0], 0
        i = 1
        while i < n:
            if oppositeSigns(l_max, a[i]):
                max_ += l_max
                l_max = a[i]
            else:
                l_max = max(l_max, a[i])
            i += 1
        max_ += l_max
        print(max_)


main()
