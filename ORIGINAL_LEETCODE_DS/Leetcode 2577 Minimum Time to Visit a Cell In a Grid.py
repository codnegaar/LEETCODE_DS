'''
Leetcode 2577 Minimum Time to Visit a Cell In a Grid

You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit 
the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].
You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions:
up, down, left, and right. Each move you make takes 1 second.
Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.
 
Example 1:
        Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
        Output: 7
        Explanation: One of the paths that we can take is the following:
        - at t = 0, we are on the cell (0,0).
        - at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
        - at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
        - at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
        - at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
        - at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
        - at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
        - at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
        The final time is 7. It can be shown that it is the minimum time possible.

Example 2:
        Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
        Output: -1
        Explanation: There is no path from the top left to the bottom-right cell.
         

Constraints:
        m == grid.length
        n == grid[i].length
        2 <= m, n <= 1000
        4 <= m * n <= 105
        0 <= grid[i][j] <= 105
        grid[0][0] == 0

'''

from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        Finds the minimum time required to reach the bottom-right corner of the grid from the top-left corner.

        Parameters:
        grid (List[List[int]]): A 2D grid where each cell contains a non-negative integer representing the minimum time at which it can be visited.

        Returns:
        int: The minimum time required to reach the destination, or -1 if it's impossible.
        """
        R, C = len(grid), len(grid[0])

        # If the adjacent cells from (0,0) cannot be reached early enough, return -1
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        # Helper functions
        def is_outside(i, j):
            """Check if the given cell is outside the boundaries of the grid."""
            return i < 0 or i >= R or j < 0 or j >= C

        def index(i, j):
            """Convert 2D coordinates to a single index to use in a flattened list."""
            return i * C + j

        # Initialize time to reach each cell to infinity
        N = R * C
        time = [float('inf')] * N
        time[0] = 0

        # Priority queue for Dijkstra-like traversal, starting from the top-left corner
        pq = [(0, 0)]  # (time, cell_index)
        
        # Directions for moving in the grid (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Begin processing nodes from the priority queue
        while pq:
            t, idx = heappop(pq)
            i, j = divmod(idx, C)

            # If we reach the bottom-right corner, return the time taken
            if i == R - 1 and j == C - 1:
                return t

            # Explore the four possible directions
            for di, dj in directions:
                r, s = i + di, j + dj
                if is_outside(r, s):
                    continue

                # Calculate the waiting time needed to enter the next cell
                wait_time = 0 if (grid[r][s] - t) % 2 != 0 else 1
                next_time = max(t + 1, grid[r][s] + wait_time)

                # Update the time to reach the cell if we found a shorter way
                next_idx = index(r, s)
                if next_time < time[next_idx]:
                    time[next_idx] = next_time
                    heappush(pq, (next_time, next_idx))

        # If we are unable to reach the bottom-right corner, return -1
        return -1
