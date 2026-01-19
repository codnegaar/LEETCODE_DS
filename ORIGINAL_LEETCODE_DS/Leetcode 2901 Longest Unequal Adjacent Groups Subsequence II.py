'''
Leetcode 2901 Longest Unequal Adjacent Groups Subsequence II

You are given a string array words, and an array groups, both arrays having length n.
The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.
You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.
Note: strings in words may be unequal in length. 

Example 1:
        Input: words = ["bab","dab","cab"], groups = [1,2,2]
        Output: ["bab","cab"]
        Explanation: A subsequence that can be selected is [0,2].
        groups[0] != groups[2]
        words[0].length == words[2].length, and the hamming distance between them is 1.
        So, a valid answer is [words[0],words[2]] = ["bab","cab"].
        Another subsequence that can be selected is [0,1].
        groups[0] != groups[1]
        words[0].length == words[1].length, and the hamming distance between them is 1.
        So, another valid answer is [words[0],words[1]] = ["bab","dab"].
        It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

Example 2:
        Input: words = ["a","b","c","d"], groups = [1,2,3,4]
        Output: ["a","b","c","d"]
        Explanation: We can select the subsequence [0,1,2,3].
        It satisfies both conditions.
        Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"].
        It has the longest length among all subsequences of indices that satisfy the conditions.
        Hence, it is the only answer. 

Constraints:        
        1 <= n == words.length == groups.length <= 1000
        1 <= words[i].length <= 10
        1 <= groups[i] <= n
        words consists of distinct strings.
        words[i] consists of lowercase English letters.

'''

from typing import List
from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Finds the longest subsequence of words such that:
        1. Each pair of adjacent words differs by exactly one character (Hamming distance of 1).
        2. No two adjacent words come from the same group.

        Parameters:
        - words: List[str] - A list of words (all words are of the same length).
        - groups: List[int] - A list indicating the group index of each word.

        Returns:
        - List[str]: The longest valid subsequence satisfying the conditions above.
        """
        def encode_word(word: str) -> int:
            """Encodes a word into an integer using base-32 positional bit shifting."""
            code = 0
            for i, ch in enumerate(word):
                code |= (ord(ch) - ord('a')) << (5 * i)  # 5 bits per character
            return code

        n = len(words)
        if n == 0:
            return []

        dp = [1] * n             # Longest subsequence ending at word i
        prev = [-1] * n          # Previous index in subsequence
        max_len = 1
        max_idx = 0

        # Mapping word lengths to wildcard pattern buckets for optimization
        pattern_buckets = {}     # key: length -> list of dicts for wildcard positions
        word_codes = [encode_word(word) for word in words]

        for i in range(n):
            length = len(words[i])
            group_i = groups[i]
            code_i = word_codes[i]

            # Initialize wildcard pattern buckets for this word length
            buckets = pattern_buckets.setdefault(length, [defaultdict(list) for _ in range(length)])

            best_len = 1
            best_prev = -1

            # Try replacing each character position with a wildcard (simulate Hamming distance 1)
            for pos in range(length):
                mask = ~(31 << (5 * pos))       # Mask out current character (5 bits)
                pattern = code_i & mask

                for j in buckets[pos].get(pattern, []):
                    if groups[j] != group_i and dp[j] + 1 > best_len:
                        best_len = dp[j] + 1
                        best_prev = j

            dp[i] = best_len
            prev[i] = best_prev

            # Register this word into the buckets using all wildcard positions
            for pos in range(length):
                mask = ~(31 << (5 * pos))
                pattern = code_i & mask
                buckets[pos].setdefault(pattern, []).append(i)

            # Track global max subsequence
            if best_len > max_len:
                max_len = best_len
                max_idx = i

        # Reconstruct longest subsequence
        result = []
        cur = max_idx
        while cur != -1:
            result.append(words[cur])
            cur = prev[cur]

        return result[::-1]
