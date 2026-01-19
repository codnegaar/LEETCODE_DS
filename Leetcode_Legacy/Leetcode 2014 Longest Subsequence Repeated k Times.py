'''
Leetcode 2014 Longest Subsequence Repeated k Times

You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.
For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

Example 1:
        example 1
        Input: s = "letsleetcode", k = 2
        Output: "let"
        Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
        "let" is the lexicographically largest one.

Example 2:
        Input: s = "bb", k = 2
        Output: "b"
        Explanation: The longest subsequence repeated 2 times is "b".

Example 3:
        Input: s = "ab", k = 2
        Output: ""
        Explanation: There is no subsequence repeated 2 times. Empty string is returned.
         
Constraints:
        n == s.length
        2 <= n, k <= 2000
        2 <= n < k * 8
        s consists of lowercase English letters.
'''
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid = sorted([ch for ch in freq if freq[ch] >= k], reverse=True)
        
        def is_subseq(x):
            t = x * k
            i = 0
            for ch in s:
                if i < len(t) and ch == t[i]:
                    i += 1
            return i == len(t)
        
        queue = deque([""])
        res = ""
        
        while queue:
            curr = queue.popleft()
            for ch in valid:
                next_candidate = curr + ch
                if is_subseq(next_candidate):
                    if len(next_candidate) > len(res) or (len(next_candidate) == len(res) and next_candidate > res):
                        res = next_candidate
                    queue.append(next_candidate)
        
        return res
