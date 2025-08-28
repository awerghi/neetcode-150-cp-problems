# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/subsets?list=neetcode150

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset_list = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                subset_list.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return subset_list

s = Solution()
print(s.subsets([1,2,1]))