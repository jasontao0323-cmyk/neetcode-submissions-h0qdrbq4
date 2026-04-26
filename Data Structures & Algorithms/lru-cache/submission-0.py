# Brute Force
# LRU cache uses a list to store (key, value) pairs. Accessing a key moves it to the end, while inserting a new key updates existing 
# keys or removes the least recently used key if the cache is full.
# TC: O(n) for each put() and get() operation
# SC: O(n)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return

        if self.capacity == len(self.cache):
            self.cache.pop(0)

        self.cache.append([key, value])
