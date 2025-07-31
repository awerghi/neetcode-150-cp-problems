# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/balanced-binary-tree?list=neetcode250


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ok = True

        def recur(curr):
            if curr is None :
                return 0

            left = recur(curr.left)
            right = recur(curr.right)
            if not right : right = 0
            if not left : left = 0
            if abs(right - left) > 1 :
                self.ok = False
            else :
                return 1+max(left,right)

        recur(root)
        return self.ok

s = Solution()
n4 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(3,n4)
n1 = TreeNode(1,n2,n3)

print(s.isBalanced(n1)) # => output : True