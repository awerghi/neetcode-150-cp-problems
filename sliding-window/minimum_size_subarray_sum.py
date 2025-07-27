# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/contains-duplicate-ii?list=neetcode250


from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = float('inf')
        n = len(nums)
        aux_sum = 0
        start = 0
        # sliding window technique
        for end in range(n):
            aux_sum += nums[end]
            # if the sum of sliding window is always bigger than target, we increment only start and not end
            while aux_sum >= target :
                min_subarray = min(min_subarray,end - start + 1)
                # we check the sum except the start value and increment start
                aux_sum -= nums[start]
                start += 1
        # if min subarray does not change that means the sum of all elts of array is less than target
        return min_subarray if min_subarray != float('inf') else 0

s = Solution()
print(s.minSubArrayLen(10,[2,1,5,1,5,3]))


