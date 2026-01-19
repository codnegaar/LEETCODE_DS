'''

Leetcode 1625 Lexicographically Smallest String After Applying Operations
 
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.
        You can apply either of the following two operations any number of times and in any order on s:
        Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
        Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
        Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter 
that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

 

Example 1:
        Input: s = "5525", a = 9, b = 2
        Output: "2050"
        Explanation: We can apply the following operations:
        Start:  "5525"
        Rotate: "2555"
        Add:    "2454"
        Add:    "2353"
        Rotate: "5323"
        Add:    "5222"
        Add:    "5121"
        Rotate: "2151"
        Add:    "2050"ΓÇïΓÇïΓÇïΓÇïΓÇï
        There is no way to obtain a string that is lexicographically smaller than "2050".

Example 2:
        Input: s = "74", a = 5, b = 1
        Output: "24"
        Explanation: We can apply the following operations:
        Start:  "74"
        Rotate: "47"
        ΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïAdd:    "42"
        ΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïRotate: "24"ΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇïΓÇï
        There is no way to obtain a string that is lexicographically smaller than "24".
        
Example 3:        
        Input: s = "0011", a = 4, b = 2
        Output: "0011"
        Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
 
Constraints:
        2 <= s.length <= 100
        s.length is even.
        s consists of digits from 0 to 9 only.
        1 <= a <= 9
        1 <= b <= s.length - 1
'''

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        vis = set([s])
        smallest = s
        q = [s]

        while q:
            cur = q.pop(0)
            if cur < smallest:
                smallest = cur

            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)
            if added not in vis:
                vis.add(added)
                q.append(added)

            rotated = cur[-b:] + cur[:-b]
            if rotated not in vis:
                vis.add(rotated)
                q.append(rotated)

        return smallest
