# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/balanced-binary-tree?list=neetcode250

from typing import Optional

from typing_inspection.introspection import ForbiddenQualifier


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (not p and q) or (not q and p):
            return False
        if p and q and p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

s = Solution()
n2 = TreeNode(2)
n3 = TreeNode(3)
n1 = TreeNode(1,n2,n3)

n2p = TreeNode(2)
n3p = TreeNode(5)
n1p = TreeNode(1,n2p,n3p)

print(s.isSameTree(n1,n1p)) # output : False
