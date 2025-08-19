# Author ahmed.werghi
# Email aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                # Minimum is in the right half
                start = mid + 1
            else:
                # Minimum is in the left half (including mid)
                end = mid

        return nums[start]



s = Solution()
print(s.findMin([2,1]))