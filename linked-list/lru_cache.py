# PROBLEM STATEMENT : https://neetcode.io/problems/lru-cache?list=neetcode150
# Author aw.aw.ahmed.werghi@gmail.com

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.usage = {}
        self.priority = 1

    def get(self, key: int) -> int:
        result = self.cache.get(key,-1)
        if result != 1:
            self.usage[key] = self.priority
            self.priority += 1
        return result

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key,-1) == -1:
            if len(self.cache.items()) == self.capacity:
                min_key = min(self.usage, key=self.usage.get)
                del self.cache[min_key]
                del self.usage[min_key]
            self.cache[key] = value
            self.usage[key] = self.priority
            self.priority += 1
        else :
            self.cache[key] = value
            self.usage[key] = self.priority
            self.priority += 1


