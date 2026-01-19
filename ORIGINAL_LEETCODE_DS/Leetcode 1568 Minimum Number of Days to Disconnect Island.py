'''
Leetcode 1568 Minimum Number of Days to Disconnect Island

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
In one day, we are allowed to change any single land cell (1) into a water cell (0).
Return the minimum number of days to disconnect the grid.

Example 1:
        Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
        Output: 2
                Explanation: We need at least 2 days to get a disconnected grid.
                Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:
        Input: grid = [[1,1]]
        Output: 2
        Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
         
Constraints:        
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 30
        grid[i][j] is either 0 or 1.

''''


from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands() -> int:
            seen = set()
            
            def dfs(r, c):
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        islands += 1
                        seen.add((i, j))
                        dfs(i, j)
            return islands
        
        # If there are initially 0 or more than 1 islands, return 0
        if count_islands() != 1:
            return 0
        
        # Try removing each land cell and check if it increases the number of islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        # If no single removal makes the grid disconnected, return 2
        return 2
