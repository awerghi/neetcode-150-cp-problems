# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/contains-duplicate-ii?list=neetcode250

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the case where the length of nums is equal or less than k
        # just check if nums contains only distinct values or not
        if len(nums) <= k :
            if len(set(nums)) != len(nums):
                return True
            else :
                return False
        # each time, take a window and check if the length of set is equal to nums len
        for i in range(len(nums)-k):
            window_nums = nums[i:i+k+1]
            # set gives us non duplicated values
            # if the len of set == to length of nums => nums does not contains duplicate numbers
            if len(set(window_nums)) != len(window_nums):
                return True
        return False


s = Solution()
print(s.containsNearbyDuplicate([99,99],2)) # output : True
print(s.containsNearbyDuplicate([1,2,3,1],3)) # output : True
print(s.containsNearbyDuplicate([2,1,2],1)) # output : False
