# PROBLEM STATEMENT : https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
# Author aw.ahmed.werghi@gmail.com


# The idea is to solve the problem in O(n) time complexity

from typing import List
import heapq



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # use heapify to convert a list to a heap
        heapq.heapify(nums)
        if len(nums) == 0: return 0

        # pop the heap elt, which always be the minimum number in the heap
        last = heapq.heappop(nums)
        consecutive = 1
        max_largest = 1
        while nums:
            current = heapq.heappop(nums)

            # check if the difference between last element and current is one
            # else break and begin a new counter
            if current - last == 1:
                consecutive += 1
                if consecutive > max_largest:
                    max_largest = consecutive
                last = current
                continue
            elif current == last:
                last = current
                continue
            else:
                last = current
                consecutive = 1

        return max_largest
