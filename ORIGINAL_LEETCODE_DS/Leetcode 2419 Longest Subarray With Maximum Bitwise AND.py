'''
Leetcode 2419 Longest Subarray With Maximum Bitwise AND

You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.

Example 1:
        Input: nums = [1,2,3,3,2,2]
        Output: 2
        Explanation:
                The maximum possible bitwise AND of a subarray is 3.
                The longest subarray with that value is [3,3], so we return 2.

Example 2:
          Input: nums = [1,2,3,4]
          Output: 1
          Explanation:
                The maximum possible bitwise AND of a subarray is 4.
                The longest subarray with that value is [4], so we return 1.

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 106

'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  # Handle empty input case
            return 0
        
        xMax = max(nums)  # Find the maximum value in the array
        maxLen = 0
        currentLen = 0
        
        for i in range(n):
            if nums[i] == xMax:
                currentLen += 1  # Increment length of current contiguous max subarray
            else:
                maxLen = max(maxLen, currentLen)  # Update max length found so far
                currentLen = 0  # Reset current length
        
        maxLen = max(maxLen, currentLen)  # Handle the case where the subarray ends at the last element
        
        return maxLen
