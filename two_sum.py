# PROBLEM STATEMENT : https://neetcode.io/problems/two-integer-sum?list=neetcode150

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elt_map = {}
        for i in range(len(nums)):
            if elt_map.get(target-nums[i]) is not None:
                return [elt_map.get(target-nums[i]),i]
            else:
                elt_map[nums[i]] = i

        return [-1]
