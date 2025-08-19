# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/majority-element-ii?list=neetcode250

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ_map = {}
        n = len(nums)
        majority_res_list = set()
        for elt in nums :
            if occ_map.get(elt) is not None:
                occ_map[elt] += 1
                if occ_map[elt] > n//3:
                    majority_res_list.add(elt)
            else :
                occ_map[elt] = 1
                if n < 3:
                    majority_res_list.add(elt)
        return list(majority_res_list)

s = Solution()
print(s.majorityElement([5,2,3,2,2,2,2,5,5,5])) # -> output : [2, 5]
print(s.majorityElement([4,4,4,4,4]))           # -> output : [4]
print(s.majorityElement([1,2,3]))               # -> output : []
print(s.majorityElement([1]))                   # -> output : [1]


