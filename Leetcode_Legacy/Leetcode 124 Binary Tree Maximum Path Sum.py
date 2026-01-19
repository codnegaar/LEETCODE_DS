'''
Leetcode 123 Best Time to Buy and Sell Stock III
 
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
     Input: prices = [3,3,5,0,0,3,1,4]
     Output: 6
     Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
     Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
     
Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple
    transactions at the same time. You must sell before buying again.

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 105
'''


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    sellTwo = 0
    holdTwo = -math.inf
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellTwo = max(sellTwo, holdTwo + price)
      holdTwo = max(holdTwo, sellOne - price)
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellTwo


# Solution II
class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution class to compute the maximum path sum in a binary tree.
    """

    def maxPathSum(self, root: TreeNode) -> int:
        """
        Computes the maximum path sum of any path in a binary tree.
        A path must contain at least one node.

        Parameters:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The maximum path sum of any path in the tree.
        """

        # Initialize the global max path sum as negative infinity
        self.max_sum = float('-inf')

        def max_gain(node):
            """
            Computes the maximum path gain for a given node.

            Parameters:
                node (TreeNode): Current node being processed.

            Returns:
                int: Maximum gain possible from this node's subtree.
            """
            if not node:
                return 0  # Base case: Null nodes contribute nothing
            
            # Compute max path sum from left and right subtrees
            left_gain = max(max_gain(node.left), 0)  # Ignore negative gains
            right_gain = max(max_gain(node.right), 0)

            # New potential max path sum including the current node
            current_path_sum = node.val + left_gain + right_gain

            # Update global max path sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max gain to propagate to the parent
            return node.val + max(left_gain, right_gain)

        # Start DFS recursion from the root
        max_gain(root)
        return self.max_sum


# Helper function to build a binary tree from a level-order list representation
def build_tree(nodes, index=0):
    """
    Builds a binary tree from a list representing level-order traversal.

    Parameters:
        nodes (List[Optional[int]]): Level-order representation of the tree.
        index (int): Current index in the list.

    Returns:
        TreeNode: Root node of the binary tree.
    """
    if index >= len(nodes) or nodes[index] is None:
        return None

    node = TreeNode(nodes[index])
    node.left = build_tree(nodes, 2 * index + 1)
    node.right = build_tree(nodes, 2 * index + 2)
    return node


# Unit tests
def test_maxPathSum():
    solution = Solution()

    test_cases = [
        ([1, 2, 3], 6),  # 2 + 1 + 3 = 6
        ([-10, 9, 20, None, None, 15, 7], 42),  # 15 + 20 + 7 = 42
        ([5], 5),  # Single node tree
        ([1, -2, None, -3, None], 1),  # 1 is the max path
        ([-3, -2, -1], -1)  # -1 is the max path
    ]

    for i, (tree_list, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        assert solution.maxPathSum(root) == expected, f"Test Case {i} Failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_maxPathSum()

