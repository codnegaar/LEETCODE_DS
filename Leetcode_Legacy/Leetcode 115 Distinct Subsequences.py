'''

Leetcode 115 Distinct Subsequences
 
Given two strings s and t, return the number of distinct 
subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer. 

Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
                As shown below, there are 3 ways you can generate "rabbit" from s.
                rabbbit
                rabbbit
                rabbbit

Example 2:
        Input: s = "babgbag", t = "bag"
        Output: 5
        Explanation:
        As shown below, there are 5 ways you can generate "bag" from s.
        babgbag
        babgbag
        babgbag
        babgbag
        babgbag
 

Constraints:
        1 <= s.length, t.length <= 1000
        s and t consist of English letters.
'''

class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    dp = [1] + [0] * n

    for i in range(1, m + 1):
      for j in range(n, 1 - 1, -1):
        if s[i - 1] == t[j - 1]:
          dp[j] += dp[j - 1]

    return dp[n]





