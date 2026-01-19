'''
114 Flatten Binary Tree to Linked List
 
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

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
  def flatten(self, root: Optional[TreeNode]) -> None:
    if not root:
      return

    while root:
      if root.left:
        # Find the rightmost root
        rightmost = root.left
        while rightmost.right:
          rightmost = rightmost.right
        # Rewire the connections
        rightmost.right = root.right
        root.right = root.left
        root.left = None
      # Move on to the right side of the tree
      root = root.right


# Second solution

from typing import Optional, List
import unittest
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """
        Initialize a binary tree node.

        Parameters:
        val (int): The value of the node.
        left (Optional[TreeNode]): The left child of the node.
        right (Optional[TreeNode]): The right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten the binary tree to a linked list in-place following pre-order traversal.

        The flattened tree should use the right pointers to point to the next node in the list,
        and all left pointers should be set to None.

        Parameters:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        None: The tree is modified in-place.
        """
        current = root  # Initialize the current node to root

        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right

                # Rewire the connections:
                # 1. Connect the rightmost node of left subtree to the current node's right subtree
                rightmost.right = current.right
                # 2. Move the left subtree to the right
                current.right = current.left
                # 3. Set the left child to None
                current.left = None
            # Move to the next node in the list
            current = current.right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a list of values. None indicates absence of a node.

    Parameters:
    values (List[Optional[int]]): Level-order traversal list of node values.

    Returns:
    Optional[TreeNode]: The root of the binary tree.
    """
    if not values:
        return None

    iter_vals = iter(values)
    root_val = next(iter_vals)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])

    for val in iter_vals:
        parent = queue.popleft()

        # Assign left child
        if val is not None:
            parent.left = TreeNode(val)
            queue.append(parent.left)
        else:
            parent.left = None

        # Assign right child
        try:
            val = next(iter_vals)
            if val is not None:
                parent.right = TreeNode(val)
                queue.append(parent.right)
            else:
                parent.right = None
        except StopIteration:
            break

    return root

def get_flattened_list(root: Optional[TreeNode]) -> List[int]:
    """
    Extract the flattened list from the right pointers of the tree.

    Parameters:
    root (Optional[TreeNode]): The root of the flattened binary tree.

    Returns:
    List[int]: The list of node values in the flattened tree.
    """
    result = []
    current = root
    while current:
        result.append(current.val)
        if current.left:
            raise ValueError("Left child should be None in flattened tree.")
        current = current.right
    return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        root = None
        self.solution.flatten(root)
        self.assertIsNone(root)

    def test_single_node(self):
        root = TreeNode(1)
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1])

    def test_already_flattened(self):
        # Tree: 1 - 2 - 3 - 4
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1, 2, 3, 4])

    def test_complex_tree(self):
        # Tree structure:
        #      1
        #     / \
        #    2   5
        #   / \   \
        #  3   4   6
        tree_values = [1, 2, 5, 3, 4, None, 6]
        root = build_tree(tree_values)
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1, 2, 3, 4, 5, 6])

    def test_left_skewed_tree(self):
        # Tree: 1 - 2 - 3 - 4 (all left children)
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1, 2, 3, 4])

    def test_right_skewed_tree(self):
        # Tree: 1 - 2 - 3 - 4 (all right children)
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1, 2, 3, 4])

    def test_tree_with_nulls(self):
        # Tree structure:
        #      1
        #     / \
        #    2   5
        #     \   \
        #      3   6
        tree_values = [1, 2, 5, None, 3, None, 6]
        root = build_tree(tree_values)
        self.solution.flatten(root)
        self.assertEqual(get_flattened_list(root), [1, 2, 3, 5, 6])

    def test_large_tree(self):
        # Creating a larger tree for testing
        tree_values = list(range(1, 16))  # Tree with nodes 1 to 15
        root = build_tree(tree_values)
        self.solution.flatten(root)
        expected = list(range(1, 16))
        self.assertEqual(get_flattened_list(root), expected)

    def test_invalid_flattened_tree(self):
        # Ensure that the flatten function sets all left pointers to None
        tree_values = [1, 2, 5, 3, 4, None, 6]
        root = build_tree(tree_values)
        self.solution.flatten(root)
        # Manually introduce a left child after flattening to test validation
        if root and root.right:
            root.right.left = TreeNode(999)
        with self.assertRaises(ValueError):
            get_flattened_list(root)

def print_flattened_tree(root: Optional[TreeNode]) -> None:
    """
    Print the values of the flattened tree.

    Parameters:
    root (Optional[TreeNode]): The root of the flattened binary tree.

    Returns:
    None
    """
    flattened = get_flattened_list(root)
    print("Flattened tree:", flattened)

if __name__ == "__main__":
    # Example Usage
    # Example 1
    # Tree structure:
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    tree_values1 = [1, 2, 5, 3, 4, None, 6]
    root1 = build_tree(tree_values1)

    solution = Solution()
    solution.flatten(root1)

    print_flattened_tree(root1)  # Output: Flattened tree: [1, 2, 3, 4, 5, 6]

    # Example 2
    # Tree structure:
    #     0
    #    /
    #   1
    tree_values2 = [0, 1]
    root2 = build_tree(tree_values2)

    solution.flatten(root2)

    print_flattened_tree(root2)  # Output: Flattened tree: [0, 1]

    # Run Unit Tests
    unittest.main(argv=[''], exit=False)
