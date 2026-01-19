'''
Leetcode 2493 Divide Nodes Into the Maximum Number of Groups

You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.
Divide the nodes of the graph into m groups (1-indexed) such that:
Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

Example 1:
        Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
        Output: 4
        Explanation: As shown in the image we:
        - Add node 5 to the first group.
        - Add node 1 to the second group.
        - Add nodes 2 and 4 to the third group.
        - Add nodes 3 and 6 to the fourth group.
        We can see that every edge is satisfied.
        It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

Example 2:
        Input: n = 3, edges = [[1,2],[2,3],[3,1]]
        Output: -1
        Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
        It can be shown that no grouping is possible.
         

Constraints:
          1 <= n <= 500
          1 <= edges.length <= 104
          edges[i].length == 2
          1 <= ai, bi <= n
          ai != bi
          There is at most one edge between any pair of vertices.

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    """
    Class to determine the maximum number of magnificent sets that can be formed 
    in a graph while ensuring no two directly connected nodes belong to the same group.
    """

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        """
        Finds the maximum number of magnificent sets in an undirected graph.

        Parameters:
        n (int): Number of nodes in the graph.
        edges (List[List[int]]): List of edges representing the graph.

        Returns:
        int: The maximum number of sets that can be formed or -1 if impossible.
        """
        # Step 1: Construct the graph as an adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Find connected components
        components = []
        visited = set()

        for node in range(1, n + 1):
            if node in visited:
                continue

            # BFS to find all nodes in this connected component
            queue = deque([node])
            component = set([node])

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in component:
                        component.add(neighbor)
                        queue.append(neighbor)

            components.append(component)
            visited.update(component)

        # Step 3: Find the longest valid BFS path for each component
        max_groups = []
        
        for component in components:
            longest = -1  # Track the maximum depth
            for node in component:
                bfs_result = self.bfs_longest_path(graph, node)
                if bfs_result == -1:
                    return -1  # Graph contains an odd cycle, making division impossible
                longest = max(longest, bfs_result)
            max_groups.append(longest)

        # Step 4: Sum the longest BFS paths from each component
        return sum(max_groups)

    def bfs_longest_path(self, graph: dict, start: int) -> int:
        """
        Performs BFS to determine the longest path in a bipartite graph.

        Parameters:
        graph (dict): Adjacency list of the graph.
        start (int): The starting node for BFS traversal.

        Returns:
        int: The longest distance from start in a bipartite setting, or -1 if the graph is not bipartite.
        """
        queue = deque([start])
        seen = {start}
        level_nodes = set()
        depth = 0

        while queue:
            depth += 1
            next_level = set()

            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in level_nodes:
                        return -1  # Cycle detected, meaning graph is not bipartite
                    if neighbor not in seen:
                        seen.add(neighbor)
                        next_level.add(neighbor)
                        queue.append(neighbor)

            level_nodes = next_level  # Track nodes at the current level

        return depth  # Return the longest depth found

# Example Usage
solution = Solution()
n = 6
edges = [[1, 2], [2, 3], [4, 5], [5, 6]]
print(solution.magnificentSets(n, edges))  # Expected Output: 4

# Unit Tests
import unittest

class TestMagnificentSets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [5, 6]]
        self.assertEqual(self.solution.magnificentSets(n, edges), 4)

    def test_case_2(self):
        n = 5
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]  # Odd cycle (not bipartite)
        self.assertEqual(self.solution.magnificentSets(n, edges), -1)

    def test_case_3(self):
        n = 4
        edges = [[1, 2], [2, 3], [3, 4], [4, 1]]  # Even cycle (bipartite)
        self.assertEqual(self.solution.magnificentSets(n, edges), 4)

if __name__ == "__main__":
    unittest.main()
