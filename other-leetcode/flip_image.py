# Author aw.ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/flipping-an-image/description/

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for elt in image:
            elt.reverse()
            for i in range(len(elt)):
                elt[i] = 0 if elt[i] == 1 else 1
        return image

s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])) # output : [[1,0,0],[0,1,0],[1,1,1]]