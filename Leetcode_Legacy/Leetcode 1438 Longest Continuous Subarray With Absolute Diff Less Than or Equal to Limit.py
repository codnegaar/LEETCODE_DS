'''

Leetcode 1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
        Input: nums = [8,2,4,7], limit = 4
        Output: 2 
        Explanation: All subarrays are: 
        [8] with maximum absolute diff |8-8| = 0 <= 4.
        [8,2] with maximum absolute diff |8-2| = 6 > 4. 
        [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
        [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
        [2] with maximum absolute diff |2-2| = 0 <= 4.
        [2,4] with maximum absolute diff |2-4| = 2 <= 4.
        [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
        [4] with maximum absolute diff |4-4| = 0 <= 4.
        [4,7] with maximum absolute diff |4-7| = 3 <= 4.
        [7] with maximum absolute diff |7-7| = 0 <= 4. 
        Therefore, the size of the longest subarray is 2.

Example 2:        
        Input: nums = [10,1,2,4,7,2], limit = 5
        Output: 4 
        Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
        Input: nums = [4,2,2,2,4,4,2,2], limit = 0
        Output: 3
 

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109
        0 <= limit <= 109

'''

from typing import List
import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deques to keep track of the maximum and minimum values in the current window
        maxDeque = collections.deque()
        minDeque = collections.deque()
        left = 0
        maxLength = 0

        for right, num in enumerate(nums):
            # Maintain the decreasing deque for the maximum values
            while maxDeque and num > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(num)

            # Maintain the increasing deque for the minimum values
            while minDeque and num < minDeque[-1]:
                minDeque.pop()
            minDeque.append(num)

            # If the difference between the maximum and minimum values exceeds the limit
            while maxDeque[0] - minDeque[0] > limit:
                # Move the left pointer to shrink the window
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1

            # Update the maximum length of the subarray
            maxLength = max(maxLength, right - left + 1)

        return maxLength
