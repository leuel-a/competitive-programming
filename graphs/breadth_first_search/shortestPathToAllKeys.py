#!/usr/bin/python3
"""LeetCode Problem #864 --> Shortest Path to Get All Keys"""
from queue import Queue
from collections import defaultdict

class Solution:
    def shortestPathAllKeys(self, g):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = Queue()
        n = len(g)
        m = len(g[0])
        keys = 0

        for i in range(n):
            for j in range(m):
                if g[i][j] == '@':
                    q.put(((i, j), 0))
                if 'a' <= g[i][j] <= 'z':
                    keys += 1

        check = (1 << keys) - 1
        p = defaultdict(int)
        ans = 0

        while not q.empty():
            k = q.qsize()

            for _ in range(k):
                j = q.get()
                x = j[0][0]
                y = j[0][1]
                mask = j[1]

                if mask == check:
                    return ans

                for h in range(4):
                    nx = x + dx[h]
                    ny = y + dy[h]

                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#':
                        if 'a' <= g[nx][ny] <= 'z':
                            n_mask = mask | (1 << (ord(g[nx][ny]) - ord('a')))

                            if (nx, ny, n_mask) not in p:
                                p[(nx, ny, n_mask)] = n_mask
                                q.put(((nx, ny), n_mask))
                        elif 'A' <= g[nx][ny] <= 'Z':
                            c = ord(g[nx][ny]) - ord('A')

                            if (mask & (1 << c)) == 0:
                                continue

                            n_mask = mask

                            if (nx, ny, n_mask) not in p:
                                p[(nx, ny, n_mask)] = n_mask
                                q.put(((nx, ny), n_mask))
                        else:
                            n_mask = mask

                            if (nx, ny, n_mask) not in p:
                                p[(nx, ny, n_mask)] = n_mask
                                q.put(((nx, ny), n_mask))
            ans += 1
        return -1
