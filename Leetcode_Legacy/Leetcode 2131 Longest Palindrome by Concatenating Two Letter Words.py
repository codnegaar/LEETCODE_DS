'''
Leetcode 2131 Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward. 

Example 1:
        Input: words = ["lc","cl","gg"]
        Output: 6
        Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
        Note that "clgglc" is another longest palindrome that can be created.

Example 2:
        Input: words = ["ab","ty","yt","lc","cl","ab"]
        Output: 8
        Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
        Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
        Input: words = ["cc","ll","xx"]
        Output: 2
        Explanation: One longest palindrome is "cc", of length 2.
        Note that "ll" is another longest palindrome that can be created, and so is "xx".
         
Constraints:
        1 <= words.length <= 105
        words[i].length == 2
        words[i] consists of lowercase English letters.
'''

from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        Finds the length of the longest palindrome that can be built from a list of 2-letter words.
        
        Parameters:
        words (List[str]): A list of 2-letter lowercase English words.
        
        Returns:
        int: The maximum length of a palindrome that can be formed.
        """
        freq = Counter(words)  # Count frequency of each word
        palindrome_length = 0  # Total length of the resulting palindrome
        has_center = False     # Track if we can place a symmetric word in the middle

        for word, count in freq.items():
            # Case 1: word is symmetric like "aa", "bb"
            if word[0] == word[1]:
                # Use as many pairs of such words as possible
                palindrome_length += (count // 2) * 4
                # If there's one left, it can potentially go in the center
                if count % 2 == 1:
                    has_center = True
            # Case 2: non-symmetric pairs, only process one direction to avoid duplicates
            elif word[0] < word[1]:
                reversed_word = word[::-1]
                # Add 4 characters for every valid matching pair
                palindrome_length += min(count, freq.get(reversed_word, 0)) * 4

        # Add center if any symmetric word is available
        if has_center:
            palindrome_length += 2

        return palindrome_length

