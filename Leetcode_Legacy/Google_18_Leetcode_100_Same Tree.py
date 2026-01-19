'''
7. Check if two binary trees are identical
Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same 
if they are structurally identical, and the nodes have the same value.

solution:
 
Runtime complexity: O(N)
Space complexity: O(N)
 

This problem can be tackled using recursion. The base case of the recursive solution would be when both nodes being compared are null or one of them is null.

Two trees being compared are identical if:

data on their roots is the same
the left sub-tree of ΓÇÿAΓÇÖ is identify to the left sub-tree of ΓÇÿBΓÇÖ
the right sub-tree of ΓÇÿAΓÇÖ is identical to the right sub-tree of ΓÇÿBΓÇÖ
Using recursion, we can solve this problem through a depth-first traversal on both trees simultaneously while comparing the data at each node.


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p  and not q:
            return True
        if not p  or not q or p.val !=q.val:
	        return False
        
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
               
