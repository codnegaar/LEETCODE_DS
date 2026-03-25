'''
Leetcode 3546 Equal Sum Grid Partition I
 
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

Example 1:
        Input: grid = [[1,4],[2,3]]
        Output: true
        Explanation: A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:        
        Input: grid = [[1,3],[2,4]]        
        Output: false        
        Explanation:        
        No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

Constraints:
        1 <= m == grid.length <= 105
        1 <= n == grid[i].length <= 105
        2 <= m * n <= 105
        1 <= grid[i][j] <= 105
'''

import numpy as np
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        matrix = np.array(grid)
        m, n = matrix.shape
        total_sum = matrix.sum()
    
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2

        # Binary Search on Horizontal Cuts (Rows)
        low, high = 0, m - 2 # m-2 ensures the second section is non-empty
        while low <= high:
            mid = (low + high) // 2
            # Sum everything from row 0 to row mid
            current_sum = matrix[:mid+1, :].sum()
        
            if current_sum == target:
                return True
            elif current_sum < target:
                low = mid + 1
            else:
                high = mid - 1

        # Binary Search on Vertical Cuts (Columns)
        low, high = 0, n - 2 # n-2 ensures the second section is non-empty
        while low <= high:
            mid = (low + high) // 2
            # Sum everything from column 0 to column mid
            current_sum = matrix[:, :mid+1].sum()
        
            if current_sum == target:
                return True
            elif current_sum < target:
                low = mid + 1
            else:
                high = mid - 1

        return False        
