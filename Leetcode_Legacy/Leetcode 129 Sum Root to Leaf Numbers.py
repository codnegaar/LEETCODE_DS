'''
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123. Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will fit in a 32-bit integer. A leaf node is a node with no children.

Example 1:
        Input: root = [1,2,3]
        Output: 25
        Explanation:
        The root-to-leaf path 1->2 represents the number 12.
        The root-to-leaf path 1->3 represents the number 13.
        Therefore, sum = 12 + 13 = 25.
        
Example 2:
        Input: root = [4,9,0,5,1]
        Output: 1026
        Explanation:
        The root-to-leaf path 4->9->5 represents the number 495.
        The root-to-leaf path 4->9->1 represents the number 491.
        The root-to-leaf path 4->0 represents the number 40.
        Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 9
        The depth of the tree will not exceed 10.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(root: Optional[TreeNode], path: int) -> None:
      nonlocal ans
      if not root:
        return
      if not root.left and not root.right:
        ans += path * 10 + root.val
        return

      dfs(root.left, path * 10 + root.val)
      dfs(root.right, path * 10 + root.val)

    dfs(root, 0)
    return and


# Second solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Calculates the total sum of all root-to-leaf numbers in the binary tree.

        Each root-to-leaf path represents a number, where the digits are the node values
        concatenated together along the path.

        Parameters:
        root (TreeNode): The root node of the binary tree.

        Returns:
        int: The total sum of all root-to-leaf numbers.
        """
        return self.dfs(root, 0)

    def dfs(self, node: TreeNode, num: int) -> int:
        """
        A helper method that performs a depth-first search to calculate the sum.

        Parameters:
        node (TreeNode): The current node being visited.
        num (int): The number formed from the root to the current node.

        Returns:
        int: The cumulative sum of all numbers formed from root to leaf nodes.
        """
        if not node:  # Base case: if the node is None, return 0
            return 0

        # Update the current number formed by adding the node value
        num = num * 10 + node.val

        # If it's a leaf node, return the number formed
        if not node.left and not node.right:
            return num

        # Recursively calculate the sum for left and right subtrees
        left_sum = self.dfs(node.left, num)
        right_sum = self.dfs(node.right, num)
        
        return left_sum + right_sum
import unittest

class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.solution.sumNumbers(root), 25)  # Paths: 12, 13 -> 12 + 13 = 25

    def test_case_2(self):
        root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
        self.assertEqual(self.solution.sumNumbers(root), 1026)  # Paths: 495, 491, 40 -> 495 + 491 + 40 = 1026

    def test_case_3(self):
        root = TreeNode(0)
        self.assertEqual(self.solution.sumNumbers(root), 0)  # Single node, value is 0

    def test_case_4(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution.sumNumbers(root), 123)  # Path: 123

    def test_case_5(self):
        root = None
        self.assertEqual(self.solution.sumNumbers(root), 0)  # Empty tree

if __name__ == "__main__":
    unittest.main()

