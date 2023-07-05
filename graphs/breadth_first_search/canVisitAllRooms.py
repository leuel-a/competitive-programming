#!/usr/bin/python3
"""LeetCode Problem #841 --> Keys and Rooms"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue, visited = deque(), set()

        queue.append(0)
        while queue:
            room = queue.popleft()

            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
        return len(rooms) == len(visited)
