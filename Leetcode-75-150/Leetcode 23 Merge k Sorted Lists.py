'''
Leetcode 23 Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
          Input: lists = [[1,4,5],[1,3,4],[2,6]]
          Output: [1,1,2,3,4,4,5,6]
          Explanation: The linked-lists are:
          [
            1->4->5,
            1->3->4,
            2->6
          ]
          merging them into one sorted list:
          1->1->2->3->4->4->5->6

Example 2:        
        Input: lists = []
        Output: []

Example 3:        
        Input: lists = [[]]
        Output: []
 

Constraints:        
        k == lists.length
        0 <= k <= 104
        0 <= lists[i].length <= 500
        -104 <= lists[i][j] <= 104
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 104.
'''

from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy node to simplify merging
        dummy = ListNode()
        current = dummy
        heap = []

        # Push the head of each non-empty list into the heap
        for index, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, index, lst))  # (value, index, node)

        # Process the heap until it is empty
        while heap:
            _, index, node = heappop(heap)
            current.next = node  # Add the smallest node to the merged list
            current = current.next
            if node.next:  # Push the next node from the same list into the heap
                heappush(heap, (node.next.val, index, node.next))

        return dummy.next
