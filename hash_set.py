# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/design-hashset?list=neetcode250

class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        for i in range(len(self.hashset)):
            if self.hashset[i] == key :
                return True
        return False

obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.hashset)
obj.remove(4)
print(obj.hashset)
obj.remove(1)
print(obj.hashset)
print(obj.contains(3))
print(obj.contains(5))