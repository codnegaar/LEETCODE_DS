'''
Leetcode 1695 Maximum Erasure Value
 
You are given an array of positive integers nums, and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
Return the maximum score you can get by erasing exactly one subarray.
An array b is called a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r). 

Example 1:
        Input: nums = [4,2,4,5,6]
        Output: 17
        Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
        Input: nums = [5,2,1,2,5,2,1,2,5]
        Output: 8
        Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
         
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 104
'''
from typing import List

class Solution:
    """
    Provides a method to find the maximum sum of a subarray with all unique elements.
    """

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Calculates the maximum sum of a subarray that contains only unique elements.

        Parameters:
        nums (List[int]): List of integers representing the input array.

        Returns:
        int: The maximum possible sum of a subarray with all unique elements.
        """
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            current_sum += nums[right]
            seen.add(nums[right])
            max_sum = max(max_sum, current_sum)

        return max_sum

            # Update max sum
            max_sum = max(max_sum, current_sum)

        return max_sum
