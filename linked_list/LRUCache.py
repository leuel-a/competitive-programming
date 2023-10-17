"""Leetcode Problem #146 --> LRU Cache"""


class Node:

    def __init__(self, key, val):
        """Defines a node for a doubly linked list"""
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        """Initializes the LRU cache"""
        self.cap = capacity
        self.cache = {}  # Map key --> node

        # left=LRU, right=MRU
        self.left, self.right = Node(0, 0), Node(0, 0)

        # Making them both the start and end pointers
        self.left.next, self.right.prev = self.right, self.left

    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        """Gets a value from the cache if the value exists in the cache"""
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
