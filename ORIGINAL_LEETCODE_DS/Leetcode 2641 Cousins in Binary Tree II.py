'''

Leetcode 2641 Cousins in Binary Tree II

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root node to it.

Example 1:
        Input: root = [5,4,9,1,10,null,7]
        Output: [0,0,0,7,7,null,11]
        Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
        - Node with value 5 does not have any cousins so its sum is 0.
        - Node with value 4 does not have any cousins so its sum is 0.
        - Node with value 9 does not have any cousins so its sum is 0.
        - Node with value 1 has a cousin with value 7 so its sum is 7.
        - Node with value 10 has a cousin with value 7 so its sum is 7.
        - Node with value 7 has cousins with values 1 and 10 so its sum is 11.

Example 2:
        Input: root = [3,1,2]
        Output: [0,0,0]
        Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
        - Node with value 3 does not have any cousins so its sum is 0.
        - Node with value 1 does not have any cousins so its sum is 0.
        - Node with value 2 does not have any cousins so its sum is 0.

Constraints:
        The number of nodes in the tree is in the range [1, 105].
        1 <= Node.val <= 104

'''

class Solution:
    def replaceValueInTree(self, root):
        # Helper function to calculate the sum of children for nodes at the current level
        def calculate_level_sum(nodes):
            total_sum = 0
            for node in nodes:
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val
            return total_sum

        # Helper function to update children values for nodes at the current level
        def update_children_values(nodes, total_sum):
            next_level_nodes = []
            for node in nodes:
                # Calculate the sum of children values for the current node
                current_sum = 0
                if node.left:
                    current_sum += node.left.val
                if node.right:
                    current_sum += node.right.val

                # Update left child value
                if node.left:
                    node.left.val = total_sum - current_sum
                    next_level_nodes.append(node.left)

                # Update right child value
                if node.right:
                    node.right.val = total_sum - current_sum
                    next_level_nodes.append(node.right)

            return next_level_nodes

        # Main function logic using DFS to traverse each level
        def dfs_level_order(root_node):
            current_level_nodes = [root_node]
            while current_level_nodes:
                # Calculate the total sum of all child nodes for the current level
                total_sum = calculate_level_sum(current_level_nodes)
                # Update child nodes' values and move to the next level
                current_level_nodes = update_children_values(current_level_nodes, total_sum)

        # Initialize root value to 0 as per the requirement
        root.val = 0
        dfs_level_order(root)
        return root

# Example usage
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# Solution().replaceValueInTree(root) - The function will modify the tree in place.
# The root value is set to 0, and other nodes are updated according to the logic.
