import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def search (self):
        # in python, only min heap is defined, we need kth largest, so we multiply by -1 in order to make it min heap
        # in the other direction
        pq = [-1 * elt for elt in self.nums.copy()]
        # magic tool to convert list to heap in O(n)
        heapq.heapify(pq)
        # get the k min elt in the negative which is the kth largest in the positive
        i = 1
        while i < self.k  and pq:
            current = heapq.heappop(pq)
            i += 1
        # multiply by -1 and return the result
        return heapq.heappop(pq) * -1

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.search()


s = KthLargest(3,[1, 2, 3,3])
print(s.add(3)) # output : 3
print(s.add(5)) # output : 3
print(s.add(6)) # output : 3
print(s.add(7)) # output : 5
print(s.add(8)) # output : 6