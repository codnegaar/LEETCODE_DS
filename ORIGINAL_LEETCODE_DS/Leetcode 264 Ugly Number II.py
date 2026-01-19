'''


264 Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
 
Example 1:
        Input: n = 10
        Output: 12
        Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
        
Example 2:
        Input: n = 1
        Output: 1
        Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
Constraints:
        1 <= n <= 1690

'''
class Solution:
  def nthUglyNumber(self, n: int) -> int:
    nums = [1]
    i2 = 0
    i3 = 0
    i5 = 0

    while len(nums) < n:
      next2 = nums[i2] * 2
      next3 = nums[i3] * 3
      next5 = nums[i5] * 5
      next = min(next2, next3, next5)
      if next == next2:
        i2 += 1
      if next == next3:
        i3 += 1
      if next == next5:
        i5 += 1
      nums.append(next)

    return nums[-1]
