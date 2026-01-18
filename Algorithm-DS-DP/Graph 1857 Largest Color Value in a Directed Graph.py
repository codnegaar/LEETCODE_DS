'''
Graph 1857 Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed).
You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. 
The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle. 

Example 1:
        Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
        Output: 3
        Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
        Input: colors = "a", edges = [[0,0]]
        Output: -1
        Explanation: There is a cycle from 0 to 0.
         
Constraints:
        n == colors.length
        m == edges.length
        1 <= n <= 105
        0 <= m <= 105
        colors consist of lowercase English letters.
        0 <= aj, bj < n
'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        This function returns the largest value of any path in the graph based on node colors.
        
        Parameters:
        colors (str): A string where each character represents a color for a node (0-indexed).
        edges (List[List[int]]): A list of directed edges representing connections between nodes.
        
        Returns:
        int: The largest color value on any valid path, or -1 if there is a cycle.
        """
        n = len(colors)  # Number of nodes
        graph = defaultdict(list)
        indegree = [0] * n  # Store indegree for each node
        
        # Build the graph and populate indegree values
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        
        # Perform Topological Sort (Kahn's Algorithm)
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        dp = [[0] * 26 for _ in range(n)]  # dp[i][c] stores max count of color 'c' at node 'i'
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
        
        visited = 0
        max_color_value = 0
        
        while q:
            node = q.popleft()
            visited += 1
            max_color_value = max(max_color_value, max(dp[node]))
            
            for neighbor in graph[node]:
                # Update the dp table for the neighbor
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))
                
                # Decrease indegree and add to queue if indegree becomes 0
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # If all nodes were not visited, there is a cycle
        return -1 if visited < n else max_color_value

