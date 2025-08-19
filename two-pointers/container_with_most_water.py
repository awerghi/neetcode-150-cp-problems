# PROBLEM STATEMENT : https://neetcode.io/problems/max-water-container?list=neetcode150
# Author aw.aw.ahmed.werghi@gmail.com


from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0
        while i < j:
            current_height = min(heights[i],heights[j]) * (j-i)
            if current_height > maxi:
                maxi = current_height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxi


s = Solution()
print(s.maxArea([2,2,2]))

