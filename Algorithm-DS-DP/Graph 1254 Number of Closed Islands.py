'''
Graph 1254 Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:
        Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        Output: 2
        Explanation: Islands in gray are closed because they are completely surrounded by water (group of 1s).


Example 2:
        Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        Output: 1

Example 3:
        Input: grid = [[1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,1,0,1,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        Output: 2
 
Constraints:
          1 <= grid.length, grid[0].length <= 100
          0 <= grid[i][j] <=1
'''

from typing import List

class Solution:
    LAND = 0  # Represents land in the grid
    WATER = 1  # Represents water in the grid

    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Counts the number of closed islands in a grid. A closed island is a group of
        connected land cells (0s) completely surrounded by water cells (1s).

        Parameters:
            grid (List[List[int]]): 2D grid with 0 representing land and 1 representing water.

        Returns:
            int: The number of closed islands in the grid.
        """
        n, m = len(grid), len(grid[0])

        # Convert border land cells to water to eliminate non-closed islands
        for row in range(n):
            self._flood_fill(row, 0, grid)         # Left border
            self._flood_fill(row, m - 1, grid)     # Right border

        for col in range(m):
            self._flood_fill(0, col, grid)         # Top border
            self._flood_fill(n - 1, col, grid)     # Bottom border

        closed_islands = 0

        # Check and count closed islands by starting flood fill from each land cell
        for row in range(1, n - 1):
            for col in range(1, m - 1):
                if grid[row][col] == self.LAND:
                    self._flood_fill(row, col, grid)
                    closed_islands += 1

        return closed_islands

    def _flood_fill(self, row: int, col: int, grid: List[List[int]]):
        """
        Converts connected land cells (0s) into water (1s) to mark them as visited.

        Parameters:
            row (int): The current row index in the grid.
            col (int): The current column index in the grid.
            grid (List[List[int]]): The 2D grid of land and water.
        """
        # Check for out-of-bounds or non-land cells to avoid unnecessary recursion
        if not self._in_bounds(row, col, grid) or grid[row][col] != self.LAND:
            return

        # Mark current cell as water to mark it as visited
        grid[row][col] = self.WATER

        # Recursively flood fill all adjacent cells
        self._flood_fill(row - 1, col, grid)  # Up
        self._flood_fill(row + 1, col, grid)  # Down
        self._flood_fill(row, col - 1, grid)  # Left
        self._flood_fill(row, col + 1, grid)  # Right

    @staticmethod
    def _in_bounds(row: int, col: int, grid: List[List[int]]) -> bool:
        """
        Checks if a given cell is within the bounds of the grid.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            grid (List[List[int]]): The 2D grid of land and water.

        Returns:
            bool: True if the cell is within bounds, False otherwise.
        """
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
