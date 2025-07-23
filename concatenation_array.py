# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/concatenation-of-array?list=neetcode250

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

s = Solution()
print(s.getConcatenation([1,4,1,2])) # -> output : [1, 4, 1, 2, 1, 4, 1, 2]
print(s.getConcatenation([22,21,20,1])) # -> output : [22, 21, 20, 1, 22, 21, 20, 1]