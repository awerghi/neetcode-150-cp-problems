# PROBLEM STATEMENT : https://neetcode.io/problems/car-fleet?list=neetcode150
# Author aw.aw.ahmed.werghi@gmail.com

from typing import List


class Solution:
    def time_to_target(self, position, speed, target):
        return (target - position) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        car_fleet_number = 1

        position_with_speed = [[position[i], speed[i]] for i in range(len(position))]
        position_with_speed.sort(key=lambda x: x[0])
        time_to_target = self.time_to_target(position_with_speed[-1][0], position_with_speed[-1][1], target)

        for i in range(len(position_with_speed) - 2, -1, -1):
            if self.time_to_target(position_with_speed[i][0], position_with_speed[i][1], target) <= time_to_target:
                continue
            else:
                time_to_target = self.time_to_target(position_with_speed[i][0], position_with_speed[i][1], target)
                car_fleet_number += 1

        return car_fleet_number





s = Solution()

print(s.carFleet(target=12,position=[10,8,0,5,3],speed=[2,4,1,1,3])) # answer : 3
