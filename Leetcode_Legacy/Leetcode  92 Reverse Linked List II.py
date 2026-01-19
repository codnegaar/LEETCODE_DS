'''

Leetcode 92 Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the 
list from position left to position right, and return the reversed list.


Example 1:    
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]
 

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head and left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next  # Point to the node before the sublist [left, right]

        tail = prev.next  # Will be the tail of the sublist [left, right]

        # Reverse the sublist [left, right] one by one
        for _ in range(right - left):
            cache = tail.next
            tail.next = cache.next
            cache.next = prev.next
            prev.next = cache

        return dummy.next

# second solution:
class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]


# Third Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Reverses a sublist of a linked list between positions left and right.

        Parameters:
        head (ListNode): The head of the singly-linked list.
        left (int): The start position of the sublist to reverse (1-indexed).
        right (int): The end position of the sublist to reverse (1-indexed).
        
        Returns:
        ListNode: The head of the modified linked list.
        """

        # Edge case: if list is empty or no need to reverse (left == right)
        if not head or left == right:
            return head

        # Create a dummy node to simplify boundary conditions when reversing from the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move 'prev' to point to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # 'tail' will be the first node in the sublist that will be reversed
        tail = prev.next

        # Reverse the sublist between 'left' and 'right'
        for _ in range(right - left):
            cache = tail.next  # Cache the next node to be reversed
            # Move the 'cache' node to the front of the sublist
            tail.next = cache.next
            cache.next = prev.next
            prev.next = cache

        # Return the modified list, starting from the real head
        return dummy.next


