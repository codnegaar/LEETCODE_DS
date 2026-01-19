'''
Leetcode 1380 Lucky Numbers in a Matrix

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and the maximum in its column.

Example 1:
        Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
        Output: [15]
        Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
        Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
        Output: [12]
        Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
        Input: matrix = [[7,8],[1,2]]
        Output: [7]
        Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column. 

Constraints:
        m == mat.length
        n == mat[i].length
        1 <= n, m <= 50
        1 <= matrix[i][j] <= 105.
        All elements in the matrix are distinct.

'''
from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        # Find the maximum value among the minimum values of each row
        row_min_max = max(min(row) for row in matrix)
        
        # Find the minimum value among the maximum values of each column
        col_max_min = min(max(col) for col in zip(*matrix))
        
        # If the values match, return the lucky number; otherwise, return an empty list
        return [row_min_max] if row_min_max == col_max_min else []
