'''
Leetcode DFS 695 Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0.

 
Example 1:
        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6
        Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0
         
Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0 or 1
'''


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def dfs(i: int, j: int) -> int:
      if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
        return 0
      if grid[i][j] != 1:
        return 0

      grid[i][j] = 2

      return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


# Second solution:

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum area of an island in a grid.
        
        An island is a connected group of 1s (representing land),
        connected horizontally or vertically. The function returns
        the area of the largest island found.

        Parameters:
        grid (List[List[int]]): 2D grid containing 0s (water) and 1s (land).
        
        Returns:
        int: The area of the largest island in the grid.
        """
        
        def dfs(i: int, j: int) -> int:
            """
            Performs depth-first search to calculate the area of the island starting at (i, j).
            Marks visited cells by changing their value to 2 to avoid re-visits.
            
            Parameters:
            i (int): Row index.
            j (int): Column index.
            
            Returns:
            int: Area of the island connected to (i, j).
            """
            # Check boundaries and if cell is land (1)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            # Mark the cell as visited
            grid[i][j] = 2

            # Calculate area recursively for neighboring cells
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        # Iterate over all cells in the grid to find the maximum island area
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Start DFS if a new island is found
                    max_area = max(max_area, dfs(i, j))

        return max_area
