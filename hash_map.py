# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/concatenation-of-array?list=neetcode250

# simple hashmap implementation
class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        for i,k in enumerate(self.map):
            if k == key:
                return self.map[k]
        return -1
    def remove(self, key: int) -> None:
        for i,k in enumerate(self.map):
            if k == key:
                del self.map[k]
                return


# example
obj = MyHashMap()
obj.put(1,1) # -> output : null
obj.put(2,2) # -> output : null
print(obj.map)          # -> output : {1: 1, 2: 2}
print(obj.get(1))       # -> output : 1
print(obj.get(3))       # -> output : -1
obj.put(2,1) # -> output : null
print(obj.map)          # -> output : {1: 1, 2: 1}
print(obj.get(2))       # -> output : 1
obj.remove(2)           # -> output : null
print(obj.map)          # -> output : {1: 1}
print(obj.get(2))       # -> output : -1