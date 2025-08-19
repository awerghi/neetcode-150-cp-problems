# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/sort-colors?list=neetcode250

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        map_occ = {}

        for elt in nums:
            if map_occ.get(elt) is not None:
                map_occ[elt] += 1
            else :
                map_occ[elt] = 1

        for i in range(map_occ.get(0,0)):
            nums[i] = 0

        for i in range(map_occ.get(0,0),map_occ.get(0,0)+map_occ.get(1,0)):
            nums[i] = 1

        for i in range(map_occ.get(0,0)+map_occ.get(1,0),len(nums)):
            nums[i] = 2

s = Solution()
nums = [1,0,1,2]
nums1 = [2,1,0]
s.sortColors(nums)
s.sortColors(nums1)
print(nums) # -> [0,1,1,2]
print(nums1) # -> [0,1,2]

