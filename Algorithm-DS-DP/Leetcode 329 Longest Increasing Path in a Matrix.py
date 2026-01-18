'''
329 Longest Increasing Path in a Matrix
Given an m x n integers matrix, return the length of the longest increasing path in the matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
        Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
        Output: 4
        Explanation: The longest increasing path is [1, 2, 6, 9].
        
Example 2:
        Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
        Output: 4
        Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
        
Example 3:
        Input: matrix = [[1]]
        Output: 1
 
Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 200
        0 <= matrix[i][j] <= 231 - 1

'''
class Solution:
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])

    @functools.lru_cache(None)
    def dfs(i: int, j: int, prev: int) -> int:
      if i < 0 or i == m or j < 0 or j == n:
        return 0
      if matrix[i][j] <= prev:
        return 0

      curr = matrix[i][j]
      return 1 + max(dfs(i + 1, j, curr),
                     dfs(i - 1, j, curr),
                     dfs(i, j + 1, curr),
                     dfs(i, j - 1, curr))

    return max(dfs(i, j, -math.inf) for i in range(m) for j in range(n))
