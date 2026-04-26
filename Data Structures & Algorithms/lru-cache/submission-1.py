# LRUCache
# Built-In Data Structure
# Built-in ordered maps/dictionaries, which store key-value pairs and track insertion/update order, are ideal for implementing LRU caches. They enable fast 
# lookups, updates, and removals, simplifying the cache implementation.
# TC: O(1)
# SC: O(n)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
