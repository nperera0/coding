'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

'''



# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    depth = []

    def maxDepth_helper(self, root, cur_d):

        if root.left is None and root.right is None:
            self.depth.append(cur_d)
            return

        elif root.left is not None and root.right is None:
            self.maxDepth_helper(root.left, cur_d += 1)

        elif root.right is not None and root.left is None:
            self.maxDepth_helper(root.right, cur_d += 1)

        else:
            self.maxDepth_helper(root.left, cur_d += 1)
            self.maxDepth_helper(root.right, cur_d += 1)


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth_helper(root, 0)

        return max(depth)
