'''
Leetcode 300 Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        
Example 2:
        Input: nums = [0,1,0,3,2,3]
        Output: 4
        
Example 3:
        Input: nums = [7,7,7,7,7,7,7]
        Output: 1 

Constraints:
        1 <= nums.length <= 2500
        -104 <= nums[i] <= 104
 
 '''
class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
      return 0

    # dp[i] := LIS ending at nums[i]
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
      for j in range(i):
        if nums[j] < nums[i]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Second solution
from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest increasing subsequence in a given list.

        :param nums: List of integers.
        :return: Length of the longest increasing subsequence.

        Example:
        >>> Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        4
        """
        if not nums:
            return 0  # Edge case: Empty list

        subsequence = []  # Stores the longest increasing subsequence
        
        for num in nums:
            # Use binary search to find the position to replace or extend
            idx = bisect_left(subsequence, num)
            
            if idx == len(subsequence):
                # If num is greater than all elements, extend the list
                subsequence.append(num)
            else:
                # Replace an element to maintain a lower LIS value
                subsequence[idx] = num

        return len(subsequence)  # The length of the subsequence is the answer
