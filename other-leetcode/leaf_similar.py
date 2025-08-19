# Author aw.ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/leaf-similar-trees/description/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isLeaf(self,root):
        if root is not None and root.left is None and root.right is None:
            return True
        else :
            return False

    def get_leafs(self,root):
        self.leafs = []

        def recur(current):
            if current is None:
                return None

            recur(current.left)
            recur(current.right)
            if self.isLeaf(current):
                self.leafs = [current.val] + self.leafs

        recur(root)
        return self.leafs

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if self.get_leafs(root1) == self.get_leafs(root2):
            return True
        else :
            return False

s = Solution()
n2 = TreeNode(2)
n3 = TreeNode(3)
n1 = TreeNode(1,n2,n3)
n11 = TreeNode(1,n3,n2)
print(s.leafSimilar(n1,n11)) # output : False

