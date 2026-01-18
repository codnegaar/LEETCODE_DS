'''

Leetcode DFS 501 Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
        Input: root = [1,null,2,2]
        Output: [2]

Example 2:
        Input: root = [0]
        Output: [0]
 
Constraints:
        The number of nodes in the tree is in the range [1, 104].
        -105 <= Node.val <= 105

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    self.ans = []
    self.pred = None
    self.count = 0
    self.maxCount = 0

    def updateCount(root: Optional[TreeNode]) -> None:
      if self.pred and self.pred.val == root.val:
        self.count += 1
      else:
        self.count = 1

      if self.count > self.maxCount:
        self.maxCount = self.count
        self.ans = [root.val]
      elif self.count == self.maxCount:
        self.ans.append(root.val)

      self.pred = root

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)
      updateCount(root)
      inorder(root.right)

    inorder(root)
    return self.ans
