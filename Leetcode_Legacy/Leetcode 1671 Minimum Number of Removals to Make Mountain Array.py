'''

Leetcode 1671 Minimum Number of Removals to Make Mountain Array

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array numsΓÇïΓÇïΓÇï, return the minimum number of elements to remove to make numsΓÇïΓÇïΓÇï a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.


'''
from typing import List
from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Calculate the minimum number of removals needed to form a mountain array.
        A mountain array is defined as an array where elements increase up to a peak and then decrease.

        Parameters:
        nums (List[int]): The list of integers from which the mountain array will be formed.

        Returns:
        int: Minimum number of elements to remove to form a valid mountain array.
        """
        n = len(nums)
        
        # Calculate the length of Longest Increasing Subsequence (LIS) ending at each index
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # Calculate the length of Longest Decreasing Subsequence (LDS) starting at each index
        LDS = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)

        # Find the maximum mountain length
        maxMountainLength = 0
        for i in range(1, n - 1):
            # A valid mountain peak must have LIS > 1 and LDS > 1 (i.e., elements on both sides)
            if LIS[i] > 1 and LDS[i] > 1:
                maxMountainLength = max(maxMountainLength, LIS[i] + LDS[i] - 1)

        # Return the minimum number of removals to make a mountain array
        return n - maxMountainLength

# Example usage:
# sol = Solution()
# print(sol.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
