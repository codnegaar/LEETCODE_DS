'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

Example 2:
        Input: head = [1], n = 1
        Output: []

Example 3:
        Input: head = [1,2], n = 1
        Output: [1]
 

Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz 

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)        
        l, r = dummyNode, head
        
        while n> 0 and r:
            r=r.next
            n -=1
            
        while r:
            l=l.next
            r=r.next
        
        # Delete the node after being find
        l.next=l.next.next
        return dummyNode.next   
            
            
        
        
        
        
