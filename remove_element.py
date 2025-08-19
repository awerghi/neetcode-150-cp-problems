# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/remove-element?list=neetcode250

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        number_val = 0
        for i in range(len(nums)):
            if nums[i] == val :
                number_val += 1
            else :
                nums [i-number_val] = nums[i]
        return len(nums)-number_val
