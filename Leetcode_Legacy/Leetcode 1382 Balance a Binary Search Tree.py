'''

Leetcode 1382 balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:
        Input: root = [1,null,2,null,3,null,4,null,null]
        Output: [2,1,3,null,null,null,4]
        Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
        Input: root = [2,1,3]
        Output: [2,1,3] 

Constraints:
        The number of nodes in the tree is in the range [1, 104].
        1 <= Node.val <= 105

'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_nodes = []
        self._inorder_traverse(root, sorted_nodes)
        return self._sorted_array_to_bst(sorted_nodes, 0, len(sorted_nodes) - 1)

    def _inorder_traverse(self, node: TreeNode, sorted_nodes: List[TreeNode]) -> None:
        if not node:
            return
        self._inorder_traverse(node.left, sorted_nodes)
        sorted_nodes.append(node)
        self._inorder_traverse(node.right, sorted_nodes)

    def _sorted_array_to_bst(self, sorted_nodes: List[TreeNode], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        root = sorted_nodes[mid]
        root.left = self._sorted_array_to_bst(sorted_nodes, start, mid - 1)
        root.right = self._sorted_array_to_bst(sorted_nodes, mid + 1, end)
        return root
