'''
221 Maximal Square
 
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

'''

class Solution:
  def maximalSquare(self, matrix: List[List[chr]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    dp = [0] * n
    maxLength = 0
    prev = 0  # dp[i - 1][j - 1]

    for i in range(m):
      for j in range(n):
        cache = dp[j]
        if i == 0 or j == 0 or matrix[i][j] == '0':
          dp[j] = 1 if matrix[i][j] == '1' else 0
        else:
          dp[j] = min([prev, dp[j], dp[j - 1]]) + 1
        maxLength = max(maxLength, dp[j])
        prev = cache

    return maxLength * maxLength


# second solution
from typing import List

class Solution:
    """
    A class to generate all combinations of well-formed parentheses for a given n.
    """

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all possible combinations of n pairs of well-formed parentheses.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            List[str]: A list of valid parentheses combinations.
        """
        res = []  # Stores the valid combinations

        def dfs(open_count: int, close_count: int, current: str):
            """
            Uses depth-first search (DFS) to generate valid parentheses.

            Args:
                open_count (int): The number of open parentheses used so far.
                close_count (int): The number of close parentheses used so far.
                current (str): The current sequence of parentheses.
            """
            if len(current) == n * 2:  # Base case: if the sequence is complete
                res.append(current)
                return
            
            if open_count < n:  # Add an open parenthesis if limit not reached
                dfs(open_count + 1, close_count, current + "(")
            
            if close_count < open_count:  # Add a closing parenthesis if valid
                dfs(open_count, close_count + 1, current + ")")

        dfs(0, 0, "")  # Start DFS

        return res


# Example usage
solution = Solution()
print(solution.generateParenthesis(3))

