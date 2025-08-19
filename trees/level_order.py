# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode250

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        current = [root]
        res = [[root.val]]
        while current:
            aux = []
            for elt in current:
                if elt.left is not None : aux.append(elt.left)
                if elt.right is not None : aux.append(elt.right)
            current = aux
            current_vals = [elt.val for elt in current]
            if current_vals : res.append(current_vals)

        return res