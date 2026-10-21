'''
Leetcode 3863 Minimum Operations to Sort a String

You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"

Output: 1

Explanation:​​​​​​​

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
Example 2:

Input: s = "card"

Output: 2

Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
Example 3:

Input: s = "gf"

Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

'''

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        flag = True

        for i in range(n):
            if i > 0 and s[i] < s[i - 1]:
                flag = False
                break

        if flag:
            return 0

        if n == 2:
            return -1

        minChar = 'z'
        maxChar = 'a'

        for ch in s:
            minChar = min(minChar, ch)
            maxChar = max(maxChar, ch)

        if minChar == s[0] or maxChar == s[n - 1]:
            return 1

        for i in range(1, n - 1):
            if s[i] == minChar or s[i] == maxChar:
                return 2

        return 3
