def main():
    num_of_tests = int(input())
    queue = input().split()

    num_of_new_ppl = int(input())
    for i in range(num_of_new_ppl):
        new_person = input()
        low, high = 0, len(queue) - 1
        while low < high:
            mid = low + (high - low) // 2

            if (new_person > queue[mid]) == True:
                low = mid + 1
            else:
                high = mid - 1
        print(high)


if __name__ == '__main__':
    main()

# Ananiya Bereket Daniel Fikremariam Gizaw Haile Jeal Kidus KinfeMichael Leul
