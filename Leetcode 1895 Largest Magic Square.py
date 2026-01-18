'''
Leetcode 1895 Largest Magic Square

A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.


Example 1:
        Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
        Output: 3
        Explanation: The largest magic square has a size of 3.
        Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
        - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
        - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
        - Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:
        Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
        Output: 2
         

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        1 <= grid[i][j] <= 106

'''

from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Return the size (k) of the largest magic square inside `grid`.
        A k x k square is "magic" when every row, every column, and the two main diagonals
        all sum to the same value.

        Approach:
        - Precompute prefix sums for each row and each column.
        - Try square sizes from largest to smallest. For each top-left corner,
          check all row sums and column sums quickly using prefix arrays; if they
          match the target, check the two diagonals by direct summation.
        - Helper functions row_sum and col_sum make range-sum queries O(1).
        """
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0

        # Row prefix sums: row_prefix[r][c] = sum of grid[r][:c] with an extra leading 0
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_prefix[r][c+1] = row_prefix[r][c] + grid[r][c]

        # Column prefix sums: col_prefix[c][r] = sum of grid[:r][c] with an extra leading 0
        col_prefix = [[0] * (m + 1) for _ in range(n)]
        for c in range(n):
            for r in range(m):
                col_prefix[c][r+1] = col_prefix[c][r] + grid[r][c]

        # Helper: sum of row r from column c1 (inclusive) to c2 (exclusive)
        def row_sum(r: int, c1: int, c2: int) -> int:
            return row_prefix[r][c2] - row_prefix[r][c1]

        # Helper: sum of column c from row r1 (inclusive) to r2 (exclusive)
        def col_sum(c: int, r1: int, r2: int) -> int:
            return col_prefix[c][r2] - col_prefix[c][r1]

        max_k = min(m, n)

        # Try sizes from largest down to 2 (1 is always valid)
        for k in range(max_k, 1, -1):
            # For each possible top-left corner (r, c) of a k x k square
            for r in range(0, m - k + 1):
                for c in range(0, n - k + 1):
                    target = row_sum(r, c, c + k)  # sum of the first row of the candidate square

                    # Quick check: all rows and all columns should sum to target
                    all_rows_ok = all(row_sum(r + i, c, c + k) == target for i in range(k))
                    if not all_rows_ok:
                        continue
                    all_cols_ok = all(col_sum(c + j, r, r + k) == target for j in range(k))
                    if not all_cols_ok:
                        continue

                    # Check diagonals
                    diag1 = sum(grid[r + i][c + i] for i in range(k))
                    diag2 = sum(grid[r + i][c + (k - 1) - i] for i in range(k))
                    if diag1 == target and diag2 == target:
                        return k

        return 1



