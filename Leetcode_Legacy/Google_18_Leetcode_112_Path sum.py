'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum. A leaf is a node with no children.

Solution
	Runtime complexity: O(N)
	Space complexity: O(N)


This problem can be solved utilizing a simple linear search algorithm, since we already know that inputs are sorted by
starting timestamps. HereΓÇÖs the approach we will take:
List of input intervals is given, and weΓÇÖll keep merged intervals in the output list. For each interval,If the input 
interval is overlapping with the last interval in the output list, weΓÇÖll merge the two intervals and update the last 
interval of the output list with the merged interval. Otherwise, weΓÇÖll add an input interval to the output list.

'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs (node, curSum):
            if not node:
                return False
            
            curSum += node.val
            
            # if node has no child
            if not node.left and not node.right:
                return curSum == targetSum
            
            # check if the node has child
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        return dfs(root, 0)
	
