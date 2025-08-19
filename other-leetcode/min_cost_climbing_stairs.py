# Author aw.ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs_dp = [0 for _ in range(len(cost))]
        costs_dp[0] = cost[0]
        costs_dp[1] = cost[1]

        for i in range(2,len(cost)):
            costs_dp[i] = min(costs_dp[i-1]+cost[i],costs_dp[i-2]+cost[i])
        return min(costs_dp[-1],costs_dp[len(cost)-2])

s = Solution()
cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]

print(s.minCostClimbingStairs(cost1)) # output : 15
print(s.minCostClimbingStairs(cost2)) # output : 6