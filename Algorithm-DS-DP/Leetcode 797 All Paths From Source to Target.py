'''
Leetcode 797 All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
        Input: graph = [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
        Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
        Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
        Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]         

Constraints:
        n == graph.length
        2 <= n <= 15
        0 <= graph[i][j] < n
        graph[i][j] != i (i.e., there will be no self-loops).
        All the elements of graph[i] are unique.
        The input graph is guaranteed to be a DAG.

'''

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        This function finds all possible paths from the source node (node 0) to the target node (last node in the graph).
        
        @param self: Reference to the current instance of the class.
        @param graph: A list of lists representing a directed acyclic graph, where graph[i] contains the nodes that node i is connected to.
        @return: A list of lists, where each list represents a path from the source node (0) to the target node (n-1).
        """
        # List to store all valid paths from the source (node 0) to the target (last node)
        paths = []
        
        # Stack to store nodes for DFS traversal. Each element is a tuple containing the current node and the current path.
        stack = [(0, [0])]  # Start with the source node (0) and the initial path containing only the source node.

        # Perform Depth First Search (DFS) using a stack
        while stack:
            # Pop a node and path from the stack to explore further
            node, path = stack.pop()
            
            # If we reach the target node (the last node in the graph), add the path to the list of paths
            if node == len(graph) - 1:
                paths.append(path)
                continue  # No need to continue for this path, as it is complete

            # Iterate over all neighboring nodes
            for neighbor in graph[node]:
                # Add neighbor to the stack along with the updated path
                stack.append((neighbor, path + [neighbor]))

        # Return all collected paths from the source to the target
        return paths

# Example usage:
# solution = Solution()
# graph = [[1,2], [3], [3], []]
# result = solution.allPathsSourceTarget(graph)
# print(result)  # Output: [[0, 1, 3], [0, 2, 3]]

# Detailed comments for each part of the code:
# paths: List to store all the paths from the source to target.
# stack: Used for DFS traversal; each element is a tuple (current_node, path_so_far).
# node: Current node being explored.
# path: Path from the source to the current node.


