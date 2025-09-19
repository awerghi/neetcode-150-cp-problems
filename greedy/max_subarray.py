from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_subarray = float("-inf")
        for i in range(len(nums)):
            current_sum += nums[i]
            max_subarray = max(max_subarray,current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_subarray

s = Solution()
print(s.maxSubArray([-1]))
