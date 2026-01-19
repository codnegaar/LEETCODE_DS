'''
Leetcode 2461 Maximum Sum of Distinct Subarrays With Length K

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
        Input: nums = [1,5,4,2,9,9,9], k = 3
        Output: 15
        Explanation: The subarrays of nums with length 3 are:
        - [1,5,4] which meets the requirements and has a sum of 10.
        - [5,4,2] which meets the requirements and has a sum of 11.
        - [4,2,9] which meets the requirements and has a sum of 15.
        - [2,9,9] which does not meet the requirements because the element 9 is repeated.
        - [9,9,9] which does not meet the requirements because the element 9 is repeated.
        We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
        Input: nums = [4,4,4], k = 3
        Output: 0
        Explanation: The subarrays of nums with length 3 are:
        - [4,4,4] which does not meet the requirements because the element 4 is repeated.
        We return 0 because no subarrays meet the conditions.
         
Constraints:
        1 <= k <= nums.length <= 105
        1 <= nums[i] <= 105
'''

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum sum of any subarray of length k without duplicate elements.

        Args:
        nums (List[int]): A list of integers representing the input array.
        k (int): Length of the subarray.

        Returns:
        int: The maximum sum of a subarray of length k without duplicate elements.
        """
        n = len(nums)
        if k > n:
            return 0  # No subarray of length k is possible if k > n

        # Sliding window to maintain a window of exactly 'k' elements
        unique_elements = set()  # Set to track unique elements in the current window
        current_sum = 0  # Sum of elements in the current window
        max_sum = 0  # To keep track of the maximum sum found
        left = 0  # Left pointer of the sliding window

        for right in range(n):
            # Add current element to the window
            current_element = nums[right]

            # Shrink the window from the left until it contains no duplicates
            while current_element in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add the new element to the window
            unique_elements.add(current_element)
            current_sum += current_element

            # If the window size reaches k, update the maximum sum if needed
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                # Remove the leftmost element to maintain the window size for the next iteration
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum
