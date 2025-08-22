# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/valid-binary-search-tree?list=neetcode150
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.valid_bst = True

        def traverse(current):
            if current is None:
                return None

            left,mini,maxi = traverse(current.left)
            right,mini1,maxi1 = traverse(current.right)

            if (left and left.val >= current.val) or (right and right.val <= current.val)\
                    or (current.val >= mini1) or (current.val <= maxi):
                self.valid_bst = False

            if left and right: return current,min(mini,left.val),max(maxi,right.val)
            if left : return current,min(left.val,mini),0
            if right : return current,1001,max(maxi,right.val)
            return current,1001,0

        traverse(root)
        return self.valid_bst
