'''
Leetcode 2471 Minimum Number of Operations to Sort a Binary Tree by Level
 
You are given the root of a binary tree with unique values.
In one operation, you can choose any two nodes at the same level and swap their values.
Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
The level of a node is the number of edges along the path between it and the root node. 

Example 1:
        Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
        Output: 3
        Explanation:
        - Swap 4 and 3. The 2nd level becomes [3,4].
        - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
        - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
        We used 3 operations so return 3.
        It can be proven that 3 is the minimum number of operations needed.

Example 2:
        Input: root = [1,3,2,7,6,5,4]
        Output: 3
        Explanation:
        - Swap 3 and 2. The 2nd level becomes [2,3].
        - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
        - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
        We used 3 operations so return 3.
        It can be proven that 3 is the minimum number of operations needed.

Example 3:
        Input: root = [1,2,3,4,5,6]
        Output: 0
        Explanation: Each level is already sorted in increasing order so return 0.
         
Constraints:
        The number of nodes in the tree is in the range [1, 105].
        1 <= Node.val <= 105
        All the values of the tree are unique.

'''

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the minimum number of operations to sort the level-wise values of a binary tree.
        
        Parameters:
        root (TreeNode): The root of the binary tree.
        
        Returns:
        int: Minimum number of operations required to sort the tree level-wise.
        """
        if not root:
            return 0  # If the tree is empty, no operations are needed.

        # Initialize variables: `ans` for counting operations, and `queue` for BFS traversal.
        ans = 0
        queue = deque([root])

        while queue:
            # Extract all nodes at the current level.
            level = [node.val for node in queue if node]
            
            # Track the indices to determine the sort operation order.
            indexed = [(val, i) for i, val in enumerate(level)]
            sorted_indices = [i for _, i in sorted(indexed)]  # Indices after sorting by value.

            # Calculate the minimum swaps to sort this level.
            for i in range(len(sorted_indices)):
                while sorted_indices[i] != i:  # Perform swaps to resolve indices.
                    j = sorted_indices[i]
                    sorted_indices[i], sorted_indices[j] = sorted_indices[j], sorted_indices[i]
                    ans += 1  # Increment operation count for each swap.

            # Add the next level's children to the queue.
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans

# Unit Test
def test_minimum_operations():
    """
    Test the Solution.minimumOperations function with example cases.
    """
    # Example 1: Test case from prompt
    root = TreeNode(1,
                    TreeNode(4, TreeNode(7), TreeNode(6, TreeNode(11))),
                    TreeNode(3, TreeNode(8, TreeNode(9)), TreeNode(5, TreeNode(10))))
    sol = Solution()
    assert sol.minimumOperations(root) == 5, "Test Case 1 Failed"

    # Example 2: Simple single-level tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.minimumOperations(root) == 0, "Test Case 2 Failed"

    # Example 3: Tree with multiple unsorted levels
    root = TreeNode(1,
                    TreeNode(3, TreeNode(5), TreeNode(4)),
                    TreeNode(2, TreeNode(6), TreeNode(7)))
    assert sol.minimumOperations(root) == 2, "Test Case 3 Failed"  # Updated from 3 to 2

    print("All test cases passed!")

# Run the test
test_minimum_operations()
