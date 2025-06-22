# Problem statement : https://neetcode.io/problems/daily-temperatures?list=neetcode150
# Author aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def find_next_warmer(self,nums : List[int], target : int) -> int:
        count = 0
        ok = False
        while nums:
            current = nums.pop()
            if current > target:
                ok = True
                count += 1
                return count
            else :
                count += 1
        if ok:
            return count
        else:
            return 0


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_r = []
        res_temperatures = []
        while temperatures:
            current = temperatures.pop()
            stack_r_copy = stack_r.copy()
            next_warmer = self.find_next_warmer(stack_r_copy,current)
            res_temperatures.append(next_warmer)
            stack_r.append(current)
        res_temperatures.reverse()
        return res_temperatures



s = Solution()
print(s.dailyTemperatures([22,21,20]))
print(s.dailyTemperatures([30,38,30,36,35,40,28]))


