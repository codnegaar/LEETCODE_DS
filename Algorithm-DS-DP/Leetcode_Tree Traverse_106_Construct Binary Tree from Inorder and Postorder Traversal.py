'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the 
postorder traversal of the same tree, construct and return the binary tree.

Example 1:
        Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        Output: [3,9,20,null,null,15,7]
Example 2:
       Input: inorder = [-1], postorder = [-1]
       Output: [-1]

Constraints:
          1 <= inorder.length <= 3000
          postorder.length == inorder.length
          -3000 <= inorder[i], postorder[i] <= 3000
          inorder and postorder consist of unique values.
          Each value of postorder also appears in inorder.
          inorder is guaranteed to be the inorder traversal of the tree.
          postorder is guaranteed to be the postorder traversal of the tree.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i
            
        def rec(low, high):
            if low > high:
                return

            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = rec(mid+1, high)
            root.left = rec(low, mid-1)
            return root
            
        return rec(0, len(inorder)-1)

# Second solution
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode object.

        Args:
        - val (int): The value of the node.
        - left (TreeNode): Left child node.
        - right (TreeNode): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from its inorder and postorder traversal.

        Args:
        - inorder (List[int]): Inorder traversal of the binary tree.
        - postorder (List[int]): Postorder traversal of the binary tree.

        Returns:
        - TreeNode: Root of the reconstructed binary tree.
        """

        # Create a mapping of values to their indices in the inorder list
        value_to_index = {val: idx for idx, val in enumerate(inorder)}

        def construct_tree(low: int, high: int) -> Optional[TreeNode]:
            """
            Recursive helper function to construct the binary tree.

            Args:
            - low (int): Start index of the current inorder segment.
            - high (int): End index of the current inorder segment.

            Returns:
            - TreeNode: Root of the subtree constructed from the segment.
            """
            if low > high:  # Base case: invalid segment
                return None

            # The last element in postorder is the root of the current subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Find the index of the root value in the inorder traversal
            mid = value_to_index[root_val]

            # Construct the right and left subtrees recursively
            root.right = construct_tree(mid + 1, high)  # Build right subtree
            root.left = construct_tree(low, mid - 1)   # Build left subtree

            return root

        # Start the recursive construction from the full range of inorder traversal
        return construct_tree(0, len(inorder) - 1)


# Unit Test
if __name__ == "__main__":
    def print_tree(root: TreeNode):
        """Helper function to print the tree in level-order for testing."""
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values for cleaner output
        while result and result[-1] is None:
            result.pop()
        return result

    # Test case 1
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution = Solution()
    tree = solution.buildTree(inorder, postorder)
    print(print_tree(tree))  # Expected output: [3, 9, 20, None, None, 15, 7]

    # Test case 2
    inorder = [2, 1]
    postorder = [2, 1]
    tree = solution.buildTree(inorder, postorder)
    print(print_tree(tree))  # Expected output: [1, 2]



