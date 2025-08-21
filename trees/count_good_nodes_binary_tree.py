# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        # track the number of good nodes outside the traversal
        self.number_good_nodes = 0
        # first good_node is root
        self.previous_good_node = root

        def traverse(current, previous_good_node):

            if current is None:
                return None

            u_previous_good_node = previous_good_node
            # a good node is a node greater or equal to the last good one because the node between them if exists are not good
            if current.val >= previous_good_node.val:
                u_previous_good_node = current
                self.number_good_nodes += 1

            traverse(current.left, u_previous_good_node)
            traverse(current.right, u_previous_good_node)

        traverse(root, self.previous_good_node)
        return self.number_good_nodes




