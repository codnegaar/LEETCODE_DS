'''
Leetcode 2583 Kth Largest Sum in a Binary Tree

You are given the root of a binary tree and a positive integer k.
The level sum in the tree is the sum of the values of the nodes that are on the same level.
Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
Note that two nodes are on the same level if they have the same distance from the root. 

Example 1:
        Input: root = [5,8,9,2,1,3,7,4,6], k = 2
        Output: 13
        Explanation: The level sums are the following:
        - Level 1: 5.
        - Level 2: 8 + 9 = 17.
        - Level 3: 2 + 1 + 3 + 7 = 13.
        - Level 4: 4 + 6 = 10.
        The 2nd largest level sum is 13.

Example 2:
        Input: root = [1,2,null,3], k = 1
        Output: 3
        Explanation: The largest level sum is 3.
 
Constraints:
        The number of nodes in the tree is n.
        2 <= n <= 105
        1 <= Node.val <= 106
        1 <= k <= n
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        """
        Finds the k-th largest level sum in a binary tree.

        Parameters:
        - root: TreeNode, the root node of the binary tree.
        - k: int, the rank of the largest level sum to return.

        Returns:
        - int, the k-th largest sum of values at any level in the tree.
        - If k is greater than the number of levels, return -1.
        """
        if not root:  # If the tree is empty, return -1
            return -1

        level_sums = []  # To store sum of each level
        queue = deque([root])  # Queue for level-order traversal (BFS)

        # Perform level-order traversal (BFS)
        while queue:
            level_sum = 0  # Sum of node values at the current level
            for _ in range(len(queue)):  # Process all nodes in the current level
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)  # Store the sum of the current level

        # If k is larger than the number of levels, return -1
        if k > len(level_sums):
            return -1

        # Sort sums in descending order and return the k-th largest sum
        level_sums.sort(reverse=True)
        return level_sums[k - 1]  # k is 1-based, so use k-1 for indexing
