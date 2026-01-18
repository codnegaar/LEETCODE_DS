'''
102_Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
Example 2:
        Input: root = [1]
        Output: [[1]]
Example 3:
        Input: root = []
        Output: []
 
Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range (qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

# Second solution
from collections import deque
from typing import List, Optional
import unittest

class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level-order traversal (BFS) on a binary tree.

        Parameters:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[List[int]]: A list of lists where each inner list contains values 
                         of nodes at the corresponding level.

        Time Complexity:
        O(n) - Each node is visited once.

        Space Complexity:
        O(n) - The queue can hold at most n nodes.
        """
        if not root:
            return []

        res = []  # Stores values level-wise
        queue = deque([root])  # BFS queue initialized with root node

        while queue:
            level_size = len(queue)  # Nodes at current level
            level_values = []  # List for storing current level values

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue
                level_values.append(node.val)  # Store value

                # Add children to queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_values)  # Append level results

        return res

 
