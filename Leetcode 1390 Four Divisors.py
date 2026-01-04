'''
Leetcode 1390 Four Divisors

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

Example 1:
        Input: nums = [21,4,7]
        Output: 32
        Explanation: 
                    21 has 4 divisors: 1, 3, 7, 21
                    4 has 3 divisors: 1, 2, 4
                    7 has 2 divisors: 1, 7
                    The answer is the sum of divisors of 21 only.

Example 2:
        Input: nums = [21,21]
        Output: 64

Example 3:
        Input: nums = [1,2,3,4,5]
        Output: 0 

Constraints:
        1 <= nums.length <= 104
        1 <= nums[i] <= 105

'''

from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_div_sum(n: int) -> int:
            s = 0
            cnt = 0

            for d in range(1, int(n ** 0.5) + 1):
                if n % d == 0:
                    d2 = n // d

                    cnt += 1
                    s += d
                    if d != d2:
                        cnt += 1
                        s += d2

                    if cnt > 4:
                        return 0

            return s if cnt == 4 else 0

        return sum(four_div_sum(n) for n in nums)
