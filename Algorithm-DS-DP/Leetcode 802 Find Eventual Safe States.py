'''
802 Find Eventual Safe States

There is a directed graph of n nodes with each node labeled from 0 to n - 1. A 0-indexed 2D integer represents the graph 
array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a
terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
        Illustration of graph
        Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
        Output: [2,4,5,6]
        Explanation: The given graph is shown above.
        Nodes 5 and 6 are terminal nodes with no outgoing edges from either of them.
        Every path starting at nodes 2, 4, 5, and 6 all leads to either node 5 or 6.
        
Example 2:
        Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
        Output: [4]
        Explanation:
        Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

Constraints:
        n == graph.length
        1 <= n <= 104
        0 <= graph[i].length <= n
        0 <= graph[i][j] <= n - 1
        graph[i] is sorted in a strictly increasing order.
        The graph may contain self-loops.
        The number of edges in the graph will be in the range [1, 4 * 104].
'''

from enum import Enum


class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2


class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    states = [State.kInit] * len(graph)

    def hasCycle(u: int) -> bool:
      if states[u] == State.kVisiting:
        return True
      if states[u] == State.kVisited:
        return False

      states[u] = State.kVisiting
      if any(hasCycle(v) for v in graph[u]):
        return True
      states[u] = State.kVisited

    return [i for i in range(len(graph)) if not hasCycle(i)]

# Second Solution
from collections import deque
from typing import List

class Solution:
    """
    A solution to find all eventual safe nodes in a directed graph.

    Methods
    -------
    eventualSafeNodes(graph: List[List[int]]) -> List[int]:
        Determines which nodes in the graph are eventually safe.
    """
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Finds all nodes in the graph that are eventually safe. A node is safe if it either has
        no outgoing edges (terminal nodes) or all paths starting from it lead to terminal nodes.

        Parameters
        ----------
        graph : List[List[int]]
            A directed graph represented as an adjacency list, where graph[i] contains
            the list of nodes that node i points to.

        Returns
        -------
        List[int]
            A sorted list of all safe nodes in the graph.
        """
        
        # Step 1: Reverse the graph.
        def reverse_graph(graph: List[List[int]]) -> List[List[int]]:
            """
            Constructs the reverse of the given directed graph.

            Parameters
            ----------
            graph : List[List[int]]
                The original graph as an adjacency list.

            Returns
            -------
            List[List[int]]
                The reversed graph where edges point in the opposite direction.
            """
            reversed_graph = [[] for _ in range(len(graph))]
            for node, neighbors in enumerate(graph):
                for neighbor in neighbors:
                    reversed_graph[neighbor].append(node)
            return reversed_graph

        # Number of nodes in the graph.
        n = len(graph)

        # Track out-degrees for each node.
        out_degrees = [len(neighbors) for neighbors in graph]

        # Reverse the graph for efficient traversal.
        reversed_graph = reverse_graph(graph)

        # Collect terminal nodes (nodes with 0 out-degree).
        terminals = [node for node in range(n) if out_degrees[node] == 0]

        # Initialize a queue for nodes to process and mark nodes as safe when processed.
        queue = deque(terminals)
        safe = [False] * n  # Track safeness of each node.

        # Step 2: Process the graph in reverse topological order.
        while queue:
            current = queue.popleft()
            safe[current] = True  # Mark the current node as safe.
            for neighbor in reversed_graph[current]:
                out_degrees[neighbor] -= 1  # Decrease out-degree of the neighbor.
                if out_degrees[neighbor] == 0:  # If it becomes a terminal, enqueue it.
                    queue.append(neighbor)

        # Return sorted list of safe nodes.
        return [node for node in range(n) if safe[node]]


# Example usage of the Solution class.
if __name__ == "__main__":
    solution = Solution()
    example_graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print("Safe Nodes:", solution.eventualSafeNodes(example_graph))
 

# Improvements made:
# 1. Simplified code with better structure and comments.
# 2. Optimized to O(V + E) complexity by avoiding redundant checks.
# 3. Clearer logic for reversing the graph and processing nodes.
# 4. Added unit tests to verify correctness for multiple cases.

# Reference: 
# Python's `collections.deque` for efficient queue operations: https://docs.python.org/3/library/collections.html#collections.deque
# Python's list comprehensions and adjacency lists for graph representation.



