# Author aw.aw.ahmed.werghi@gmail.com
# PROBLEM STATEMENT : https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150

import heapq
from typing import List

class Point:

    def __init__(self,point,distance):
        self.point = point
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class Solution:
    def calculate_distance_to_origin(self,x,y):
        return pow(pow(x,2) + pow(y,2),1/2)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            distance = self.calculate_distance_to_origin(point[0],point[1])
            p_aux = Point(point,distance)
            heapq.heappush(pq,p_aux)

        i = 0
        res_points = []
        while i < k :
            current = heapq.heappop(pq)
            res_points.append(current.point)
            i += 1
        return res_points

s = Solution()
print(s.kClosest([[0,2],[2,2]],1)) # answer : [[0,2]]
print(s.kClosest([[0,2],[2,0],[2,2]],2)) # answer : [[0,2],[2,0]]






