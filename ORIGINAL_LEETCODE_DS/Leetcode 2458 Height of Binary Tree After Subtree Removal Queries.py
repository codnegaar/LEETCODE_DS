'''
Leetcode 2458 Height of Binary Tree After Subtree Removal Queries

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.
You have to perform m independent queries on the tree where in the ith query you do the following:
        Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
        Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.
Note:
        The queries are independent, so the tree returns to its initial state after each query.
        The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.         

Example 1:
        Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
        Output: [2]
        Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
        The height of the tree is 2 (The path 1 -> 3 -> 2).

Example 2:
        Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
        Output: [3,2,3,2]
        Explanation: We have the following queries:
        - Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
        - Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
        - Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
        - Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
         

Constraints:
        The number of nodes in the tree is n.
        2 <= n <= 105
        1 <= Node.val <= n
        All the values in the tree are unique.
        m == queries.length
        1 <= m <= min(n, 104)
        1 <= queries[i] <= n
        queries[i] != root.val

'''

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        Function to calculate the maximum height of the tree when each node is removed.
        
        Parameters:
        root (Optional[TreeNode]): The root of the binary tree.
        queries (List[int]): A list of node values for which we want to find the maximum possible height if that node is removed.
        
        Returns:
        List[int]: A list of integers representing the maximum height of the tree for each query node removed.
        """
        # Dictionary to store the maximum height of the other subtree when a particular node is removed.
        height_dict = defaultdict(int)

        # Helper function to calculate the height of the tree and populate height_dict with sibling subtree heights.
        def calculate_height(node, height):
            """
            Helper function to calculate the height of the tree and populate height_dict with sibling subtree heights.
            
            Parameters:
            node (Optional[TreeNode]): The current node being processed.
            height (int): The current height of the tree.
            
            Returns:
            int: The maximum height of the current subtree.
            """
            if not node:
                return height - 1
            
            # Recursively calculate left and right subtree heights.
            left_height = calculate_height(node.left, height + 1)
            right_height = calculate_height(node.right, height + 1)
            
            # Store the height of the sibling subtree for each child node.
            if node.left:
                height_dict[node.left.val] = right_height
            if node.right:
                height_dict[node.right.val] = left_height
            
            # Return the maximum height of the current subtree.
            return max(left_height, right_height)

        # Helper function to update height_dict with the maximum possible height if a given node is removed.
        def update_height_dict(node, max_height):
            """
            Helper function to update height_dict with the maximum possible height if a given node is removed.
            
            Parameters:
            node (Optional[TreeNode]): The current node being processed.
            max_height (int): The current maximum height of the tree excluding the current node.
            """
            if not node:
                return
            
            # Update the max height for the current node if needed.
            if max_height != -2 and height_dict[node.val] < max_height:
                height_dict[node.val] = max_height
            
            # Update max height for left and right children.
            if node.left:
                update_height_dict(node.left, max(max_height, height_dict[node.val]))
            if node.right:
                update_height_dict(node.right, max(max_height, height_dict[node.val]))

        # Step 1: Calculate the height of each subtree and populate height_dict.
        calculate_height(root, 0)
        
        # Step 2: Update height_dict to include maximum heights when removing nodes.
        update_height_dict(root, -2)
        
        # Step 3: Return the results for each query.
        return [height_dict[q] for q in queries]

# Explanation of Changes:
# 1. Renamed functions and variables to improve clarity.
# 2. Simplified the logic for calculating and updating heights.
# 3. Added detailed comments to explain each step and its purpose.
# 4. Added function parameter documentation for better understanding.
# 5. The solution maintains O(n) complexity by performing a single traversal for each helper function.


