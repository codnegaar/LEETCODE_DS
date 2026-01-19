'''
Leetcode 2699 Modify Graph Edge Weights

You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array
edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.
Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] 
so that the shortest distance between the nodes source and destination becomes equal to an integer target. If
there are multiple modifications that make the shortest distance between source and destination equal to target,
any of them will be considered correct.
Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance
from source to destination equal to target, or an empty array if it's impossible.
Note: You are not allowed to modify the weights of edges with initial positive weights. 

Example 1:
        Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
        Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
        Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.

Example 2:
        Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
        Output: []
        Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.

Example 3:
        Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
        Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
        Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
     
Constraints:
        1 <= n <= 100
        1 <= edges.length <= n * (n - 1) / 2
        edges[i].length == 3
        0 <= ai, bi < n
        wi = -1 or 1 <= wi <= 107
        ai != bi
        0 <= source, destination < n
        source != destination
        1 <= target <= 109
        The graph is connected, and there are no self-loops or repeated edges

'''
import heapq

class Solution:
    INF = int(2e9)  # Constant representing infinity for unbounded edges
    
    def dijkstra(self, n, source, destination, adj):
        distance = [float('inf')] * n  # Initialize distances to all nodes as infinity
        distance[source] = 0  # Distance from source to itself is 0
        pq = [(0, source)]  # Min-heap priority queue with the source node

        while pq:
            current_distance, node = heapq.heappop(pq)  # Get the node with the smallest distance

            if node == destination:  # Stop if we reach the destination
                break

            # Explore all adjacent nodes of the current node
            for edge_cost, neighbor in adj[node]:
                new_distance = current_distance + edge_cost
                if new_distance < distance[neighbor]:  # Found a shorter path
                    distance[neighbor] = new_distance  # Update the distance
                    heapq.heappush(pq, (new_distance, neighbor))  # Push updated distance to the queue

        return distance[destination]  # Return the shortest distance to the destination

    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adj = [[] for _ in range(n)]  # Adjacency list representation of the graph

        # Build the adjacency list, excluding edges with unknown cost (-1)
        for u, v, w in edges:
            if w != -1:
                adj[u].append((w, v))
                adj[v].append((w, u))

        # Get the shortest distance from source to destination
        min_distance = self.dijkstra(n, source, destination, adj)

        if min_distance < target:  # If the shortest path is less than the target, no valid configuration
            return []

        exact_match = min_distance == target  # Check if current distance equals the target

        # Modify edges with unknown cost (-1) to potentially find a valid configuration
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue  # Skip edges with a known cost
            
            # Set a temporary cost for the edge based on the current distance match
            edges[i][2] = self.INF if exact_match else 1
            adj[u].append((edges[i][2], v))
            adj[v].append((edges[i][2], u))

            if not exact_match:  # Recalculate the shortest path only if necessary
                new_distance = self.dijkstra(n, source, destination, adj)
                if new_distance <= target:
                    exact_match = True
                    edges[i][2] += target - new_distance  # Adjust the edge cost to reach the target

        return edges if exact_match else []  # Return modified edges if a valid configuration is found

