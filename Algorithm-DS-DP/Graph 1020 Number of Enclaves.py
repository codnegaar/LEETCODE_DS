'''
Graph 1020 Number of Enclaves

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
        Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
        Output: 3
        Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
        Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
        Output: 0
        Explanation: All 1s are either on the boundary or can reach the boundary.         

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 500
        grid[i][j] is either 0 or 1.

'''

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Function to count the number of land cells in the grid for which we cannot walk off the boundary.
        
        Parameters:
        grid (List[List[int]]): The m x n binary matrix where 0 represents sea cells and 1 represents land cells.
        
        Returns:
        int: The number of land cells that are enclosed by sea cells and cannot reach the boundary.
        """
        m, n = len(grid), len(grid[0])

        # Helper function to perform DFS and mark the connected land as sea.
        def dfs(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return
            # Mark the cell as sea to avoid revisiting it.
            grid[x][y] = 0
            # Visit all four adjacent cells.
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Step 1: Traverse the boundary cells and perform DFS to eliminate any connected land.
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    dfs(i, j)

        # Step 2: Count the number of remaining land cells that are enclosed.
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    enclave_count += 1

        return enclave_count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    grid1 = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(solution.numEnclaves(grid1))  # Output: 3
    
    grid2 = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(solution.numEnclaves(grid2))  # Output: 0

