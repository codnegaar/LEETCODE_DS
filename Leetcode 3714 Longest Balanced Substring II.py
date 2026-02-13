'''

Leetcode 3714 Longest Balanced Substring II
 
You are given a string s consisting only of the characters 'a', 'b', and 'c'.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s. 

Example 1:
        Input: s = "abbac"
        Output: 4
        Explanation: The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:
        Input: s = "aabcc"
        Output: 3
        Explanation: The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:
        Input: s = "aba"
        Output: 2
        Explanation: One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

Constraints:
        1 <= s.length <= 105
        s contains only the characters 'a', 'b', and 'c'.
'''

class Solution:
    def mono(self, s: str) -> int:
        if not s:
            return 0
        cnt = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans

    def duo(self, s: str, c1: str, c2: str) -> int:
        pos: Dict[int, int] = {0: -1}
        ans = 0
        delta = 0
        for i, ch in enumerate(s):
            if ch != c1 and ch != c2:
                pos.clear()
                pos[0] = i
                delta = 0
                continue

            if ch == c1:
                delta += 1
            else:
                delta -= 1

            if delta in pos:
                ans = max(ans, i - pos[delta])
            else:
                pos[delta] = i

        return ans

    def trio(self, s: str) -> int:
        cnt0 = cnt1 = cnt2 = 0  
        pos: Dict[Tuple[int, int], int] = {(0, 0): -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                cnt0 += 1
            elif ch == 'b':
                cnt1 += 1
            else:  
                cnt2 += 1

            key = (cnt1 - cnt0, cnt2 - cnt0)

            if key in pos:
                ans = max(ans, i - pos[key])
            else:
                pos[key] = i

        return ans

    def longestBalanced(self, s: str) -> int:
        return max(
            self.mono(s),
            self.duo(s, 'a', 'b'),
            self.duo(s, 'a', 'c'),
            self.duo(s, 'b', 'c'),
            self.trio(s),
        )
