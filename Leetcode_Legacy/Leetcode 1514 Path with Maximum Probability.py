'''
Leetcode 1514 Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge
connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
        Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
        Output: 0.25000
        Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
        Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
        Output: 0.30000

Example 3:
        Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
        Output: 0.00000
        Explanation: There is no path between 0 and 2.

Constraints:
        2 <= n <= 10^4
        0 <= start, end < n
        start != end
        0 <= a, b < n
        a != b
        0 <= succProb.length == edges.length <= 2*10^4
        0 <= succProb[i] <= 1
        There is at most one edge between every two nodes.

'''

import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        # Build the adjacency list for the graph
        adj = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        # Priority queue for Dijkstra's algorithm, using negative probabilities to simulate max-heap
        maxHeap = [(-1.0, start)]
        # Array to store the maximum probability to reach each node
        maxProb = [0.0] * n
        maxProb[start] = 1.0

        while maxHeap:
            current_prob, node = heapq.heappop(maxHeap)
            current_prob = -current_prob  # Convert back to positive

            # If we reach the end node, return the probability
            if node == end:
                return current_prob

            # Explore neighbors
            for neighbor, edge_prob in adj[node]:
                new_prob = current_prob * edge_prob
                if new_prob > maxProb[neighbor]:
                    maxProb[neighbor] = new_prob
                    heapq.heappush(maxHeap, (-new_prob, neighbor))

        return 0.0
