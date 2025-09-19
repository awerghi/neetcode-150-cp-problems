from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums) - 1
        for i in range(len(nums)-2,0,-1):
            print(f"{nums[i]} - {to_reach} - {i}")
            if nums[i] >= to_reach - i :
                to_reach = i
        if nums[0] < to_reach:
            return False
        return True

s = Solution()
print(s.canJump([0]))