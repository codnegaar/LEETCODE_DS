'''

Graph 1091 Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
        All the visited cells of the path are 0.
        All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
        The length of a clear path is the number of visited cells of this path.

Example 1:
        Input: grid = [[0,1],[1,0]]
        Output: 2

Example 2:
        Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
        Output: 4

Example 3:
        Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
        Output: -1
 
Constraints:
        n == grid.length
        n == grid[i].length
        1 <= n <= 100
        grid[i][j] is 0 or 1

'''
from collections import deque
from itertools import product, repeat
from functools import partial

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        Finds the shortest path from the top-left to the bottom-right corner of a binary matrix.
        The path can only traverse cells that contain 0, moving in 8 possible directions.
        
        Parameters:
        grid (list[list[int]]): A 2D binary grid representing open (0) and blocked (1) cells.
        
        Returns:
        int: The length of the shortest path. Returns -1 if there is no such path.
        """
        n = len(grid)
        start, end = (0, 0), (n - 1, n - 1)

        # Helper functions
        def in_bound(cell):
            """Checks if a cell is within grid bounds."""
            return 0 <= cell[0] < n and 0 <= cell[1] < n

        def grid_get(cell):
            """Gets the value of a cell if it's in bounds, otherwise returns 1 (treated as blocked)."""
            return grid[cell[0]][cell[1]] if in_bound(cell) else 1

        def all_neighbors(cell):
            """Generates all neighboring cells, including diagonals."""
            return product(range(cell[0] - 1, cell[0] + 2), range(cell[1] - 1, cell[1] + 2))

        def is_clear(cell, visited):
            """Checks if a cell is clear (value 0) and not already visited."""
            return grid_get(cell) == 0 and cell not in visited

        # Edge case: Start equals end
        if start == end:
            return -1 if grid_get(start) else 1

        # BFS initialization
        if grid_get(start):
            return -1  # If the start cell is blocked, no path exists
        queue = deque([(start, 1)])  # Queue holds tuples of (current cell, path length)
        seen = {start}  # Set of visited cells

        while queue:
            cell, length = queue.popleft()
            valid_neighbors = set(filter(lambda nbr: is_clear(nbr, seen), all_neighbors(cell)))

            # If we reached the end
            if end in valid_neighbors:
                return length + 1

            # Add valid neighbors to the queue
            queue.extend((neighbor, length + 1) for neighbor in valid_neighbors)
            seen.update(valid_neighbors)

        # If no path is found
        return -1
