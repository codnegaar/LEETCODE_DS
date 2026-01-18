'''
Leeetcode 1525. Number of Good Ways to Split a String
A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal
to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.Return the number of
good splits you can make in s. 

Example 1:
            Input: s = "aacaba"
            Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
            ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
            ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
            ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
            ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
            ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
            Example 2:

Input: s = "abcd"
            Output: 1
            Explanation: Split the string as follows ("ab", "cd").

'''
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        seen = set()
        
        sleft = [0] * n
        sright  = [0] * n

        for i in range(n):
            seen.add(s[i])
            sleft[i] = len(seen)

        seen.clear()

        for i in reversed(range(n)):
            seen.add(s[i])
            sright [i] = len(seen)

        for i in range(n - 1):
            if sleft[i] == sright [i + 1]:
                ans += 1

        return ans
