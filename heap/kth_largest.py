# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode250

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums) - k
        current = 0
        while n > 0 :
            current = heapq.heappop(nums)
            n -= 1

        return current

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4],2)) # output : 5
print(s.findKthLargest([2,3,1,5,4],2)) # output : 4
print(s.findKthLargest([2,3,1,1,5,5,4],3)) # output : 4
