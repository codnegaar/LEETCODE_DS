'''

103 Binary Tree Zigzag Level Order Traversal
Medium
8K
209
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 

class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])
    isLeftToRight = True

    while q:
      size = len(q)
      currLevel = [0] * size
      for i in range(size):
        node = q.popleft()
        index = i if isLeftToRight else size - i - 1
        currLevel[index] = node.val
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      ans.append(currLevel)
      isLeftToRight = not isLeftToRight

    return ans

# Second solution

from queue import Queue
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a binary tree node.

        Parameters:
        - val: int: Value of the node.
        - left: Optional[TreeNode]: Reference to the left child.
        - right: Optional[TreeNode]: Reference to the right child.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, A: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform zigzag level-order traversal of a binary tree.

        Parameters:
        - A: Optional[TreeNode]: Root of the binary tree.

        Returns:
        - List[List[int]]: A list of lists where each inner list contains the node values 
          for that level, ordered in zigzag (alternating) order.
        """
        if not A:
            return []  # If the tree is empty, return an empty list.

        queue = Queue()  # Queue for level-order traversal.
        queue.put(A)
        output = []  # Final output list.
        level = 0  # Track the current level to determine zigzag direction.

        # Perform level-order traversal.
        while not queue.empty():
            size = queue.qsize()  # Number of nodes at the current level.
            curr = []  # List to store current level's node values.

            # Process all nodes in the current level.
            for _ in range(size):
                temp = queue.get()  # Get the next node from the queue.

                # Append node value to current level's list based on the level's parity.
                if level % 2 == 0:
                    curr.append(temp.val)  # Left-to-right for even levels.
                else:
                    curr.insert(0, temp.val)  # Right-to-left for odd levels.

                # Add child nodes to the queue for the next level.
                if temp.left:
                    queue.put(temp.left)
                if temp.right:
                    queue.put(temp.right)

            output.append(curr)  # Add the current level's values to the output.
            level += 1  # Increment the level.

        return output  # Return the zigzag level-order traversal.

# Example Usage
if __name__ == "__main__":
    # Constructing a binary tree for testing.
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print("Zigzag Level Order Traversal:", solution.zigzagLevelOrder(root))
    # Expected output: [[3], [20, 9], [15, 7]]

