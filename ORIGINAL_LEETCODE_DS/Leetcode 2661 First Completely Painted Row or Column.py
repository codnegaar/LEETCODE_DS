'''
Leetcode 2661 First Completely Painted Row or Column

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
Return the smallest index i at which either a row or a column will be completely painted in mat.

Example 1:
        image explanation for example 1
        Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
        Output: 2
        Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

Example 2:
        image explanation for example 2
        Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
        Output: 3
        Explanation: The second column becomes fully painted at arr[3].
         

Constraints:        
        m == mat.length
        n = mat[i].length
        arr.length == m * n
        1 <= m, n <= 105
        1 <= m * n <= 105
        1 <= arr[i], mat[r][c] <= m * n
        All the integers of arr are unique.
        All the integers of mat are unique.

'''
from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        Find the first index in `arr` such that marking the elements in `mat` results in
        a completely marked row or column.

        Parameters:
        arr (List[int]): The sequence in which elements of the matrix are marked.
        mat (List[List[int]]): The matrix to be marked.

        Returns:
        int: The index in `arr` where a row or column is completely marked.
        """
        R, C = len(mat), len(mat[0])  # Dimensions of the matrix
        value_to_position = {}  # Map matrix values to their positions
        
        # Map matrix values to their row and column indices
        for row in range(R):
            for col in range(C):
                value_to_position[mat[row][col]] = (row, col)

        # Counters to track marked cells in each row and column
        row_counts = [0] * R
        col_counts = [0] * C

        # Process the sequence in `arr`
        for index, value in enumerate(arr):
            row, col = value_to_position[value]  # Get the position of the current value
            row_counts[row] += 1
            col_counts[col] += 1

            # Check if the current row or column is fully marked
            if row_counts[row] == C or col_counts[col] == R:
                return index

        return -1  # Return -1 if no row or column is fully marked
