# Author ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/spiral-matrix-ii/description/

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = []
        for i in range(n):
            matrix.append([0 for _ in range(n)])
        elts_matrix = [elt for elt in range(1, n * n + 1)]
        px = 0
        py = 0
        p_element = 0
        directions = ["right","down","left","up"]
        direction_index = 0
        # when all elts are filled, we can break
        while p_element < len(elts_matrix) :
            direction = directions[direction_index]
            # go in right direction, so increasing px index
            if direction == "right":
                while px < n and matrix[py][px] == 0 :
                    matrix[py][px] = elts_matrix[p_element]
                    p_element += 1
                    px += 1
                px -= 1
                py += 1
                direction_index += 1
                direction_index = direction_index % 4
            # go in down direction, so decreasing py index
            if direction == "down":
                while py < n and matrix[py][px] == 0 :
                    matrix[py][px] = elts_matrix[p_element]
                    p_element += 1
                    py += 1
                direction_index += 1
                direction_index = direction_index % 4
                px -= 1
                py -= 1
            # go in left direction, so decreasing px index
            if direction == "left":
                while px >= 0 and matrix[py][px] == 0 :
                    matrix[py][px] = elts_matrix[p_element]
                    p_element += 1
                    px -= 1
                direction_index += 1
                direction_index = direction_index % 4
                px += 1
                py -= 1
            # go in up direction, so decreasing py index
            if direction == "up":
                while py >= 0 and matrix[py][px] == 0 :
                    matrix[py][px] = elts_matrix[p_element]
                    p_element += 1
                    py -= 1
                direction_index += 1
                direction_index = direction_index % 4
                px += 1
                py += 1
        return matrix


s = Solution()
print(s.generateMatrix(3)) # output : [[1,2,3],[8,9,4],[7,6,5]]
print(s.generateMatrix(1)) # output : [[1]]