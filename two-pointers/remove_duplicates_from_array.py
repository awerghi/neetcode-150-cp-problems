# PROBLEM STATEMENT : https://neetcode.io/problems/remove-duplicates-from-sorted-array?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map_occ = {}
        for elt in nums:
            if map_occ.get(elt) is not None:
                map_occ[elt] += 1
            else:
                map_occ[elt] = 1

        pointer = 0
        for i in range(len(nums)):
            if map_occ.get(nums[i]) != 0:
                nums[pointer] = nums[i]
                map_occ[nums[i]] = 0
                pointer += 1
            else:
                continue
        return len(map_occ.keys())
