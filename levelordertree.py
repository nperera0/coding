'''
Level Order Traversal of Binary Tree
Given the root of a binary tree, display the node values at each level.
 Node values for all levels should be displayed on separate lines. Let’s take a look at the below binary tree.

100
50
200
25
75
350
Level order traversal for this tree should look like: 100; 50, 200; 25, 75, 350
'''

def level_order_traversal(root):
  result = ""
  #TODO: Write - Your - Code
  if root is None:
    return result

  queue = [root]
  result += str(root.data) + " "

  while len(queue) != 0:
    size = len(queue)
    for i in range(size):
      node = queue.pop(0)

      if node.left is not None:
        result += str(node.left.data) + " "
        queue.append(node.left)
      if node.right is not None:
        result +=  str(node.right.data) + " "
        queue.append(node.right)
