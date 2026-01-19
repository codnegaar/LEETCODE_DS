'''
Leetcode 1072 Flip Columns For Maximum Number of Equal Rows

You are given an m x n binary matrix matrix.
You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the cell's value from 0 to 1 or vice versa).
Return the maximum number of rows that have all values equal after some number of flips.

Example 1:
        Input: matrix = [[0,1],[1,1]]
        Output: 1
        Explanation: After flipping no values, 1 row has all values equal.

Example 2:
        Input: matrix = [[0,1],[1,0]]
        Output: 2
        Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
        Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
        Output: 2
        Explanation: After flipping values in the first two columns, the last two rows have equal values.
         
Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 300
        matrix[i][j] is either 0 or 1.
'''

from collections import defaultdict
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        Calculates the maximum number of rows that can be made identical by flipping any number
        of columns any number of times.

        Parameters:
        matrix (List[List[int]]): A 2D list consisting of rows of binary integers (0 or 1).
        
        Returns:
        int: The maximum number of identical rows obtainable by flipping columns.
        """
        # Initialize a defaultdict to store patterns and their occurrence counts.
        pattern_count = defaultdict(int)

        # Iterate over each row to determine the unique pattern it corresponds to
        for row in matrix:
            # Generate a normalized pattern where the first element becomes 0.
            # This is done by XOR-ing every element with the first element of the row.
            base_pattern = tuple(x ^ row[0] for x in row)
            
            # Increment the count for this pattern
            pattern_count[base_pattern] += 1

        # Return the highest frequency pattern as the result
        return max(pattern_count.values())

