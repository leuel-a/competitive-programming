def main():
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(int, input().split())
        left, right = 0, (a + b) // 4
        while left <= right:
            mid = left + (right - left) // 2
            if a - mid >= 0 and b - mid >= 0:
                aux = a - mid + b - mid
                if mid * 2 <= aux:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right = mid - 1
        print(right)

if __name__ == '__main__':
    main()
