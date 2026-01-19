'''
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
        Input: head = [4,2,1,3]
        Output: [1,2,3,4]

Example 2:
        Input: head = [-1,5,3,4,0]
        Output: [-1,0,3,4,5]

Example 3:
        Input: head = []
        Output: []

Constraints:
        The number of nodes in the list is in the range [0, 5 * 104].
        -105 <= Node.val <= 105
''' 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def sortList(self, head: ListNode) -> ListNode:
    def split(head: ListNode, k: int) -> ListNode:
      while k > 1 and head:
        head = head.next
        k -= 1
      rest = head.next if head else None
      if head:
        head.next = None
      return rest

    def merge(l1: ListNode, l2: ListNode) -> tuple:
      dummy = ListNode(0)
      tail = dummy

      while l1 and l2:
        if l1.val > l2.val:
          l1, l2 = l2, l1
        tail.next = l1
        l1 = l1.next
        tail = tail.next
      tail.next = l1 if l1 else l2
      while tail.next:
        tail = tail.next

      return dummy.next, tail

    length = 0
    curr = head
    while curr:
      length += 1
      curr = curr.next

    dummy = ListNode(0, head)

    k = 1
    while k < length:
      curr = dummy.next
      tail = dummy
      while curr:
        l = curr
        r = split(l, k)
        curr = split(r, k)
        mergedHead, mergedTail = merge(l, r)
        tail.next = mergedHead
        tail = mergedTail
      k *= 2

    return dummy.next

# Second solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        Sorts a singly linked list in ascending order using Merge Sort.
        """
        def split(head: ListNode, k: int) -> ListNode:
            """
            Splits the list into two parts after `k` nodes.
            Returns the second part of the split list.
            """
            while k > 1 and head:
                head = head.next
                k -= 1
            rest = head.next if head else None
            if head:
                head.next = None
            return rest

        def merge(l1: ListNode, l2: ListNode) -> tuple:
            """
            Merges two sorted linked lists.
            Returns the head and tail of the merged list.
            """
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next

            return dummy.next, tail

        # Calculate the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Iterative merge sort using bottom-up approach
        dummy = ListNode(0, head)
        k = 1
        while k < length:
            curr = dummy.next
            tail = dummy
            while curr:
                l = curr
                r = split(l, k)
                curr = split(r, k)
                mergedHead, mergedTail = merge(l, r)
                tail.next = mergedHead
                tail = mergedTail
            k *= 2

        return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(arr):
    """
    Converts a Python list into a singly linked list.
    """
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    """
    Prints the elements of a singly linked list as a Python list.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# Example usage
if __name__ == "__main__":
    head = create_linked_list([4, 2, 1, 3])
    solution = Solution()
    sorted_head = solution.sortList(head)
    print_linked_list(sorted_head)  # Output: [1, 2, 3, 4]

