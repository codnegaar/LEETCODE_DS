
'''
You are given the head of a linked list and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
        Input: head = [1,2,3,4,5], k = 2
        Output: [1,4,3,2,5]

Example 2:
        Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
        Output: [7,9,6,6,8,7,3,0,9,5]
 
Constraints:
        The number of nodes in the list is n.
        1 <= k <= n <= 105
        0 <= Node.val <= 100

'''
class Solution:
  def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    p = None  # Points k-th node from the beginning.
    q = None  # Points k-th node from the end.

    curr = head
    while curr:
      if q:
        q = q.next
      k -= 1
      if k == 0:
        p = curr
        q = head
      curr = curr.next

    p.val, q.val = q.val, p.val
    return head
