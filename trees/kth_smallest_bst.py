# Author ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode250
import heapq
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal (self,root):
        if root is None:
            return []

        left = self.inorder_traversal(root.left)
        right = self.inorder_traversal(root.right)

        return left + [root.val] + right



    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        traversal = self.inorder_traversal(root)

        heapq.heapify(traversal)

        current = 0
        while k > 0 :
            current = heapq.heappop(traversal)
            k -= 0

        return current.val

