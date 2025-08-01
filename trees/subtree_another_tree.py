# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode250


from typing import Optional


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
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None :
            return True
        if not root or not subRoot :
            return False
        if root.val == subRoot.val and self.isSameTree(root,subRoot) :
            return True
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()

n5 = TreeNode(5)
n6 = TreeNode(6)
n4 = TreeNode(4,n6)
n3 = TreeNode(3)
n2 = TreeNode(2,n4,n5)
n1 = TreeNode(1,n2,n3)


n4p = TreeNode(4)
n5p = TreeNode(5)
n2p = TreeNode(2,n4p,n5p)

print(s.isSubtree(n1,n2p)) # output : False

