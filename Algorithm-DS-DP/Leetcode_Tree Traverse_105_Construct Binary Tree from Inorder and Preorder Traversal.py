
'''
Construct Binary Tree from Preorder and Inorder Traversal


Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]

Example 2:
        Input: preorder = [-1], inorder = [-1]
        Output: [-1]

Constraints:
        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


# Second solution
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from preorder and inorder traversal lists.
        """

        if not preorder or not inorder:
            return None  # Edge case: Empty input

        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # O(n) lookup table
        preorder_iter = iter(preorder)  # Iterator for preorder traversal

        def build_subtree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None  # No valid subtree

            root_val = next(preorder_iter)  # Get root from preorder
            root = TreeNode(root_val)  # Create node

            mid = inorder_map[root_val]  # Get inorder index

            root.left = build_subtree(left, mid - 1)  # Build left subtree
            root.right = build_subtree(mid + 1, right)  # Build right subtree

            return root

        return build_subtree(0, len(inorder) - 1)

