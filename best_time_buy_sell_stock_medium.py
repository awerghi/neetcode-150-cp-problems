# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii?list=neetcode250

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] < buy :
                buy = prices[i]
                sell = prices[i]
            if prices[i] > sell :
                sell = prices[i]
                profit += sell - buy
                buy = prices[i]
        return profit


s = Solution()
print(s.maxProfit([1,2,3,4,5])) # output : 4
print(s.maxProfit([7,1,5,3,6,4])) # output : 7
