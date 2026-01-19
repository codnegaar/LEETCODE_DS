'''
Leetcode 1092 Shortest Common Supersequence 

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
        Input: str1 = "abac", str2 = "cab"
        Output: "cabac"
        Explanation: 
        str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
        str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
        The answer provided is the shortest such string that satisfies these properties.

Example 2:
        Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
        Output: "aaaaaaaa"
 
Constraints:
        1 <= str1.length, str2.length <= 1000
        str1 and str2 consist of lowercase English letters.
'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1: Find the longest common subsequence using dynamic programming
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Step 2: Construct the shortest common supersequence
        # Start from the bottom right of the dp table
        i, j = m, n
        result = []
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                # If the characters are the same, add it once
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                # If coming from top has higher value, take character from str1
                result.append(str1[i-1])
                i -= 1
            else:
                # Otherwise, take character from str2
                result.append(str2[j-1])
                j -= 1
        
        # Add remaining characters from str1 (if any)
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        
        # Add remaining characters from str2 (if any)
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        # Reverse the result to get the final supersequence
        return ''.join(result[::-1])
