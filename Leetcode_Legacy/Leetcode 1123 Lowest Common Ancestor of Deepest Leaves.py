'''
Leetcode 1123 Lowest Common Ancestor of Deepest Leaves
 
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
Recall that:
The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
 
Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4]
        Output: [2,7,4]
        Explanation: We return the node with value 2, colored in yellow in the diagram.
        The nodes coloured in blue are the deepest leaf-nodes of the tree.
        Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

Example 2:
        Input: root = [1]
        Output: [1]
        Explanation: The root is the deepest node in the tree, and it's the lca of itself.

Example 3:
        Input: root = [0,1,3,null,2]
        Output: [2]
        Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself. 

Constraints:
        The number of nodes in the tree will be in the range [1, 1000].
        0 <= Node.val <= 1000
        The values of the nodes in the tree are unique.
        
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.
        :param val: Value of the node.
        :param left: Left child node.
        :param right: Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root):
        """
        Finds the Lowest Common Ancestor (LCA) of the deepest leaves in a binary tree.

        :param root: Root node of the binary tree.
        :return: TreeNode that is the LCA of the deepest leaves.
        """
        def dfs(node):
            """
            Post-order DFS traversal to determine LCA and depth.

            :param node: Current TreeNode.
            :return: Tuple (LCA TreeNode, max depth under this node).
            """
            if not node:
                return (None, 0)

            # Recursively find LCA and depth of left and right subtrees
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            # Compare depths and determine LCA
            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif right_depth > left_depth:
                return (right_lca, right_depth + 1)
            else:
                # Both sides are equal depth ΓåÆ current node is their LCA
                return (node, left_depth + 1)

        # Extract and return only the LCA node
        lca_node, _ = dfs(root)
        return lca_node
