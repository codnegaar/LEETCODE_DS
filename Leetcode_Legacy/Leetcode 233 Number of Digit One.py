'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
 
Example 1:
        Input: n = 13
        Output: 6
        
Example 2:
        Input: n = 0
        Output: 0 

Constraints:
        0 <= n <= 109
'''
class Solution:
  def countDigitOne(self, n: int) -> int:
    ans = 0

    pow10 = 1
    while pow10 <= n:
      divisor = pow10 * 10
      quotient = n // divisor
      remainder = n % divisor
      if quotient > 0:
        ans += quotient * pow10
      if remainder >= pow10:
        ans += min(remainder - pow10 + 1, pow10)
      pow10 *= 10

    return ans
