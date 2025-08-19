# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/binary-search?list=neetcode150
# Solution: time complexity : O(log(n))
#           space complexity : O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end :
            mid = (start + end) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                start = mid + 1
            else :
                end = mid - 1
        return -1

s = Solution()
print(s.search([-1,0,2,4,6,8],4))