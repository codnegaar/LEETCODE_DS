'''

2487 Remove Nodes From Linked List

You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.
 

Example 1:
     Input: head = [5,2,13,3,8]
     Output: [13,8]
     Explanation: The nodes that should be removed are 5, 2 and 3.
          - Node 13 is to the right of node 5.
          - Node 13 is to the right of node 2.
          - Node 8 is to the right of node 3.
     
Example 2:
    Input: head = [1,1,1,1]
    Output: [1,1,1,1]
    Explanation: Every node has value 1, so no nodes are removed.
 
Constraints:
    The number of the nodes in the given list is in the range [1, 105].
    1 <= Node.val <= 105

'''

class Solution:
  def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    head.next = self.removeNodes(head.next)
    return head.next if head.next and head.val < head.next.val else head



# second solution
from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursively removes nodes from the linked list where the node's value is 
        less than the value of the next node.

        :param head: The head of the linked list.
        :return: The head of the modified linked list.
        """
        # Base case: If the list is empty or has one node, return the head
        if not head or not head.next:
            return head

        # Recursive step: Process the rest of the list
        head.next = self.removeNodes(head.next)

        # Decide whether to keep the current head or skip it
        if head.next and head.val < head.next.val:
            return head.next  # Skip the current node
        else:
            return head  # Keep the current node

# test case
solution = Solution()
# Creating a list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
result = solution.removeNodes(head)

# Function to print the list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(result)  # Output should be 2 -> 3 -> 1 or similar based on problem constraints

