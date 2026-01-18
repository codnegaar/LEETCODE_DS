'''
Graph 200 Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:        
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3 

Constraints:        
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.

'''

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands (connected groups of '1's) in the given grid.

        Parameters:
        grid (List[List[str]]): 2D grid where '1' represents land and '0' represents water.

        Returns:
        int: The number of islands.
        """
        # Initialize dimensions and directions
        m, n = len(grid), len(grid[0]) if grid else 0
        dirs = [0, 1, 0, -1, 0]  # To move in 4 directions: right, down, left, up
        
        # BFS to traverse the island and mark visited cells
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            grid[r][c] = '2'  # Mark as visited by changing '1' to '2'
            while queue:
                i, j = queue.popleft()
                for k in range(4):
                    x, y = i + dirs[k], j + dirs[k + 1]
                    # Continue only if within bounds and cell is unvisited land
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        queue.append((x, y))
                        grid[x][y] = '2'  # Mark cell as visited

        # Main logic to count islands
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # Found unvisited land
                    bfs(i, j)          # Traverse all connected land cells
                    island_count += 1  # Increment island count

        return island_count

