"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""


class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def serialize(root):

    if root is None:
        return ""

    msg = f"{root.val}" + ',' + serialize(root.left) + serialize(root.right)

    return msg.strip(",")


def deserialize(s_list):

    if len(s_list) == 0:
        return

    val = s_list.pop(0)

    if s_list is 'X':
        return

    new_node = TreeNode(val)
    new_node.left = deserialize(s_list)
    new_node.right = deserialize(s_list)

    return new_node


# A = TreeNode('A')
# A.left = TreeNode('B')
# A.right = TreeNode('C')
# A.left.left = TreeNode('X')
# A.left.right = TreeNode('D')
A = "A,B,X,D,C"
A_list = A.split(",")

ans = deserialize(A_list)
breakpoint()
print(ans)
