'''

Leetcode 2872 Maximum Number of K-Divisible Components
 
There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.
A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the 
values of its nodes.

Return the maximum number of components in any valid split. 

Example 1:
          Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
          Output: 2
          Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
          - The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
          - The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
          It can be shown that no other valid split has more than 2 connected components.

Example 2:
          Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
          Output: 3
          Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
          - The value of the component containing node 0 is values[0] = 3.
          - The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
          - The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
          It can be shown that no other valid split has more than 3 connected components.
 
Constraints:
          1 <= n <= 3 * 104
          edges.length == n - 1
          edges[i].length == 2
          0 <= ai, bi < n
          values.length == n
          0 <= values[i] <= 109
          1 <= k <= 109
          Sum of values is divisible by k.
          The input is generated such that edges represents a valid tree.
'''

from collections import defaultdict

class Solution:
    """
    Given a tree represented by an undirected graph, we need to find the maximum number
    of components that have a sum of values divisible by k.

    Attributes:
        comp: The number of valid components found.
    
    Methods:
        maxKDivisibleComponents(n, edges, values, k):
            Returns the maximum number of components that have the sum of values divisible by k.
    """
    
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        This function finds the maximum number of components in the tree where the sum of
        node values in the component is divisible by k.
        
        Parameters:
            n (int): The number of nodes in the tree.
            edges (list of tuple): The list of edges representing the tree, each edge is a tuple (u, v).
            values (list of int): The values assigned to each node in the tree.
            k (int): The divisor for checking divisibility of component sums.
            
        Returns:
            int: The number of components where the sum of values is divisible by k.
        """
        
        # Adjacency list to store the tree structure
        adj = defaultdict(list)
        
        # Build the adjacency list from edges
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Initialize the component count
        self.comp = 0
        
        def dfs(node, parent):
            """
            Depth-First Search (DFS) to traverse the tree and calculate the sum of values
            for each subtree. If the sum of values in a subtree is divisible by k, it's counted as a component.
            
            Parameters:
                node (int): The current node being visited.
                parent (int): The parent of the current node, used to avoid cycles.
            
            Returns:
                int: The remainder of the sum of values mod k for the current subtree.
            """
            total = values[node]  # Start with the node's value
            
            # Visit all neighbors of the current node
            for neighbor in adj[node]:
                if neighbor != parent:  # Avoid revisiting the parent node
                    total += dfs(neighbor, node)
            
            # If the sum of values in the subtree is divisible by k, count this component
            if total % k == 0:
                self.comp += 1
                return 0  # Reset the sum of this component
            
            return total % k  # Return the remainder of the sum mod k

        # Perform DFS starting from node 0
        dfs(0, -1)
        
        # Return the total number of components where sum is divisible by k
        return self.comp


# Unit tests
def test_solution():
    solution = Solution()

    # Example 1
    n = 5
    edges = [(0, 1), (1, 2), (1, 3), (3, 4)]
    values = [1, 2, 3, 4, 5]
    k = 5
    print(solution.maxKDivisibleComponents(n, edges, values, k))  # Expected output: 2

    # Example 2
    n = 3
    edges = [(0, 1), (1, 2)]
    values = [1, 1, 1]
    k = 2
    print(solution.maxKDivisibleComponents(n, edges, values, k))  # Expected output: 1

    # Example 3
    n = 4
    edges = [(0, 1), (1, 2), (1, 3)]
    values = [1, 2, 3, 4]
    k = 3
    print(solution.maxKDivisibleComponents(n, edges, values, k))  # Expected output: 2

test_solution()

