# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/binary-tree-diameter?list=neetcode250
# GOT some hints in order to solve it

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        def recur(curr):
            if curr is None :
                return 0

            left = recur(curr.left)
            right = recur(curr.right)
            self.diameter = max(self.diameter,left+right)
            return 1 + max (left,right)
        recur(root)
        return self.diameter

s = Solution()
n4 = TreeNode(4)
n5 = TreeNode(5)
n3 = TreeNode(3,n5)
n2 = TreeNode(2,n3,n4)
n1 = TreeNode(1,None,n2)


print(s.diameterOfBinaryTree(n1)) # output => 3

n12 = TreeNode(2)
n13 = TreeNode(3)
n11 = TreeNode(1,n12,n13)

print(s.diameterOfBinaryTree(n11)) # output => 2