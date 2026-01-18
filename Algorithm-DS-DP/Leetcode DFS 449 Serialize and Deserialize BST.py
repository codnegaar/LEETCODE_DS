'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string 
can be deserialized to the original tree structure. The encoded string should be as compact as possible.

 

Example 1:
        Input: root = [2,1,3]
        Output: [2,1,3]

Example 2:
        Input: root = []
        Output: []
 

Constraints:
        The number of nodes in the tree is in the range [0, 104].
        0 <= Node.val <= 104
        The input tree is guaranteed to be a binary search tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(node):
            if node is None:return []
            return [node.val] + helper(node.left) +       helper(node.right)
        node_vals = helper(root)
        return ",".join(str(val) for val in node_vals)
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:return None
        node_vals = data.split(',')
        node_vals = [int(val) for val in node_vals]
        def helper(node_vals):
            if not node_vals:return None
            root = TreeNode(node_vals[0])
            left_node = helper([val for val in node_vals[1:] if val < node_vals[0]])
            right_node = helper([val for val in node_vals[1:] if val > node_vals[0]])
            root.left = left_node
            root.right = right_node
            return root
        return helper(node_vals)
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
