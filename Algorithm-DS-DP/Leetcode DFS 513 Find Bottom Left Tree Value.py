'''
Leetcode DFS 513 Find Bottom Left Tree Value.py

Given the root of a binary tree, return the leftmost value in the last row of the tree. 

Example 1:
        Input: root = [2,1,3]
        Output: 1

Example 2:
        Input: root = [1, 2, 3, 4, null, 5, 6, null, null, 7]
        Output: 7
         
Constraints:
        The number of nodes in the tree is in the range [1, 104].
        -231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    q = collections.deque([root])

    while q:
      root = q.popleft()
      if root.right:
        q.append(root.right)
      if root.left:
        q.append(root.left)

    return root.val

        
