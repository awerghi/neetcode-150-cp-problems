# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/depth-of-binary-tree?list=neetcode250

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None :
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left,right)

s = Solution()
n4 = TreeNode(4)
n3 = TreeNode(3,n4)
n2 = TreeNode(2)
n1 = TreeNode(1,n2,n3)
print(s.maxDepth(n1)) # output => 3