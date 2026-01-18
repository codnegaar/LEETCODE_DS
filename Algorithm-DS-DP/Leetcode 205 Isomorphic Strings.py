'''
Leetcode 205 Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

 

Example 1:
        Input: s = "egg", t = "add"
        Output: true

Example 2:
        Input: s = "foo", t = "bar"
        Output: false

Example 3:
        Input: s = "paper", t = "title"
        Output: true

Constraints:
        1 <= s.length <= 5 * 104
        t.length == s.length
        s and t consist of any valid ascii character.

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        st=[-1]*128
        ts=[-1]*128
        for i in range(n):
            cs, ct= s[i], t[i]
            _cs=ord(cs)
            _ct=ord(ct)
            if st[_cs]==-1 and ts[_ct]==-1:
                st[_cs]=ct
                ts[_ct]=cs
            elif st[_cs]!=ct or ts[_ct]!=cs:  
                return False
        return True


        
