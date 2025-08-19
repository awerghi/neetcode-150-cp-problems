# Author ahmed.werghi
# Email aw.ahmed.werghi@gmail.com

# Solution : time complexity : O(log(h)*len(piles))
############################# log(h) : binary search to get min k , len(piles) : iterate each time

from typing import List

class Solution:

    def number_of_hours_needed_ok (self, piles : List[int], k : int, h : int) -> int :
        res_needed_hours = 0
        for elt in piles:
            if elt % k == 0 :
                res_needed_hours += elt // k
            else :
                res_needed_hours += (elt // k) + 1
        
        # check if the needed hours to finish is less than the given time h
        if res_needed_hours <= h:
            ok = True
        else:
            ok = False
        return  ok

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res_min_eating_speed = 0
        start = 0
        end = max(piles)

        while start <= end:

            mid = (start + end) // 2

            if mid != 0 and self.number_of_hours_needed_ok(piles,mid,h):
                res_min_eating_speed = mid
                end = mid - 1
            else :
                start = mid + 1

        return res_min_eating_speed

s = Solution()
print(s.minEatingSpeed([1,4,3,2],9))
print(s.minEatingSpeed([25,10,23,4],4))
print(s.minEatingSpeed([3,6,7,11],8))