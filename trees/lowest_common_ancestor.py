# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # get the ancestors of a specific node in the bst using bst search filter
    def node_ancestors(self,root : TreeNode, node : TreeNode):
        self.ancestors = []
        def traverse(current):

            if current is None :
                return []

            # bst search filter to get the path of the search
            # we are sure that the bst contains p or q
            if current.val == node.val:
                return self.ancestors
            elif node.val < current.val :
                self.ancestors.append(current)
                return traverse(current.left)
            else :
                self.ancestors.append(current)
                return traverse(current.right)
        traverse(root)
        return self.ancestors

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # get p ancestors
        p_ancestors = self.node_ancestors(root,p)
        # get q ancestors
        q_ancestors = self.node_ancestors(root,q)

        # no common node, it will root of the tree
        lowest_common = root

        # iterate through the min of the two list of ancestors
        # if ancestor is the same, change lowest common and continue
        # break when there is a difference in the path
        for i in range(min(len(q_ancestors),len(p_ancestors))):
            if q_ancestors[i] == p_ancestors[i]:
                lowest_common = q_ancestors[i]
            else :
                break

        q_ancestors_vals = [elt.val for elt in q_ancestors]
        p_ancestors_vals = [elt.val for elt in q_ancestors]

        # if p is in q ancestors
        if p.val in q_ancestors_vals :
            return p
        # if q in p ancestors
        elif q.val in p_ancestors_vals:
            return q
        return lowest_common

