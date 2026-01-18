'''
1143 Longest Common Subsequence
 
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing 
the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:
        Input: text1 = "abcde", text2 = "ace" 
        Output: 3  
        Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
        Input: text1 = "abc", text2 = "abc"
        Output: 3
        Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
        Input: text1 = "abc", text2 = "def"
        Output: 0
        Explanation: There is no such common subsequence, so the result is 0.
 
Constraints:
        1 <= text1.length, text2.length <= 1000
        text1 and text2 consist of only lowercase English characters.
'''

class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    # dp[i][j] := LCS's length of text1[0..i) and text2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        dp[i + 1][j + 1] = \
            1 + dp[i][j] if text1[i] == text2[j] \
            else max(dp[i][j + 1], dp[i + 1][j])

    return dp[m][n]


# Second Solution
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Calculates the length of the Longest Common Subsequence (LCS)
        between two input strings using dynamic programming with O(n) space.

        Parameters:
        text1 (str): First input string.
        text2 (str): Second input string.

        Returns:
        int: Length of the longest common subsequence between text1 and text2.
        """
        m, n = len(text1), len(text2)

        # Ensure text1 is the shorter string to optimize space usage
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m

        # prev: DP row for previous text1 character
        # curr: DP row for current text1 character
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr  # Move current row to previous for next iteration

        return prev[n]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    t1 = "abcde"
    t2 = "ace"
    print(f"LCS length between '{t1}' and '{t2}':", sol.longestCommonSubsequence(t1, t2))
    # Output: 3 (LCS = "ace")
