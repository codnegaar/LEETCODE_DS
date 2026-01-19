'''
Leetcode 1015 Smallest Integer Divisible by K

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
Return the length of n. If there is no such n, return -1.
Note: n may not fit in a 64-bit signed integer. 

Example 1:
        Input: k = 1
        Output: 1
        Explanation: The smallest answer is n = 1, which has length 1.

Example 2:
        Input: k = 2
        Output: -1
        Explanation: There is no such positive integer n divisible by 2.

Example 3:
        Input: k = 3
        Output: 3
        Explanation: The smallest answer is n = 111, which has length 3.         

Constraints:
        1 <= k <= 105

'''

class Solution:
  def smallestRepunitDivByK(self, k: int) -> int:
    if k % 10 not in {1, 3, 7, 9}:
      return -1

    seen = set()
    n = 0

    for length in range(1, k + 1):
      n = (n * 10 + 1) % k
      if n == 0:
        return length
      if n in seen:
        return -1
      seen.add(n)

    return -1
