def main():
    num_of_test_cases = int(input())
    for _ in range(num_of_test_cases):
        s = input()

        i, j = 0, 0
        dict_s, total = {}, 0
        minLen = float('inf')
        while j < len(s):
            if s[j] not in dict_s.keys():
                dict_s[s[j]] = 1
                total += 1

                while total == 3:
                    dict_s[s[i]] -= 1
                    minLen = min(minLen, j - i + 1)

                    if dict_s[s[i]] == 0:
                        del dict_s[s[i]]
                        total -= 1
                    i += 1
            else:
                dict_s[s[j]] += 1

            j += 1

        if minLen == float('inf'):
            minLen = 0
        print(minLen)


if __name__ == '__main__':
    main()
