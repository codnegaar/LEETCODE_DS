'''

Leetcode 1110 Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
        Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
        Output: [[1,2,null,4],[6],[7]]
        
Example 2:
        Input: root = [1,2,4,null,3], to_delete = [3]
        Output: [[1,2,4]] 

Constraints:
        The number of nodes in the given tree is at most 1000.
        Each node has a distinct value between 1 and 1000.
        to_delete.length <= 1000
        to_delete contains distinct values between 1 and 1000.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert to set for O(1) lookup
        forest = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            # Check if current node needs to be deleted
            is_deleted = node.val in to_delete_set
            
            # If this is a root node and not deleted, add it to the forest
            if is_root and not is_deleted:
                forest.append(node)
            
            # Recursively process the left and right children
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            
            # Return None if the node is deleted, otherwise return the node itself
            return None if is_deleted else node
        
        dfs(root, True)
        return forest
