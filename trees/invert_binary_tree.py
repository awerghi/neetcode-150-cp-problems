# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/invert-a-binary-tree?list=neetcode250

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        aux = root.left
        root.left = root.right
        root.right = aux

        return root


s = Solution()
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2 = TreeNode(2,n4,n5)
n3 = TreeNode(3,n6,n7)
n1 = TreeNode(1,n2,n3)


s.invertTree(n1)
print(s.preorderTraversal(n1)) # output => [1, 3, 7, 6, 2, 5, 4]