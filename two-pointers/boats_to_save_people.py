# PROBLEM STATEMENT : https://neetcode.io/problems/boats-to-save-people?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        number_rescue_boats = 0
        while start <= end :
            # when the max elt of people is more than limit, it means it should be carried only
            # we decrease by one from end in order to check the next max
            if people[start] + people[end] > limit:
                number_rescue_boats += 1
                end -= 1
            else :
                # we can carry two people together, one from min and one from maximum
                number_rescue_boats += 1
                start += 1
                end   -= 1
        return number_rescue_boats

s = Solution()
print(s.numRescueBoats([1,3,2,3,2],3)) # output : 2
print(s.numRescueBoats([5,1,4,2],6)) # output : 3


