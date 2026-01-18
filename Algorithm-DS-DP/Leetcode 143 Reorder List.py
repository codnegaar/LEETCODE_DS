'''
Leetcode 143 Reorder List

You are given the head of a singly linked list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
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

        if not head or not head.next or not head.next.next: return

        # Find the middle of the list
        slow, fast=head, head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        # Reverse the second half of the list
        prev=None
        cur=slow.next
        while cur:
            Next=cur.next
            cur.next=prev
            prev=cur
            cur=Next
        slow.next=None

        # Merge the 2 halves
        A, B=head, prev
        while A and B:
            A_next=A.next
            B_next=B.next  

            A.next=B
            B.next=A_next

            A=A_next
            B=B_next    
