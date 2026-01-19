'''
109 Convert Sorted List to Binary Search Tree
 
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
        Input: head = [-10,-3,0,5,9]
        Output: [0,-3,9,-10,null,5]
        Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:
        Input: head = []
        Output: []

Constraints:
        The number of nodes in head is in the range [0, 2 * 104].
        -105 <= Node.val <= 105
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    def helper(l: int, r: int) -> Optional[TreeNode]:
      nonlocal head
      if l > r:
        return None

      m = (l + r) // 2

      # Simulate inorder traversal: recursively form the left half
      left = helper(l, m - 1)

      # Once left half is traversed, process the current node
      root = TreeNode(head.val)
      root.left = left

      # Maintain the invariance
      head = head.next

      # Simulate inorder traversal: recursively form the right half
      root.right = helper(m + 1, r)
      return root

    return helper(0, self._getLength(head) - 1)

  def _getLength(self, head: Optional[ListNode]) -> int:
    length = 0
    curr = head
    while curr:
      length += 1
      curr = curr.next
    return length
