# PROBLEM STATEMENT : https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
# Author aw.ahmed.werghi@gmail.com
# Author comment : a very interesting pb, the complexity is how you can solve it in O(n)

from typing import List

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array_sum = 0
        array_sums = [0]

        # build an array of the sums of integers in an interval [l,r]
        for i in range(len(nums)):
            array_sums.append(nums[i] + array_sums[i])

        # a map to keep track of the previous sums
        tracking_map = {}
        for elt in array_sums:
            # if there is a value for key elt - k, that means we have a sum in a specific intervall equal to k
            if tracking_map.get(elt-k):
                # we add the value of the key to say it exists l1,l2 ... starts for the interval
                sub_array_sum += tracking_map[elt-k]
            if tracking_map.get(elt):
                tracking_map[elt] += 1
            else :
                tracking_map[elt] = 1
        return sub_array_sum

s = Solution()
print(s.subarraySum([4,4,4,4,4,4],4)) # -> output : 6
print(s.subarraySum([2,-1,1,2],2))    # -> output : 2
