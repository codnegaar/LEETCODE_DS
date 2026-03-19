'''
Leetcode 3212 Count Submatrices With Equal Frequency of X and Y
 
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
        grid[0][0]
        an equal frequency of 'X' and 'Y'.
        at least one 'X'. 

Example 1:
        Input: grid = [["X","Y","."],["Y",".","."]]
        Output: 3
        Explanation:

Example 2:
        Input: grid = [["X","X"],["X","Y"]]
        Output: 0
        Explanation: No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:
        Input: grid = [[".","."],[".","."]]
        Output: 0        
        Explanation:
        No submatrix has at least one 'X'. 

Constraints:
        1 <= grid.length, grid[i].length <= 1000
        grid[i][j] is either 'X', 'Y', or '.'.
'''


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]], ans = 0) -> int:

        n = len(grid[0])
        X, Y = [0] * n, [0] * n

        for row in grid:
            rowX, rowY = 0, 0

            for j in range(n):

                rowX+= (row[j] == 'X')
                rowY+= (row[j] == 'Y')

                X[j]+= rowX
                Y[j]+= rowY

                ans+= (X[j] > 0) & (X[j] == Y[j])

        return ans        
