'''
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:
        Input: root = [5,3,6,2,4,null,7], k = 9
        Output: true

Example 2:
        Input: root = [5,3,6,2,4,null,7], k = 28
        Output: false
 
Constraints:
        The number of nodes in the tree is in the range [1, 104].
        -104 <= Node.val <= 104
        root is guaranteed to be a valid binary search tree.
        -105 <= k <= 105

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
  def __init__(self, root: Optional[TreeNode], leftToRight: bool):
    self.stack = []
    self.leftToRight = leftToRight
    self._pushUntilNone(root)

  def next(self) -> int:
    node = self.stack.pop()
    if self.leftToRight:
      self._pushUntilNone(node.right)
    else:
      self._pushUntilNone(node.left)
    return node.val

  def _pushUntilNone(self, root: Optional[TreeNode]):
    while root:
      self.stack.append(root)
      root = root.left if self.leftToRight else root.right


class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    if not root:
      return False

    left = BSTIterator(root, True)
    right = BSTIterator(root, False)

    l = left.next()
    r = right.next()
    while l < r:
      summ = l + r
      if summ == k:
        return True
      if summ < k:
        l = left.next()
      else:
        r = right.next()

    return False


