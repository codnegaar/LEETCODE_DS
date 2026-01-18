'''
Leetcode 1192 Critical Connections in a Network

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection 
between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order. 

Example 1:
        Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
        Output: [[1,3]]
        Explanation: [[3,1]] is also accepted.

Example 2:
        Input: n = 2, connections = [[0,1]]
        Output: [[0,1]]
 
Constraints:
        2 <= n <= 105
        n - 1 <= connections.length <= 105
        0 <= ai, bi <= n - 1
        ai != bi
        There are no repeated connections.

'''

from typing import List
import collections

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Finds critical connections (bridges) in an undirected graph.
        
        Parameters:
        - n: int - number of nodes in the graph
        - connections: List[List[int]] - a list of edges between nodes

        Returns:
        - List[List[int]] - a list of critical connections/bridges where removing the edge disconnects the graph.
        """
        
        # Create adjacency list to represent the graph
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Variables to store discovery time (depth), lowest point (earliest visited ancestor),
        # parent of each node, and visited status of nodes
        timer = 0
        depth = [-1] * n  # Discovery time of each node
        lowest = [0] * n  # Lowest discovery time reachable from the node
        parent = [-1] * n # Parent of each node
        visited = [False] * n  # Visited status
        res = []  # List to store critical connections (bridges)

        def dfs(u: int):
            """
            Depth First Search (DFS) to find bridges.
            
            Parameters:
            - u: int - current node being visited in DFS
            """
            nonlocal timer
            visited[u] = True
            depth[u] = lowest[u] = timer
            timer += 1

            # Explore all adjacent nodes of u
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u  # Set the parent of v
                    dfs(v)  # Recursive DFS call

                    # After visiting v, check if it's a bridge
                    if lowest[v] > depth[u]:
                        res.append([u, v])

                    # Update the lowest point reachable from u
                    lowest[u] = min(lowest[u], lowest[v])

                # If v is already visited and it's not the parent, update the lowest point
                elif v != parent[u]:
                    lowest[u] = min(lowest[u], depth[v])

        # Start DFS from node 0 (assuming graph is connected)
        dfs(0)
        return res

