'''
Graph 863 All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
        Output: [7,4,1]
        Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
        Input: root = [1], target = 1, k = 3
        Output: []
         

Constraints:
        The number of nodes in the tree is in the range [1, 500].
        0 <= Node.val <= 500
        All the values Node.val are unique.
        target is the value of one of the nodes in the tree.
        0 <= k <= 1000

'''
from collections import deque

class Solution:
    def match_parent(self, root, parent_map):
        """
        Populates the parent_map with each node's parent for easy traversal.
        
        Args:
            root (TreeNode): The root of the binary tree.
            parent_map (dict): Dictionary that will store the parent of each node.
        """
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # If left child exists, map its parent and add to queue
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)

            # If right child exists, map its parent and add to queue
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def distanceK(self, root, target, k):
        """
        Finds all nodes that are a distance 'k' from the target node.
        
        Args:
            root (TreeNode): The root of the binary tree.
            target (TreeNode): The target node from which to measure distance.
            k (int): The distance from the target node.
        
        Returns:
            List[int]: A list of node values that are at distance 'k' from the target.
        """
        # Map each node to its parent to facilitate bi-directional traversal
        parent_map = {}
        self.match_parent(root, parent_map)

        # Use BFS to find nodes at distance k
        queue = deque([target])
        seen = {target}  # Track visited nodes to avoid cycles
        cur_distance = 0

        while queue:
            # Stop if we have reached the desired distance
            if cur_distance == k:
                break
            cur_distance += 1

            # Process nodes at the current distance
            for _ in range(len(queue)):
                node = queue.popleft()

                # Check left child, add to queue if not seen
                if node.left and node.left not in seen:
                    seen.add(node.left)
                    queue.append(node.left)

                # Check right child, add to queue if not seen
                if node.right and node.right not in seen:
                    seen.add(node.right)
                    queue.append(node.right)

                # Check parent, add to queue if not seen
                if node in parent_map and parent_map[node] not in seen:
                    seen.add(parent_map[node])
                    queue.append(parent_map[node])

        # Collect all nodes at distance k
        return [node.val for node in queue]

# Usage Example
# root = TreeNode(...)
# target = TreeNode(...)
# k = 2
# solution = Solution()
# result = solution.distanceK(root, target, k)
