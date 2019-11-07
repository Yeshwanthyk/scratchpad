"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(root):

    if not root:
        print("no more leaves")
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    depth = 1 + max(left, right)
    return depth


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(7)
root.right.right = TreeNode(11)
root.right.left.right = TreeNode(71)


ans = max_depth(root)
print(ans)
