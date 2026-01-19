'''
Leetcode 1930 Unique Length-3 Palindromic Subsequences

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:
        Input: s = "aabca"
        Output: 3
        Explanation: The 3 palindromic subsequences of length 3 are:
        - "aba" (subsequence of "aabca")
        - "aaa" (subsequence of "aabca")
        - "aca" (subsequence of "aabca")

Example 2:
          Input: s = "adc"
          Output: 0
          Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
        Input: s = "bbcbaba"
        Output: 4
        Explanation: The 4 palindromic subsequences of length 3 are:
        - "bbb" (subsequence of "bbcbaba")
        - "bcb" (subsequence of "bbcbaba")
        - "bab" (subsequence of "bbcbaba")
        - "aba" (subsequence of "bbcbaba")


Constraints:
        3 <= s.length <= 105
        s consists of only lowercase English letters.
'''
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Count the number of unique palindromic subsequences that can be formed in the string.

        A palindromic subsequence is a sequence that reads the same forward and backward.

        Args:
        s (str): The input string.

        Returns:
        int: The number of unique palindromic subsequences.
        """
        
        # Create a dictionary to store the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}

        # Traverse the string to record first and last occurrence of each character
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        # Initialize answer counter
        ans = 0
        
        # Traverse each character in the string
        for char in first_occurrence:
            # If the first and last occurrence of the character are far enough apart
            if last_occurrence[char] > first_occurrence[char]:
                # Collect the characters between the first and last occurrence
                seen = set(s[first_occurrence[char] + 1 : last_occurrence[char]])

                # Count the unique characters between the occurrences
                ans += len(seen)
        
        return ans


