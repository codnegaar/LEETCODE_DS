'''

1456 Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'. 

Example 1:
        Input: s = "abciiidef", k = 3
        Output: 3
        Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
        Input: s = "aeiou", k = 2
        Output: 2
        Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
        Input: s = "leetcode", k = 3
        Output: 2
        Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:
        1 <= s.length <= 105
        s consists of lowercase English letters.
        1 <= k <= s.length
'''
class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    ans = 0
    maxi = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i, c in enumerate(s):
      if c in vowels:
        maxi += 1
      if i >= k and s[i - k] in vowels:
        maxi -= 1
      ans = max(ans, maxi)

    return ans


# Second soluion:
class Solution(object):
    def longestOnes(self, nums, k):
      l = max_consequence = 0

      for r, num in enumerate(nums):
        k -= 1 - num

        if k < 0:
          k += 1 - nums[l]
          l += 1
        else:
            max_consequence = max(max_consequence, r-l +1)
      return max_consequence
  
 

