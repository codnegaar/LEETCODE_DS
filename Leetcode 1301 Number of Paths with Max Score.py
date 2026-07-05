'''
Leetcode 1301 Number of Paths with Max Score

You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.
You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'.
In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
In case there is no path, return [0, 0]. 

Example 1:
        Input: board = ["E23","2X2","12S"]
        Output: [7,1]

Example 2:
        Input: board = ["E12","1X1","21S"]
        Output: [4,2]

Example 3:        
        Input: board = ["E11","XXX","11S"]
        Output: [0,0] 

Constraints:
        2 <= board.length == board[i].length <= 100
'''

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        dp = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        dp[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                count = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and dp[ni][nj] != -1:
                        if dp[ni][nj] > best:
                            best = dp[ni][nj]
                            count = ways[ni][nj]
                        elif dp[ni][nj] == best:
                            count = (count + ways[ni][nj]) % MOD

                if best == -1:
                    continue

                val = 0 if board[i][j] == 'E' else int(board[i][j])
                dp[i][j] = best + val
                ways[i][j] = count

        if ways[0][0] == 0:
            return [0, 0]

        return [dp[0][0] % MOD, ways[0][0]]
