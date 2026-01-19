'''
Leetcode 1368 Minimum Cost to Make at Least One Valid Path in a Grid
 
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper
left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
Return the minimum cost to make the grid have at least one valid path. 

Example 1:
        Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
        Output: 3
        Explanation: You will start at point (0, 0).
        The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
        The total cost = 3.

Example 2:
        Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
        Output: 0
        Explanation: You can follow the path from (0, 0) to (2, 2).
        
Example 3:
        Input: grid = [[1,2],[4,3]]
        Output: 1 

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        1 <= grid[i][j] <= 4
'''

import collections
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Find the minimum cost to reach the bottom-right corner of the grid.

        Parameters:
        grid (List[List[int]]): A 2D grid where each cell contains a direction (1=right, 2=left, 3=down, 4=up).

        Returns:
        int: The minimum cost to reach the bottom-right corner.
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        queue = collections.deque([(0, 0, 0)])  # (x, y, cost)
        costs = {}  # Dictionary to store minimum cost to reach each cell

        # BFS traversal
        while queue:
            x, y, cost = queue.popleft()

            # Continue traversal if the cell hasn't been visited
            while 0 <= x < m and 0 <= y < n and (x, y) not in costs:
                costs[x, y] = cost  # Record the minimum cost to reach (x, y)

                # Add all neighbors with an incremented cost to the queue
                for dx, dy in directions:
                    queue.append((x + dx, y + dy, cost + 1))

                # Move in the predefined direction for the current cell
                dx, dy = directions[grid[x][y] - 1]
                x, y = x + dx, y + dy

        return costs[m - 1, n - 1]  # Return the cost to reach the bottom-right corner


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    print(f"Minimum cost to reach the bottom-right corner: {solution.minCost(grid)}")  # Expected output: 0
 
