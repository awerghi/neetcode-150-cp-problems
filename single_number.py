from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res ^= num

        return res

s = Solution()
print(s.singleNumber([3,2,3]))