'''
Leetcode 1976 Number of Ways to Arrive at Destination

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any
other intersection and that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in
how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7. 

Example 1:
        Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
        Output: 4
        Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
        The four ways to get there in 7 minutes are:
        - 0 Γ₧¥ 6
        - 0 Γ₧¥ 4 Γ₧¥ 6
        - 0 Γ₧¥ 1 Γ₧¥ 2 Γ₧¥ 5 Γ₧¥ 6
        - 0 Γ₧¥ 1 Γ₧¥ 3 Γ₧¥ 5 Γ₧¥ 6

Example 2:
        Input: n = 2, roads = [[1,0,10]]
        Output: 1
        Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
         
Constraints:
        1 <= n <= 200
        n - 1 <= roads.length <= n * (n - 1) / 2
        roads[i].length == 3
        0 <= ui, vi <= n - 1
        1 <= timei <= 109
        ui != vi
        There is at most one road connecting any two intersections.
        You can reach any intersection from any other intersection.
'''
import heapq
from typing import List

class Solution:
    """
    Solution class to compute the number of distinct shortest paths from node 0 to node n - 1
    in a graph represented by roads (edges with weights).

    Uses Dijkstra's algorithm with path counting.
    """

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Counts the number of distinct shortest paths from node 0 to node n - 1.

        Parameters:
        -----------
        n : int
            Number of nodes in the graph (0 to n-1).
        roads : List[List[int]]
            Each element is [u, v, time] representing a bidirectional edge.

        Returns:
        --------
        int
            The number of shortest paths from node 0 to node n-1, modulo 10^9 + 7.

        Time Complexity: O(E log V)
        Space Complexity: O(V + E)
        """

        MOD = 10**9 + 7

        # Step 1∩╕ÅΓâú: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        # Step 2∩╕ÅΓâú: Initialize distance and ways arrays
        dist = [float('inf')] * n       # Stores shortest distance to each node
        dist[0] = 0

        ways = [0] * n                  # Stores number of shortest paths to each node
        ways[0] = 1

        # Step 3∩╕ÅΓâú: Min-heap priority queue for Dijkstra (time, node)
        heap = [(0, 0)]

        while heap:
            curr_time, node = heapq.heappop(heap)

            # If current time is greater than known shortest, skip
            if curr_time > dist[node]:
                continue

            # Explore neighbors
            for neighbor, travel_time in adj[node]:
                total_time = curr_time + travel_time

                # Case 1∩╕ÅΓâú: Found a shorter path to neighbor
                if total_time < dist[neighbor]:
                    dist[neighbor] = total_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (total_time, neighbor))

                # Case 2∩╕ÅΓâú: Found an additional shortest path
                elif total_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        # Step 4∩╕ÅΓâú: Return number of ways to reach node n - 1
        return ways[n - 1] % MOD
