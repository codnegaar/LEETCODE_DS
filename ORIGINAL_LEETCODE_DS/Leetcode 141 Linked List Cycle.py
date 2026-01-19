'''
Leetcode 141 Linked List Cycle
 
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
        Input: head = [1], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.
 
Constraints:
        The number of the nodes in the list is in the range [0, 104].
        -105 <= Node.val <= 105
        pos is -1 or a valid index in the linked-list.


'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Determine if a linked list has a cycle.
        
        Parameters:
        head (ListNode): The head node of the linked list.

        Returns:
        bool: True if there is a cycle, otherwise False.
        """
        # Initialize two pointers, slow and fast
        slow = fast = head

        # Traverse the list with two pointers
        while fast and fast.next:
            # Move fast by two steps
            fast = fast.next.next
            # Move slow by one step
            slow = slow.next

            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True

        # If we reach here, there's no cycle in the list
        return False

# Time Complexity: O(n) - where n is the number of nodes in the linked list
# Space Complexity: O(1) - no extra space used apart from the pointers

# Improvement:
# Removed unnecessary dummy node initialization. Directly used head as starting points for the slow and fast pointers.
