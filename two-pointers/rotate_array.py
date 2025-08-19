# PROBLEM STATEMENT : https://neetcode.io/problems/rotate-array?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com


from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        nums_aux = [0 for i in range(n)]
        for i in range(n):
            nums_aux[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = nums_aux[i]
