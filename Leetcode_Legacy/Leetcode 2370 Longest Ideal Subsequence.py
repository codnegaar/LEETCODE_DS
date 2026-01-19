'''
Leetcode 2370 Longest Ideal Subsequence

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
        
        t is a subsequence of the string s.
        The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
        Return the length of the longest ideal string.        
        A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.        
        Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
        
Example 1:
        Input: s = "acfgbd", k = 2
        Output: 4
        Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
        Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
        
Example 2:
        Input: s = "abcd", k = 3
        Output: 4
        Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
         
Constraints:
        1 <= s.length <= 105
        0 <= k <= 25
        s consists of lowercase English letters.

'''

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 27  # dp array to store the max length ending with each character

        for ch in reversed(s):  # reverse iterate to save on recalculating bounds
            idx = ord(ch) - ord('a')
            max_len = 0  # initialize max length as 0 for this character

            # Calculate bounds within valid character range
            left = max(idx - k, 0)
            right = min(idx + k, 26)

            # Find the maximum dp value within the window [left, right]
            for j in range(left, right + 1):
                max_len = max(max_len, dp[j])

            dp[idx] = max_len + 1  # update dp value for current character

        return max(dp)  # the result is the max value in dp array

