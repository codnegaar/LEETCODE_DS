'''
1290 Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

Example 1:
        Input: head = [1,0,1]
        Output: 5
        Explanation: (101) in base 2 = (5) in base 10

Example 2:
        Input: head = [0]
        Output: 0
 
Constraints:
        The Linked List is not empty.
        Number of nodes will not exceed 30.
        Each node's value is either 0 or 1.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    ans = 0

    while head:
      ans = ans * 2 + head.val
      head = head.next

    return ans



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initializes a node in a singly linked list.

        Parameters:
        val (int): Binary digit (0 or 1).
        next (ListNode): Reference to the next node in the list.
        """
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Convert a binary number represented as a linked list to a decimal integer.

        Parameters:
        head (ListNode): Head node of the singly linked list.

        Returns:
        int: Decimal integer representation of the binary number.
        """
        result = 0  # Initialize result to hold the decimal value

        while head:
            result = (result << 1) | head.val  # Left shift result by 1 and add current node's value
            head = head.next  # Move to the next node

        return result


# Example usage
if __name__ == "__main__":
    # Linked list: 1 -> 0 -> 1 (binary 101 => decimal 5)
    node3 = ListNode(1)
    node2 = ListNode(0, next=node3)
    node1 = ListNode(1, next=node2)
    
    solution = Solution()
    print("Decimal Value:", solution.getDecimalValue(node1))  # Output: 5


# Unit test
import unittest

class TestGetDecimalValue(unittest.TestCase):
    def test_example_case(self):
        # Input: 1 -> 0 -> 1, Expected Output: 5
        head = ListNode(1, ListNode(0, ListNode(1)))
        self.assertEqual(Solution().getDecimalValue(head), 5)

    def test_single_node(self):
        # Input: 1, Expected Output: 1
        head = ListNode(1)
        self.assertEqual(Solution().getDecimalValue(head), 1)

    def test_all_zeros(self):
        # Input: 0 -> 0 -> 0, Expected Output: 0
        head = ListNode(0, ListNode(0, ListNode(0)))
        self.assertEqual(Solution().getDecimalValue(head), 0)

    def test_leading_zeros(self):
        # Input: 0 -> 1 -> 1, Expected Output: 3
        head = ListNode(0, ListNode(1, ListNode(1)))
        self.assertEqual(Solution().getDecimalValue(head), 3)

# To run tests, uncomment the following:
# if __name__ == "__main__":
#     unittest.main()


"""
Changes made:
- Added docstrings to all classes and methods
- Added inline comments to explain each operation
- Simplified and optimized binary conversion using bitwise operations (<< and |)
- Provided an example usage scenario
- Added a comprehensive unit test class with multiple test cases

Reference:
- Bitwise operations in Python: https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
"""
