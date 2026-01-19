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
        def get_sum_if_four_divisors(number: int) -> int:
            divisor_count = 0
            divisor_sum = 0

            for divisor in range(1, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    paired_divisor = number // divisor

                    divisor_count += 1
                    divisor_sum += divisor

                    if paired_divisor != divisor:
                        divisor_count += 1
                        divisor_sum += paired_divisor

                    if divisor_count > 4:
                        return 0

            return divisor_sum if divisor_count == 4 else 0

        return sum(get_sum_if_four_divisors(num) for num in nums)

