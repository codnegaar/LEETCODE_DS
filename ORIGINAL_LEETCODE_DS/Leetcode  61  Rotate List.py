'''
61 - Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]
        
Example 2:
        Input: head = [0,1,2], k = 4
        Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head  # Circle the list

        t = length - k % length
        for _ in range(t):
            tail = tail.next
        newHead = tail.next
        tail.next = None

        return newHead

# Second Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotates the linked list to the right by k places.
        
        Parameters:
        head (ListNode): The head node of the linked list.
        k (int): The number of places to rotate the list.
        
        Returns:
        ListNode: The new head of the rotated linked list.
        """
        
        # Edge case: If the list is empty or has one element, no rotation is needed
        if not head or not head.next:
            return head
        
        # Step 1: Find the length of the linked list and connect the tail to the head
        # to form a circular linked list
        n = 1  # The list has at least one element
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: If k is a multiple of n, the list remains unchanged
        k %= n  # Avoid unnecessary rotations if k >= n

        # Edge case: If k is 0 after modulo, no rotation is needed
        if k == 0:
            return head
        
        # Step 3: Find the new tail (n - k - 1) and the new head (n - k)
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
        
        # Step 4: Set the new head and break the circular link
        new_head = new_tail.next
        new_tail.next = None
        
        # Step 5: Connect the old tail to the old head to complete the rotation
        tail.next = head
        
        return new_head

# Example Unit Test:
def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Rotate the list by 2 places
solution = Solution()
rotated_head = solution.rotateRight(head, 2)

# Output the rotated list: 4 -> 5 -> 1 -> 2 -> 3
print_list(rotated_head)

