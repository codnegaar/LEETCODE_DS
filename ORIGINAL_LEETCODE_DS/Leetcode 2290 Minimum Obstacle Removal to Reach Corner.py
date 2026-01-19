'''
Leetcode 2290 Minimum Obstacle Removal to Reach Corner
  
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:
        Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
        Output: 2
        Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
        It can be shown that we need to remove at least 2 obstacles, so we return 2.
        Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
        Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
        Output: 0
        Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
         

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 105
        2 <= m * n <= 105
        grid[i][j] is either 0 or 1.
        grid[0][0] == grid[m - 1][n - 1] == 0

'''
from collections import deque

class Solution:
    def bfs(self, start, end, n, graph):
        """
        Perform BFS to find the shortest distance from start to end in the graph.

        Parameters:
        start (int): Starting node.
        end (int): Ending node.
        n (int): Number of nodes in the graph.
        graph (List[List[int]]): Adjacency list representing the graph.

        Returns:
        int: The shortest distance from start to end.
        """
        # Initialize distances as infinity for all nodes
        dist = [float('inf')] * n
        dist[start] = 0
        q = deque([start])

        # Perform BFS
        while q:
            curr = q.popleft()
            # Traverse all neighbors of the current node
            for u in graph[curr]:
                # If we find a shorter path, update and enqueue the neighbor
                if dist[u] > dist[curr] + 1:
                    dist[u] = dist[curr] + 1
                    q.append(u)

        return dist[end]

    def shortestDistanceAfterQueries(self, n, queries):
        """
        Find the shortest distance from node 0 to node n-1 after each query.

        Parameters:
        n (int): Number of nodes in the graph.
        queries (List[Tuple[int, int]]): List of queries where each query adds an edge (u, v).

        Returns:
        List[int]: List of shortest distances after each query.
        """
        answer = []
        # Initialize graph with each node pointing to the next node (linear structure)
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        # Process each query
        for u, v in queries:
            graph[u].append(v)  # Add the edge (u -> v)
            # Calculate shortest distance from node 0 to node n-1
            answer.append(self.bfs(0, n - 1, n, graph))

        return answer

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    n = 5  # Number of nodes
    queries = [(1, 3), (0, 4), (2, 4)]  # List of queries to add edges
    result = sol.shortestDistanceAfterQueries(n, queries)
    print(result)  # Output the shortest distances after each query


# Second Solution:
from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Finds the minimum number of obstacles that need to be removed to reach the bottom-right corner 
        from the top-left corner of a grid.

        Parameters:
        grid (List[List[int]]): A 2D grid of 0s (empty cell) and 1s (obstacle).

        Returns:
        int: The minimum number of obstacles that need to be removed.
        """
        m, n = len(grid), len(grid[0])  # Dimensions of the grid
        
        # Initialize distance matrix with infinity, which will store the minimum number of obstacles to reach each cell
        distance = [[float('inf')] * n for _ in range(m)]
        
        # Double-ended queue (deque) for 0-1 BFS
        dq = deque()
        
        # Starting at (0, 0), no obstacles removed initially
        distance[0][0] = 0
        dq.appendleft((0, 0))
        
        # Possible directions for movement (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS to find the minimum number of obstacles to remove
        while dq:
            x, y = dq.popleft()
            # Iterate over all possible neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within grid boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the potential new distance
                    newDist = distance[x][y] + grid[nx][ny]
                    # If the new distance is better, update it
                    if newDist < distance[nx][ny]:
                        distance[nx][ny] = newDist
                        # If the cell is empty, add it to the front of the deque for priority processing
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        # If the cell has an obstacle, add it to the back of the deque
                        else:
                            dq.append((nx, ny))
        
        # Return the distance to the bottom-right corner
        return distance[m - 1][n - 1]

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    # Grid with obstacles (1 represents an obstacle, 0 represents an empty cell)
    grid = [
        [0, 1, 1],
        [1, 1, 0],
        [1, 0, 0]
    ]
    result = sol.minimumObstacles(grid)
    print(f"Minimum obstacles to remove: {result}")  # Expected output: 2
