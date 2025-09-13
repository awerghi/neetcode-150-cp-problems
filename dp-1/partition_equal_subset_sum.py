# Author aw.ahmed.werghi@gmail.com
# PROBLEM STATEMENT : https://neetcode.io/problems/partition-equal-subset-sum?list=neetcode150

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp_sums = [[nums[0]]]
        total_sum = sum(nums)
        for i in range(1,len(nums)):
            dp_aux_sums = [nums[i]]
            for elt in dp_sums[i-1]:
                aux_sum = elt + nums[i]
                dp_aux_sums.append(aux_sum)
                if aux_sum == total_sum / 2:
                    return True
            dp_sums.append(dp_aux_sums)
        return False

s = Solution()
print(s.canPartition([1,2,3,4,5]))

