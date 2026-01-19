'''

Leetcode 1289 Minimum Falling Path Sum II

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
A falling path with non-zero shifts is a choice of exactly one element from each grid row such that no two elements chosen in adjacent rows are in the same column.

Example 1:
        Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
        Output: 13
        Explanation: 
        The possible falling paths are:
        [1,5,9], [1,5,7], [1,6,7], [1,6,8],
        [2,4,8], [2,4,9], [2,6,7], [2,6,8],
        [3,4,8], [3,4,9], [3,5,7], [3,5,9]
        The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
        Input: grid = [[7]]
        Output: 7
 

Constraints:
        n == grid.length == grid[i].length
        1 <= n <= 200
        -99 <= grid[i][j] <= 99

'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return min(grid[0])
        
        # Use the first row of the grid as the initial state of dp.
        dp = grid[0]
        
        # Iterate over each row starting from the second row.
        for i in range(1, n):
            # Create a new list to store the minimum path sums for this row.
            new_dp = [0] * n
            
            # Find the minimum and second minimum values in the previous row.
            # These will be used to ensure we do not add the value from the same column.
            min1, min2 = float('inf'), float('inf')
            for j in range(n):
                if dp[j] < min1:
                    min2, min1 = min1, dp[j]
                elif dp[j] < min2:
                    min2 = dp[j]
            
            # Calculate the minimum path sum for the current row.
            for j in range(n):
                # If dp[j] was the minimum in the last row, we use min2, otherwise use min1.
                new_dp[j] = grid[i][j] + (min2 if dp[j] == min1 else min1)
            
            # Update dp to the new_dp for the next iteration.
            dp = new_dp
        
        # Return the minimum value from the last dp array.
        return min(dp)


