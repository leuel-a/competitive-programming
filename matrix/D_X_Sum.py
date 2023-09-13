from typing import List, Tuple

def solve() -> None:
    t = int(input())

    directions: List[Tuple[int, int]] = [
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1)
    ]

    def inbound(row: int, col: int) -> bool:
        return 0 <= row < n and 0 <= col < m

    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        
        max_sum = -1
        for i in range(n):
            for j in range(m):
                curr_sum = grid[i][j]

                for rInc, cInc in directions:
                    r, c = i + rInc, j + cInc
                    while inbound(r, c):
                        curr_sum += grid[r][c]
                        r += rInc
                        c += cInc
                if max_sum < curr_sum:
                    max_sum = curr_sum
        print(max_sum)


solve()