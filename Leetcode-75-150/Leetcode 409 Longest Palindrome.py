'''
409 Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here. 

Example 1:
        Input: s = "abccccdd"
        Output: 7
        Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
        
Example 2:
        Input: s = "a"
        Output: 1
        Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
Constraints:
        1 <= s.length <= 2000
        s consists of lowercase and/or uppercase English letters only.

'''
class Solution:
  def longestPalindrome(self, s: str) -> int:
    ans = 0
    count = collections.Counter(s)

    for c in count.values():
      ans += c if c % 2 == 0 else c - 1

    hasOddCount = any(c % 2 == 1 for c in count.values())

    return ans + hasOddCount
