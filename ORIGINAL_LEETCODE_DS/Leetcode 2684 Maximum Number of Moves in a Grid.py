'''
Leetcode 2684 Maximum Number of Moves in a Grid

You are given a 0-indexed m x n matrix grid consisting of positive integers.
You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
        From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) 
        such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

Example 1:
        Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
        Output: 3
        Explanation: We can start at the cell (0, 0) and make the following moves:
        - (0, 0) -> (0, 1).
        - (0, 1) -> (1, 2).
        - (1, 2) -> (2, 3).
        It can be shown that it is the maximum number of moves that can be made.

Example 2:
        Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
        Output: 0
        Explanation: Starting from any cell in the first column we cannot perform any moves.
         
Constraints:
        m == grid.length
        n == grid[i].length
        2 <= m, n <= 1000
        4 <= m * n <= 105
        1 <= grid[i][j] <= 106
'''
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        Calculate the maximum number of moves possible in a grid, starting from any element in the first column,
        where a move consists of going from (i, j) to (i-1, j+1), (i, j+1), or (i+1, j+1), with the condition that
        the next element must be greater than the current element.

        Parameters:
        grid (List[List[int]]): A 2D list of integers representing the grid.

        Returns:
        int: The maximum number of moves possible.

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(m * n), where m is the number of rows and n is the number of columns (due to the dp table).
        """
        m, n = len(grid), len(grid[0])
        # Create a dp array initialized to 0 with the same dimensions as the grid
        dp = [[0] * n for _ in range(m)]
        max_moves = 0

        # Traverse columns from second last to the first (right to left)
        for col in range(n - 2, -1, -1):
            for row in range(m):
                # Check if we can move to the upper-right cell
                if row > 0 and grid[row][col] < grid[row - 1][col + 1]:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col + 1] + 1)
                # Check if we can move to the right cell
                if grid[row][col] < grid[row][col + 1]:
                    dp[row][col] = max(dp[row][col], dp[row][col + 1] + 1)
                # Check if we can move to the lower-right cell
                if row < m - 1 and grid[row][col] < grid[row + 1][col + 1]:
                    dp[row][col] = max(dp[row][col], dp[row + 1][col + 1] + 1)

        # Find the maximum number of moves starting from the first column
        for row in range(m):
            max_moves = max(max_moves, dp[row][0])
        
        return max_moves

# Example usage
# sol = Solution()
# grid = [[1,3,1],[3,4,2],[2,2,1]]
# print(sol.maxMoves(grid))  # Expected output: 3
