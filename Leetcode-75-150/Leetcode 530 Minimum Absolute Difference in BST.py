'''
530 Minimum Absolute Difference in BST
 
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
        Input: root = [4,2,6,1,3]
        Output: 1
        
Example 2:
        Input: root = [1,0,48,null,null,12,49]
        Output: 1
 
Constraints:
        The number of nodes in the tree is in the range [2, 104].
        0 <= Node.val <= 105
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        min_diff = float('inf')
        
        def inorderTraversal(root):
            nonlocal prev, min_diff
            if not root:
                return
            if root.left:
                inorderTraversal(root.left)
            if (root.val - prev) < min_diff:
                min_diff = root.val - prev
            prev = root.val
            if root.right:
                inorderTraversal(root.right)
                
        inorderTraversal(root)
        return min_diff
