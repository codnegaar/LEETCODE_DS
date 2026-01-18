'''
Leetcode 75-Binary Tree - DFS 104 Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node. 

Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
Example 2:
        Input: root = [1, null, 2]
        Output: 2
Constraints:
        The number of nodes in the tree is in the range [0, 104].
        -100 <= Node.val <= 100

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

# Second Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))                       
        return dfs(root, 0)
        
# Second Solution
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.

        Parameters:
        root (TreeNode): The root node of the binary tree.

        Returns:
        int: The maximum depth of the binary tree.
        """
        if not root:
            return 0  # If the tree is empty, return 0 as the depth

        # Use a queue to facilitate level-order traversal
        q = deque([root])
        depth = 0

        # Iterate while there are nodes in the queue
        while q:
            depth += 1  # Increment depth with each level

            # Iterate through all nodes at the current level
            for _ in range(len(q)):
                node = q.popleft()  # Remove node from the front of the queue
                if node.left:
                    q.append(node.left)  # Add left child to the queue if it exists
                if node.right:
                    q.append(node.right)  # Add right child to the queue if it exists

        return depth

# Unit Test for the Solution
import unittest

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        # Create a binary tree for testing:
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

    def test_max_depth(self):
        solution = Solution()
        self.assertEqual(solution.maxDepth(self.root), 3)  # Expected depth is 3

    def test_empty_tree(self):
        solution = Solution()
        self.assertEqual(solution.maxDepth(None), 0)  # Expected depth for empty tree is 0

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
