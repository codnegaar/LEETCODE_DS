'''

Leetcode 1669 Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result: Build the result list and return its head.

Example 1:
        Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
        Output: [10,1,13,1000000,1000001,1000002,5]
        Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
        Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
        Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
        Explanation: The blue edges and nodes in the above figure indicate the result.
         
Constraints:
        3 <= list1.length <= 104
        1 <= a <= b < list1.length - 1
        1 <= list2.length <= 104

'''

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize pointers to the start of list1
        prev_a = list1

        # Move prev_a to the node right before the 'a'th node
        for _ in range(a - 1):
            prev_a = prev_a.next

        # Start from prev_a to reach the 'b'th node
        end_b = prev_a
        for _ in range(b - a + 2):  # +2 to move end_b exactly after 'b'th node
            end_b = end_b.next

        # Connect the 'a-1'th node to the start of list2
        prev_a.next = list2

        # Find the end of list2
        while list2.next:
            list2 = list2.next

        # Connect the end of list2 to the node right after 'b'th node
        list2.next = end_b
        
        return list1
