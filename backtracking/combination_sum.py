from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combinations_list = []
        combination = []

        def backtrack(i):
            if sum(combination) == target :
                combinations_list.append(combination.copy())
                return

            if i >= len(nums):
                return

            if sum(combination) > target:
                return

            combination.append(nums[i])
            backtrack(i)

            combination.pop()
            backtrack(i+1)

        backtrack(0)
        return combinations_list

s = Solution()
print(s.combinationSum([2,5,6,9],9))

