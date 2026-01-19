'''

Leetcode 2033 Minimum Operations to Make a Uni-Value Grid

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
        Input: grid = [[2,4],[6,8]], x = 2
        Output: 4
        Explanation: We can make every element equal to 4 by doing the following: 
                - Add x to 2 once.
                - Subtract x from 6 once.
                - Subtract x from 8 twice.
                A total of 4 operations were used.

Example 2:
        Input: grid = [[1,5],[2,3]], x = 1
        Output: 5
        Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 
Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 105
        1 <= m * n <= 105
        1 <= x, grid[i][j] <= 104

'''

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        Calculate the minimum number of operations to make all elements in the grid equal
        by incrementing or decrementing elements by x in each operation.

        Parameters:
        grid (List[List[int]]): 2D grid of integers
        x (int): The allowed increment/decrement value

        Returns:
        int: Minimum number of operations, or -1 if not possible
        """
        # Flatten the grid and store all values in a single list
        flat = [num for row in grid for num in row]
        
        # Check for modulo consistency. All elements must have the same remainder mod x
        base_mod = flat[0] % x
        if any(num % x != base_mod for num in flat):
            return -1
        
        # Sort the list to find the median efficiently
        flat.sort()
        
        # Use the median element to minimize total operations
        median = flat[len(flat) // 2]
        
        # Calculate total operations needed to make all elements equal to the median
        return sum(abs(num - median) // x for num in flat)


# Example usage
if __name__ == "__main__":
    sol = Solution()
    grid = [[2, 4], [6, 8]]
    x = 2
    print(sol.minOperations(grid, x))  # Output: 4
