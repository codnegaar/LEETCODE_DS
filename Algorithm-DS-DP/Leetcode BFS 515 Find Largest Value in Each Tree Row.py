'''

Leetcode BFS 515 Find the Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each tree row (0-indexed).

Example 1:
        Input: root = [1,3,2,5,3,null,9]
        Output: [1,3,9]

Example 2:
        Input: root = [1,2,3]
        Output: [1,3]
 
Constraints:
        The number of nodes in the tree will be in the range [0, 104].
        -231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root: Optional[TreeNode], depth: int) -> None:
      if not root:
        return
      if depth + 1 > len(ans):
        ans.append(root.val)
      else:
        ans[depth] = max(ans[depth], root.val)

      dfs(root.left, depth + 1)
      dfs(root.right, depth + 1)

    dfs(root, 0)
    return ans

# Second solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            max_level = q[0].val
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                max_level =max(max_level, node.val)

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_level)
        return res

# Third SOlution
from collections import deque
from typing import Optional, List

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Find the largest value in each row of a binary tree.

        Parameters:
        - root: Optional[TreeNode]: Root of the binary tree.

        Returns:
        - List[int]: A list containing the largest value from each row.
        """
        if not root:
            return []  # If the tree is empty, return an empty list.

        res = []  # Result list to store the largest values.
        q = deque([root])  # Queue to perform level-order traversal.

        # Level-order traversal of the binary tree.
        while q:
            max_level = float('-inf')  # Initialize max value for the current level.
            len_q = len(q)  # Number of nodes at the current level.

            # Iterate through all nodes at the current level.
            for _ in range(len_q):
                node = q.popleft()  # Remove the front node from the queue.
                max_level = max(max_level, node.val)  # Update max value.

                # Add left and right children to the queue if they exist.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(max_level)  # Append the maximum value for this level.
        
        return res  # Return the list of largest values.

# Unit Test
if __name__ == "__main__":
    # Constructing the binary tree for testing.
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    solution = Solution()
    print("Test Case 1:", solution.largestValues(root))  # Expected output: [1, 3, 9]

    # Additional test case
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.right = TreeNode(5)

    print("Test Case 2:", solution.largestValues(root2))  # Expected output: [1, 3, 5]



        

