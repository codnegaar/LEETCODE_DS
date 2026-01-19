'''
Leetcode 226 - Invert Binary Tree - Depth First Search
Given the root of a binary tree, invert the tree, and return its root.

Solution
    Runtime complexity: O(N)
    Space complexity: O(N) 

      This problem is quite straightforward. For this algorithm, we will utilize a post order traversal of the binary tree.
      For each node, we will swap its left and right child.

'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None

        # swap the child Nodes
        tmp = root.left
        root.left = root.right 
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# 2nd solution
import unittest
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
    - val (int): The value of the node.
    - left (Optional[TreeNode]): Left child node.
    - right (Optional[TreeNode]): Right child node.
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: Optional['TreeNode']) -> bool:
        """Compares two trees for equality."""
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __repr__(self) -> str:
        """Returns a string representation of the TreeNode for debugging."""
        return f"TreeNode({self.val}, left={self.left}, right={self.right})"


class Solution:
    """
    Provides a method to invert a binary tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping left and right children of each node.

        Args:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - Optional[TreeNode]: The root of the inverted tree.
        """
        if not root:
            return None  # Base case: return if tree is empty

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root  # Return the updated root

 
