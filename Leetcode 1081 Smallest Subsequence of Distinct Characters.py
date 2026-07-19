'''
Leetcode 1081 Smallest Subsequence of Distinct Characters
 
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once. 

Example 1:
        Input: s = "bcabc"
        Output: "abc"

Example 2:
        Input: s = "cbacdcbc"
        Output: "acdb"
 
Constraints:
        1 <= s.length <= 1000
        s consists of lowercase English letters.
'''

class Solution:
    def smallestSubsequence(self, s: str) -> str:

        freq = Counter(s)
        vis = set()
        st = []

        for c in s:

            freq[c] -= 1

            if c in vis:
                continue

            while st and st[-1] > c and freq[st[-1]]:

                vis.remove(st.pop())

            st.append(c)
            vis.add(c)

        return "".join(st)
