'''
Leetcode 934 Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands. 

Example 1:
        Input: grid = [[0,1],[1,0]]
        Output: 1

Example 2:
        Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
        Output: 2

Example 3:
        Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        Output: 1

Constraints:
        n == grid.length == grid[i].length
        2 <= n <= 100
        grid[i][j] is either 0 or 1.
        There are exactly two islands in grid.
'''
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Find the shortest bridge (minimum number of 0s) to connect two islands in the grid.

        Parameters:
        grid (List[List[int]]): A 2D list representing the map of the grid where 1s represent land and 0s represent water.

        Returns:
        int: The minimum number of 0s that must be flipped to connect the two islands.
        """

        # Step 1: Find and get all components of the first island (island 1)
        islandOne, q, visited = deque(), deque(), set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # Start BFS from the first land cell found to get all cells of the first island
                    islandOne.append([r, c])
                    q.append([r, c])
                    visited.add((r, c))
                    break
            if len(islandOne) == 1:
                break

        def isvalid(row: int, col: int) -> bool:
            """
            Check if the given cell (row, col) is within the grid bounds.

            Parameters:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

            Returns:
            bool: True if the cell is within the bounds of the grid, otherwise False.
            """
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        # Step 1 continued: Perform BFS to find all cells that belong to the first island
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                # Explore all four directions (right, left, down, up)
                for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isvalid(newRow, newCol) and grid[newRow][newCol] == 1:
                        q.append([newRow, newCol])
                        islandOne.append([newRow, newCol])
                        visited.add((newRow, newCol))

        # Step 2: Perform BFS on islandOne to find the shortest path to the second island
        numberOfMoves = 0
        while islandOne:
            size = len(islandOne)
            for _ in range(size):
                row, col = islandOne.popleft()
                # Explore all four directions (right, left, down, up)
                for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isvalid(newRow, newCol):
                        # If we find a cell from the second island, return the number of moves taken
                        if grid[newRow][newCol] == 1:
                            return numberOfMoves
                        # Add the water cell to continue expanding the BFS frontier
                        islandOne.append([newRow, newCol])
                        visited.add((newRow, newCol))
            numberOfMoves += 1

        return -1  # Should never be reached if input guarantees exactly two islands

