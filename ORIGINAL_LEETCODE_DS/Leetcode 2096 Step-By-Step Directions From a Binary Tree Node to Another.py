'''
Leetcode 2096 Step-By-Step Directions From a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:        
        'L' means to go from a node to its left child node.
        'R' means to go from a node to its right child node.
        'U' means to go from a node to its parent node.
        Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:        
        Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
        Output: "UURL"
        Explanation: The shortest path is: 3 ΓåÆ 1 ΓåÆ 5 ΓåÆ 2 ΓåÆ 6.

Example 2:
        Input: root = [2,1], startValue = 2, destValue = 1
        Output: "L"
        Explanation: The shortest path is: 2 ΓåÆ 1.
 
Constraints:
        The number of nodes in the tree is n.
        2 <= n <= 105
        1 <= Node.val <= n
        All the values in the tree are unique.
        1 <= startValue, destValue <= n
        startValue != destValue

'''



from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find(node: TreeNode, val: int) -> str:
            if node.val == val:
                return ""
            if node.left:
                left_path = find(node.left, val)
                if left_path is not None:
                    return "L" + left_path
            if node.right:
                right_path = find(node.right, val)
                if right_path is not None:
                    return "R" + right_path
            return None
        
        # Find paths from root to startValue and destValue
        s_path = find(root, startValue)
        d_path = find(root, destValue)
        
        # Remove the common prefix
        i = 0
        while i < len(s_path) and i < len(d_path) and s_path[i] == d_path[i]:
            i += 1
        
        # Construct the result
        return "U" * (len(s_path) - i) + d_path[i:]
