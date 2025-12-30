'''

Leetcode 840 Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15. 

Example 1:
        Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        Output: 1
        Explanation: 
                The following subgrid is a 3 x 3 magic square:        
                        while this one is not:
                In total, there is only one magic square inside the given grid.

Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

'''

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            # Check if the numbers in the 3x3 grid are all unique and between 1 and 9
            unique_nums = set()
            row_sum = [0] * 3
            col_sum = [0] * 3

            for a in range(3):
                for b in range(3):
                    x = grid[i - 1 + a][j - 1 + b]
                    if x < 1 or x > 9 or x in unique_nums:
                        return False
                    unique_nums.add(x)
                    row_sum[a] += x
                    col_sum[b] += x

            # Check if all row sums and column sums are 15
            if any(sum != 15 for sum in row_sum + col_sum):
                return False

            # Check diagonals
            if (grid[i - 1][j - 1] + grid[i + 1][j + 1] != 10 or
                grid[i + 1][j - 1] + grid[i - 1][j + 1] != 10):
                return False

            return True

        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3:
            return 0

        count = 0
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if grid[i][j] == 5 and isMagic(i, j):
                    count += 1
        return count
