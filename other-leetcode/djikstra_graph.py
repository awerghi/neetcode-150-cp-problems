# Author ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/network-delay-time/description/


import heapq
from typing import List

class Solution:
    def build_adjacency_list(self,n,linput):
        adj = []
        for _ in range(n):
            adj.append([])
        for source,destination,time in linput:
            adj[source-1].append([time,destination-1])
        return adj

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heappush(heap,[0,k-1])
        adjacency_list = self.build_adjacency_list(n,times)
        distances = []
        visited = set()
        while heap :

            current = heapq.heappop(heap)
            if current[1] in visited:
                continue
            visited.add(current[1])
            distances.append(current[0])
            for time,dest in adjacency_list[current[1]]:
                if dest not in visited:
                    heapq.heappush(heap,[time+current[0],dest])
        if len(distances) < n :
            return -1
        else :
            return max(distances)

s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)) # output : 2
print(s.networkDelayTime([[1,2,1]],2,2)) # output : -1





