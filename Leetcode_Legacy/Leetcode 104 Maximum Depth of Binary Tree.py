'''
Leetcode 104 Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3

Example 2:
        Input: root = [1,null,2]
        Output: 2

Constraints:
        The number of nodes in the tree is in the range [0, 104].
        -100 <= Node.val <= 100

'''
from typing import Optional
from collections import deque
import unittest

class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Computes the maximum depth (height) of a binary tree using BFS.

        Parameters:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        int: The maximum depth of the binary tree.

        Time Complexity: O(n) - Every node is visited once.
        Space Complexity: O(n) - The queue stores nodes at the deepest level.
        """
        if not root:
            return 0  # Base case: If tree is empty, return 0.

        queue = deque([root])
        depth = 0  # Initialize depth

        while queue:
            depth += 1  # Increment depth for each level

            # Process all nodes at the current depth level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)  # Enqueue left child if exists
                if node.right:
                    queue.append(node.right)  # Enqueue right child if exists

        return depth


# Unit Tests
class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        """Sets up test cases with different binary tree structures."""
        self.solution = Solution()

        # Test Case 1: Balanced binary tree
        #        3
        #       / \
        #      9  20
        #         /  \
        #        15   7
        self.root = TreeNode(3)
        self.root.left = TreeNode(9)
        self.root.right = TreeNode(20)
        self.root.right.left = TreeNode(15)
        self.root.right.right = TreeNode(7)

        # Test Case 2: Single node tree
        self.single_node = TreeNode(1)

        # Test Case 3: Left-heavy tree
        #       1
        #      /
        #     2
        #    /
        #   3
        self.left_heavy = TreeNode(1)
        self.left_heavy.left = TreeNode(2)
        self.left_heavy.left.left = TreeNode(3)

        # Test Case 4: Right-heavy tree
        #   1
        #    \
        #     2
        #      \
        #       3
        self.right_heavy = TreeNode(1)
        self.right_heavy.right = TreeNode(2)
        self.right_heavy.right.right = TreeNode(3)

    def test_max_depth(self):
        """Tests the maxDepth function on various trees."""
        self.assertEqual(self.solution.maxDepth(self.root), 3)  # Balanced tree
        self.assertEqual(self.solution.maxDepth(self.single_node), 1)  # Single node
        self.assertEqual(self.solution.maxDepth(None), 0)  # Empty tree
        self.assertEqual(self.solution.maxDepth(self.left_heavy), 3)  # Left-heavy tree
        self.assertEqual(self.solution.maxDepth(self.right_heavy), 3)  # Right-heavy tree

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
