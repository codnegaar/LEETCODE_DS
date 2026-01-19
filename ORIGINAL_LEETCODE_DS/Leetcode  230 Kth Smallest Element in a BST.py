'''

230 Kth Smallest Element in a BST
 
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1
        
Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3

Constraints:
        The number of nodes in the tree is n.
        1 <= k <= n <= 104
        0 <= Node.val <= 104 
 '''
 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def countNodes(root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      return 1 + countNodes(root.left) + countNodes(root.right)

    leftCount = countNodes(root.left)

    if leftCount == k - 1:
      return root.val
    if leftCount >= k:
      return self.kthSmallest(root.left, k)
    return self.kthSmallest(root.right, k - 1 - leftCount)  # LeftCount < k

# new solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Finds the kth smallest element in a Binary Search Tree (BST).

        Parameters:
        root (TreeNode): The root of the BST.
        k (int): The position (1-based index) of the smallest element to be found.

        Returns:
        int: The value of the k-th smallest element.
        """
        # Initialize an empty stack to simulate the recursion for in-order traversal.
        stack = []
        cur = root
        n = 0  # To keep track of the number of nodes visited

        # Traverse the BST in an in-order fashion iteratively.
        while cur or stack:
            # Reach the leftmost node of the current node.
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Pop the node at the top of the stack.
            cur = stack.pop()
            n += 1

            # If we have visited `k` nodes, then this is the k-th smallest element.
            if n == k:
                return cur.val
            
            # Move to the right subtree.
            cur = cur.right
