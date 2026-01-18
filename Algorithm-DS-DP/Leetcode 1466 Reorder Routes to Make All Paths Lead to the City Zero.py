'''
Leetcode 1466 Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities
(this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:
        Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        Output: 3
        Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
        Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
        Output: 2
        Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:        
        Input: n = 3, connections = [[1,0],[2,0]]
        Output: 0
 

Constraints:
        2 <= n <= 5 * 104
        connections.length == n - 1
        connections[i].length == 2
        0 <= ai, bi <= n - 1
        ai != bi


'''

from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Given a number of cities 'n' connected by bidirectional roads such that every road has a direction,
        this function returns the minimum number of roads we need to change in order to make all roads lead to city 0.

        @param self: Reference to the current instance of the class.
        @param n: Total number of cities (nodes in the graph).
        @param connections: List of roads represented as pairs [a, b], where 'a' is connected to 'b'.
        @return: Minimum number of roads that need to be reordered.
        """
        # Create an adjacency list to represent the graph.
        adj_list = defaultdict(list)
        
        # Build the graph: add forward edges as positive and backward edges as negative.
        for a, b in connections:
            adj_list[a].append(b)   # Forward edge (indicating a -> b)
            adj_list[b].append(-a)  # Backward edge (indicating b -> a, using negative to differentiate direction)
        
        # Initialize a list to track visited nodes.
        visited = [0] * n
        
        # Define a Depth First Search (DFS) function to traverse the graph.
        def dfs(node: int, vis: List[int]) -> int:
            """
            Recursive DFS function to explore the graph and count reorders needed.

            @param node: The current node being visited.
            @param vis: List to track visited nodes.
            @return: Number of road directions that need to be changed.
            """
            res = 0
            # Traverse all adjacent nodes of the current node.
            for nxt in adj_list[node]:
                # If the next node has already been visited, skip it.
                if vis[abs(nxt)] == 1:
                    continue
                # If the edge is a forward edge (positive value), increment reorder count.
                if nxt > 0:
                    res += 1
                # Mark the next node as visited.
                vis[abs(nxt)] = 1
                # Recursively visit the next node and accumulate the result.
                res += dfs(abs(nxt), vis)
            return res
        
        # Start DFS from node 0, marking it as visited.
        visited[0] = 1
        return dfs(0, visited)

# Example Usage:
# sol = Solution()
# print(sol.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))

