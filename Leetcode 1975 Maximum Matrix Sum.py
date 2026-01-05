'''
Leetcode 1975 Maximum Matrix Sum

You are given an n x n integer matrix. You can do the following operation any number of times:
        Choose any two adjacent elements of matrix and multiply each of them by -1.
        Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
          Input: matrix = [[1,-1],[-1,1]]
          Output: 4
          Explanation: We can follow the following steps to reach sum equals 4:
          - Multiply the 2 elements in the first row by -1.
          - Multiply the 2 elements in the first column by -1.
          
Example 2:
        Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
        Output: 16
        Explanation: We can follow the following step to reach sum equals 16:
        - Multiply the 2 last elements in the second row by -1.
 
Constraints:
        n == matrix.length == matrix[i].length
        2 <= n <= 250
        -105 <= matrix[i][j] <= 105
'''

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Calculates the maximum possible matrix sum after flipping signs of elements any number of times.

        Parameters:
        - matrix (List[List[int]]): A 2D list of integers representing the matrix.

        Returns:
        - int: The maximum sum achievable after any number of sign flips.
        """
        total_sum = 0  # To store the sum of absolute values of all elements
        min_abs_value = float('inf')  # Minimum absolute value in the matrix
        negative_count = 0  # Count of negative numbers

        # Iterate through the matrix to calculate required values
        for row in matrix:
            for val in row:
                total_sum += abs(val)  # Add absolute value to the total sum
                min_abs_value = min(min_abs_value, abs(val))  # Track the smallest absolute value
                if val < 0:
                    negative_count += 1  # Count negative numbers

        # If there is an odd count of negative numbers, adjust the sum
        # Subtract twice the smallest absolute value to account for the unavoidable negative
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum
