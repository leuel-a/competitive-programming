#!/usr/bin/python3

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    i = j = total = 0
    dict_s = {}
    lst = []
    maxLen = float('-inf')

    while j < len(arr):
        # print(i, j, total)c
        if arr[j] not in dict_s.keys():
            dict_s[arr[j]] = 1
            total += 1

            while total > k:
                dict_s[arr[i]] -= 1
                if dict_s[arr[i]] == 0:
                    del dict_s[arr[i]]
                    total -= 1
                i += 1
        else:
            dict_s[arr[j]] += 1

        if total == k:
            if maxLen < (j - i + 1):
                lst.append([i + 1, j + 1])
                maxLen = j - i + 1
        j += 1
        print(lst)





    print(f'{lst[-1][0]} {lst[-1][1]}')

if __name__ == '__main__':
    main()
