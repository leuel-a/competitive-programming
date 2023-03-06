def main():
    num_of_cards = int(input())
    cards = list(map(lambda x : int(x), input().split()))

    left, right = 0, num_of_cards - 1
    p1, p2 = 0, 0
    while left < right:
        if cards[left] > cards[right]:
            p1 += cards[left]
            left += 1
        else:
            p1 += cards[right]
            right -= 1

        if cards[left] > cards[right]:
            p2 += cards[left]
            left += 1
        else:
            p2 += cards[right]
            right -= 1

    if left == right:
        p1 += cards[left]

    print(f'{p1} {p2}')

if __name__ == '__main__':
    main()
