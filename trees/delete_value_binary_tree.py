from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Find the min value of a binary tree
    def findMin(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        #search in the right branch
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # search in the left branch
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # the value is found
        else:
            # node with left child
            if root.right is None:
                return root.left
            # node with right child
            elif root.left is None:
                return root.right

            # find the minimum of the right branch
            temp = self.findMin(root.right)

            # put the temp value in the root
            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)

        return root



s = Solution()

n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3,n1,n4)
n9 = TreeNode(9)
n5 = TreeNode(5,n3,n9)
print(s.deleteNode(n5,3))