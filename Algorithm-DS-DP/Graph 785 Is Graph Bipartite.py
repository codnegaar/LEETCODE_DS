'''

Graph 785 Is Graph Bipartite

Note: A bipartite graph is a graph where the vertices can be divided into two disjoint sets such that all edges connect a vertex in one set to a vertex in another set.
There are no edges between vertices in the disjoint sets.

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that
node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
Return true if and only if it is bipartite. 

Example 1:        
        Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        Output: false
        Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
        Input: graph = [[1,3],[0,2],[1,3],[0,2]]
        Output: true
        Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:
        graph.length == n
        1 <= n <= 100
        0 <= graph[u].length < n
        0 <= graph[u][i] <= n - 1
        graph[u] does not contain u.
        All the values of graph[u] are unique.
        If graph[u] contains v, then graph[v] contains u.

'''

from enum import Enum

class Color(Enum):
  kWhite = 0
  kRed = 1
  kGreen = 2


class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    colors = [Color.kWhite] * len(graph)

    def isValidColor(u: int, color: Color) -> bool:
      # The painted color should be same as the `color`.
      if colors[u] != Color.kWhite:
        return colors[u] == color

      colors[u] = color

      # All the children should have valid colors.
      childrenColor = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
      return all(isValidColor(v, childrenColor) for v in graph[u])

    return all(colors[i] != Color.kWhite or isValidColor(i, Color.kRed)
               for i in range(len(graph)))
        
# Second solution
from enum import Enum
from typing import List

class Color(Enum):
    WHITE = 0  # Unvisited nodes are marked as WHITE.
    RED = 1    # RED indicates one of the partitions of the bipartite graph.
    GREEN = 2  # GREEN indicates the other partition of the bipartite graph.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Determines if the given graph is bipartite.
        
        Parameters:
        graph (List[List[int]]): The graph represented as an adjacency list where
                                 graph[i] is a list of nodes adjacent to node i.
        
        Returns:
        bool: True if the graph is bipartite, False otherwise.
        """
        n = len(graph)
        colors = [Color.WHITE] * n

        # Loop through each node in case the graph is disconnected.
        for i in range(n):
            if colors[i] == Color.WHITE:
                # Start coloring from the current node using iterative DFS.
                stack = [(i, Color.RED)]
                while stack:
                    node, color = stack.pop()

                    if colors[node] == Color.WHITE:
                        # Color the current node.
                        colors[node] = color

                        # Add all adjacent nodes to the stack with the alternate color.
                        next_color = Color.GREEN if color == Color.RED else Color.RED
                        for neighbor in graph[node]:
                            stack.append((neighbor, next_color))
                    elif colors[node] != color:
                        # If the current node has already been colored with a different color,
                        # then the graph is not bipartite.
                        return False

        return True

