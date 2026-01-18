'''
Leetcode DFS 404 Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 24
        Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
        Input: root = [1]
        Output: 0        

Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -1000 <= Node.val <= 1000
 '''

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # edge case
        if root == None:
            return 0
        
        # regular case
        if root.left == None:
            return self.sumOfLeftLeaves(root.right)

        if root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)




