'''
Leetcode 2342 Max Sum of a Pair With Equal Sum of Digits

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

Example 1:
        Input: nums = [18,43,36,13,7]
        Output: 54
        Explanation: The pairs (i, j) that satisfy the conditions are:
        - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
        - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
        So the maximum sum that we can obtain is 54.

Example 2:
        Input: nums = [10,12,19,14]
        Output: -1
        Explanation: There are no two numbers that satisfy the conditions, so we return -1.
         

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109

'''

from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of two numbers in the array such that they have the same digit sum.

        Parameters:
        nums (List[int]): A list of positive integers.

        Returns:
        int: The maximum sum of two numbers having the same digit sum, or -1 if no such pair exists.
        """
        # Dictionary to store the largest number for each digit sum
        max_dict = {}
        max_sum = -1  # Initialize result as -1 (default case)

        for num in nums:
            # Calculate the digit sum of the current number
            digit_sum = sum(int(d) for d in str(num))

            # If there is already a number with this digit sum, update max_sum
            if digit_sum in max_dict:
                max_sum = max(max_sum, num + max_dict[digit_sum])

            # Update the largest number for this digit sum
            max_dict[digit_sum] = max(max_dict.get(digit_sum, 0), num)

        return max_sum


