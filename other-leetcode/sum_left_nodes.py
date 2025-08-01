# Author ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isleaf (self,root):
        if root and not root.left and not root.right :
            return True
        else:
            return False

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum_elts = 0

        def recur(curr):

            if curr is None :
                return 0

            recur(curr.left)
            recur(curr.right)

            if self.isleaf(curr.left) :
                self.sum_elts += curr.left.val


        recur(root)
        return self.sum_elts