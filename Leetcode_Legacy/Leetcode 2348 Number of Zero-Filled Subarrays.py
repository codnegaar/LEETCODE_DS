'''
Leetcode 2348 Number of Zero-Filled Subarrays
 
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
        Input: nums = [1,3,0,0,2,0,0,4]
        Output: 6
        Explanation: 
        There are 4 occurrences of [0] as a subarray.
        There are 2 occurrences of [0,0] as a subarray.
        There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:
        Input: nums = [0,0,0,2,0,0]
        Output: 9
        Explanation:
        There are 5 occurrences of [0] as a subarray.
        There are 3 occurrences of [0,0] as a subarray.
        There is 1 occurrence of [0,0,0] as a subarray.
        There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
        
Example 3:
        Input: nums = [2,10,2019]
        Output: 0
        Explanation: There is no subarray filled with 0. Therefore, we return 0.
         
Constraints:
        1 <= nums.length <= 105
        -109 <= nums[i] <= 109

'''

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Count the total number of subarrays filled with only zeros.

        Parameters:
        ----------
        nums : List[int]
            A list of integers which may contain zeros and non-zero integers.

        Returns:
        -------
        int
            The total number of contiguous subarrays consisting only of zeros.
        """

        return self._count_zero_subarrays(nums)

    def _count_zero_subarrays(self, nums: List[int]) -> int:
        """
        Helper function to compute the number of zero-filled subarrays.

        Parameters:
        ----------
        nums : List[int]
            The input list of integers.

        Returns:
        -------
        int
            Count of zero-filled subarrays.
        """
        zero_count = 0     # Tracks consecutive zeros
        total_subarrays = 0  # Accumulates total zero-filled subarrays

        for num in nums:
            if num == 0:
                zero_count += 1  # Increase count for consecutive zeros
            else:
                # When sequence of zeros ends, calculate subarrays
                total_subarrays += self._subarray_combinations(zero_count)
                zero_count = 0   # Reset count for next sequence

        # Handle any trailing zeros in the list
        total_subarrays += self._subarray_combinations(zero_count)

        return total_subarrays

    @staticmethod
    def _subarray_combinations(length: int) -> int:
        """
        Calculates the number of subarrays that can be formed from
        a sequence of 'length' zeros using the formula n(n+1)/2.

        Parameters:
        ----------
        length : int
            The length of a contiguous zero sequence.

        Returns:
        -------
        int
            Total subarrays that can be formed.
        """
        return (length * (length + 1)) // 2 if length > 0 else 0
