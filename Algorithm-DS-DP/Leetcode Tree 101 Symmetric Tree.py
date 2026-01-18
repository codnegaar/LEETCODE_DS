'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
        Input: root = [1,2,2,3,4,4,3]
        Output: true
Example 2:
        Input: root = [1,2,2,null,3,null,3]
        Output: false
Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        def dfs_left(root, res):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            dfs_left(root.left, res)
            dfs_left(root.right, res)
            return res
        
        def dfs_right(root, res):
            if root is None: 
                res.append(None)
                return
            res.append(root.val)
            dfs_right(root.right, res)
            dfs_right(root.left, res)
            return res
        
        return dfs_left(root.left, [])==dfs_right(root.right, [])


# Second solution
class Solution(object):
    def isSymmetric(self, root):
        """
        Determines if a binary tree is symmetric around its center.

        Parameters:
        root (TreeNode): The root node of the binary tree.

        Returns:
        bool: True if the binary tree is symmetric, otherwise False.
        """
        # Special case: if the tree is empty, it's symmetric
        if not root:
            return True
        # Check if the left and right subtrees are symmetric
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        """
        Helper function to determine if two subtrees are mirror images of each other.

        Parameters:
        left (TreeNode): The root of the left subtree.
        right (TreeNode): The root of the right subtree.

        Returns:
        bool: True if the two subtrees are mirror images, otherwise False.
        """
        # If both subtrees are empty, they are mirrors
        if not left and not right:
            return True
        # If one subtree is empty and the other is not, they are not mirrors
        if not left or not right:
            return False
        # If the values of the roots are different, they are not mirrors
        if left.val != right.val:
            return False
        # Check if the left subtree of the left tree is a mirror of the right subtree of the right tree
        # and the right subtree of the left tree is a mirror of the left subtree of the right tree
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


# Unit Tests
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_isSymmetric():
    solution = Solution()

    # Test Case 1: Symmetric Tree
    root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert solution.isSymmetric(root1) == True, "Test Case 1 Failed"

    # Test Case 2: Not Symmetric Tree
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert solution.isSymmetric(root2) == False, "Test Case 2 Failed"

    # Test Case 3: Empty Tree
    root3 = None
    assert solution.isSymmetric(root3) == True, "Test Case 3 Failed"

    # Test Case 4: Single Node Tree
    root4 = TreeNode(1)
    assert solution.isSymmetric(root4) == True, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_isSymmetric()

        
