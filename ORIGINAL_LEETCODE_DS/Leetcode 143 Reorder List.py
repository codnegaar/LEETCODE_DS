
'''
Leetcode 143 Reorder List
You are given the head of a singly linked-list. The list can be represented as:
L0 ΓåÆ L1 ΓåÆ ΓÇª ΓåÆ Ln - 1 ΓåÆ Ln
Reorder the list to be on the following form:

L0 ΓåÆ Ln ΓåÆ L1 ΓåÆ Ln - 1 ΓåÆ L2 ΓåÆ Ln - 2 ΓåÆ ΓÇª
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]
        
Example 2:
        Input: head = [1,2,3,4,5]
        Output: [1,5,2,4,3]

Constraints:
        The number of nodes in the list is in the range [1, 5 * 104].
        1 <= Node.val <= 1000

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

     
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    def findMid(head: ListNode):
      prev = None
      slow = head
      fast = head

      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None

      return slow

    def reverse(head: ListNode) -> ListNode:
      prev = None
      curr = head

      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

      return prev

    def merge(l1: ListNode, l2: ListNode) -> None:
      while l2:
        next = l1.next
        l1.next = l2
        l1 = l2
        l2 = next

    if not head or not head.next:
      return

    mid = findMid(head)
    reversed = reverse(mid)
    merge(head, reversed)
