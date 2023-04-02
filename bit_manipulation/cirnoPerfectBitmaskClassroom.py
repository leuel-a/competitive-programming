#!/usr/bin/python3

def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        x = int(input())

        i = 0
        while x & (1 << i) == 0:
            i += 1

        val, not_found = 1 << i, True
        while not_found:
            if x & val > 0 and x ^ val > 0:
                print(val)
                break
            val += 1

if __name__ == '__main__':
    main()
