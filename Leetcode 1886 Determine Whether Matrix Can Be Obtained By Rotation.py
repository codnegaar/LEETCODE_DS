'''
Leetcode 1886 Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
        Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
        Output: true
        Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
        Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
        Output: false
        Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
        Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
        Output: true
        Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.

'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 0, 90, 180, 270
        possible = [True, True, True, True]
        
        for i in range(n):
            for j in range(n):
                # Check 0 rotation: mat[i][j] should = target[i][j]
                if mat[i][j] != target[i][j]:
                    possible[0] = False
                
                # Check 90 rotation: mat[i][j] should = target[j][n-1-i]
                if mat[i][j] != target[j][n-1-i]:
                    possible[1] = False
                
                # Check 180 rotation: mat[i][j] should = target[n-1-i][n-1-j]
                if mat[i][j] != target[n-1-i][n-1-j]:
                    possible[2] = False
                
                # Check 270 rotation: mat[i][j] should  target[n-1-j][i]
                if mat[i][j] != target[n-1-j][i]:
                    possible[3] = False
                
                # Early exit if all possibilities are eliminated
                if not any(possible):
                    return False
        
        return any(possible)
