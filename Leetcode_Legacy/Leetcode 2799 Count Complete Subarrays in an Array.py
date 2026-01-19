'''
Leetcode 2799 Count Complete Subarrays in an Array

You are given an array nums consisting of positive integers.
We call a subarray of an array complete if the following condition is satisfied:
The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.
A subarray is a contiguous non-empty part of an array.

Example 1:
        Input: nums = [1,3,1,2,2]
        Output: 4
        Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

Example 2:
        Input: nums = [5,5,5,5]
        Output: 10
        Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
         
Constraints:
        1 <= nums.length <= 1000
        1 <= nums[i] <= 2000

'''
from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        Count the number of complete subarrays in the given list.
        A complete subarray contains all distinct elements present in the entire array.

        Parameters:
        nums (List[int]): The input list of integers.

        Returns:
        int: The number of complete subarrays.
        """
        total_unique = len(set(nums))  # Total distinct elements in the entire list
        freq = defaultdict(int)        # Frequency of elements in the current window
        left = 0                       # Left pointer for sliding window
        count = 0                      # Final result
        current_unique = 0            # Number of unique elements in current window

        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1

            # First time seeing this element in the window
            if freq[num] == 1:
                current_unique += 1

            # Try to shrink the window while it still contains all unique elements
            while current_unique == total_unique:
                count += len(nums) - right  # All subarrays starting from left to end are valid

                # Remove leftmost element from window
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    current_unique -= 1
                left += 1

        return count
