'''
Leetcode 1261 Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:
root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
Implement the FindElements class:
FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 
Example 1:
          Input
          ["FindElements","find","find"]
          [[[-1,null,-1]],[1],[2]]
          Output
          [null,false,true]
          Explanation
          FindElements findElements = new FindElements([-1,null,-1]); 
          findElements.find(1); // return False 
          findElements.find(2); // return True 

Example 2:
        Input
        ["FindElements","find","find","find"]
        [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
        Output
        [null,true,true,false]
        Explanation
        FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
        findElements.find(1); // return True
        findElements.find(3); // return True
        findElements.find(5); // return False

Example 3:
        Input
        ["FindElements","find","find","find","find"]
        [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
        Output
        [null,true,false,false,true]
        Explanation
        FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
        findElements.find(2); // return True
        findElements.find(3); // return False
        findElements.find(4); // return False
        findElements.find(5); // return True
 

Constraints:
        TreeNode.val == -1
        The height of the binary tree is less than or equal to 20
        The total number of nodes is between [1, 104]
        Total calls of find() is between [1, 104]
        0 <= target <= 106

'''

from typing import Optional, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    """
    A class that reconstructs a contaminated binary tree and allows querying 
    whether a specific target value exists in the tree.
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the FindElements object by reconstructing the tree.

        :param root: The root of the contaminated binary tree with all values set to -1.
        """
        self.seen: Set[int] = set()  # A set to store all valid node values for O(1) lookup

        def dfs(node: TreeNode, val: int):
            """
            Depth-first search to reconstruct the tree with correct values.

            :param node: Current tree node being processed.
            :param val: The correct value of the current node.
            """
            if not node:
                return

            node.val = val  # Assign the correct value to the node
            self.seen.add(val)  # Store the value in the set for quick lookup

            # Recursively assign values to left and right children
            dfs(node.left, 2 * val + 1)  # Left child formula
            dfs(node.right, 2 * val + 2)  # Right child formula

        # Start tree recovery from the root, setting its value to 0
        if root:
            dfs(root, 0)

    def find(self, target: int) -> bool:
        """
        Checks if a given target value exists in the reconstructed tree.

        :param target: The value to check for existence in the tree.
        :return: True if target exists, otherwise False.
        """
        return target in self.seen  # O(1) lookup time

# Example of usage
if __name__ == "__main__":
    # Constructing a contaminated tree (all values originally -1)
    root = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))

    # Initialize FindElements class with the contaminated tree
    obj = FindElements(root)

    # Example queries
    print(obj.find(1))  # Output: True (if 1 is in the tree)
    print(obj.find(5))  # Output: False (if 5 is not in the tree)


