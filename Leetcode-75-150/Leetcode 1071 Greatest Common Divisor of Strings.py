'''
1071 Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. 

Example 1:
        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"

Example 2:
        Input: str1 = "ABABAB", str2 = "ABAB"
        Output: "AB"

Example 3:
        Input: str1 = "LEET", str2 = "CODE"
        Output: ""
 

Constraints:
        1 <= str1.length, str2.length <= 1000
        str1 and str2 consist of English uppercase letters.
'''
class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    def mod(s1: str, s2: str) -> str:
      while s1.startswith(s2):
        s1 = s1[len(s2):]
      return s1

    if len(str1) < len(str2):
      return self.gcdOfStrings(str2, str1)
    if not str1.startswith(str2):
      return ''
    if not str2:
      return str1
    return self.gcdOfStrings(str2, mod(str1, str2))

  
  # Second Sollution
  class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1=len(str1)
    len2=len(str2)

    def isDivisor(l):
      if len1 % l or len2 % l:
        return False
      f1, f2 = len1 //l, len2 //l
      return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

    for l in range(min(len1,len2), 0, -1):
      if isDivisor(l):
        return str1[:l]
    return  ""


