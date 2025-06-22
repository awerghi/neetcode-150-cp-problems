# Problem statement : https://neetcode.io/problems/duplicate-integer?list=neetcode150
# Author aw.ahmed.werghi@gmail.com

from typing import List

class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        map_occ = {}
        for elt in nums:
            if map_occ.get(elt) is not None:
                return True
            else:
                map_occ[elt] = 1

        return False

s = Solution()

print(s.hasDuplicate([1, 2, 3, 3])) # -> True
print(s.hasDuplicate([1, 2, 3, 4])) # -> False
