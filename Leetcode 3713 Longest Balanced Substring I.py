'''
Leetcode 3713 Longest Balanced Substring I

You are given a string s consisting of lowercase English letters.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s. 

Example 1:
        Input: s = "abbac"
        Output: 4
        Explanation: The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:
        Input: s = "zzabccy"
        Output: 4
        Explanation: The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

Example 3:
        Input: s = "aba"
        Output: 2
        Explanation: ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
        
Constraints:
        1 <= s.length <= 1000
        s consists of lowercase English letters.
'''

class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt, n=1, len(s)
        for l in range(n):
            freq=[0]*26
            uniq, maxF, cntMax=0, 0, 0
            for r in range(l, n):
                freq[ord(s[r])-97]+=1
                f=freq[ord(s[r])-97]
                uniq+=f==1
                if f>maxF:
                    maxF=f
                    cntMax=1
                elif f==maxF:
                    cntMax+=1
                if uniq==cntMax:
                    cnt=max(cnt, r-l+1)
        return cnt
