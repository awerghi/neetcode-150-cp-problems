# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/last-stone-weight?list=neetcode250


import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * elt for elt in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            current1 = heapq.heappop(stones)
            current2 = heapq.heappop(stones)
            if current1 ==  current2 :
                continue
            else :
                heapq.heappush(stones,current1-current2)
        if len(stones) == 0 :
            return 0
        else :
            return stones[0] * -1

s = Solution()
print(s.lastStoneWeight([1,2])) # output : 1
print(s.lastStoneWeight([2,3,6,2,4])) # output : 1