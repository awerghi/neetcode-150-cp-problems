# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/majority-element?list=neetcode250

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_map = {}
        maxi = 0
        elt_maxi = 0
        for elt in nums:
            majority_map[elt] = majority_map[elt] + 1 if majority_map.get(elt) else 1
            if majority_map[elt] > maxi:
                maxi = majority_map[elt]
                elt_maxi = elt
        return elt_maxi

