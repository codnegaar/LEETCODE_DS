'''

1074. Number of Submatrices That Sum to Target

Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
        Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
        Output: 4
        Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
        Input: matrix = [[1,-1],[-1,1]], target = 0
        Output: 5
        Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
        Input: matrix = [[904]], target = 0
        Output: 0

Constraints:
        1 <= matrix.length <= 100
        1 <= matrix[0].length <= 100
        -1000 <= matrix[i][j] <= 1000
        -10^8 <= target <= 10^8

'''

from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        xlen, ylen = len(matrix[0]), len(matrix)
        ans = 0
        
        # Compute the prefix sums for each row
        for row in matrix:
            for j in range(1, xlen):
                row[j] += row[j - 1]

        # Iterate over all pairs of columns
        for j in range(xlen):
            for k in range(j, xlen):
                res = defaultdict(int)
                res[0] = 1
                csum = 0
                
                # Calculate the sum of submatrixes between columns j and k for each row
                for i in range(ylen):
                    csum += matrix[i][k] - (matrix[i][j - 1] if j > 0 else 0)
                    ans += res[csum - target]
                    res[csum] += 1
        
        return ans


