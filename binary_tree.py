
'''
Determine if a binary tree is a binary search tree
Given a Binary Tree, figure out whether it’s a Binary Search Tree.
In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree,
and is greater than the key values of all nodes in the left subtree. Below is an example of a binary tree that is a valid BST.

'''


def is_bst(root, minVal=float('-inf'), maxVal=float('inf')):
  #TODO: Write - Your - Code

  if root is None:
    return True

  if root.data > minVal and root.data < maxVal and \
  is_bst(root.left, minVal, root.data) and \
  is_bst(root.right, root.data, maxVal):
    return True
  else:
    return False
