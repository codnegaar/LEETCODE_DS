
'''

Leetcode 3105 Longest Strictly Increasing or Strictly Decreasing Subarray
 
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50

'''


from typing import List
import unittest

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest contiguous monotonic (increasing or decreasing) subarray.

        :param nums: List of integers.
        :return: The length of the longest increasing or decreasing contiguous subarray.

        Approach:
        - Use two counters: `inc_len` (for increasing subarrays) and `dec_len` (for decreasing).
        - Iterate through `nums`, updating these counters based on comparisons with previous elements.
        - Keep track of `max_len` to store the longest monotonic subarray length.

        Example:
        >>> Solution().longestMonotonicSubarray([1, 2, 3, 2, 1, 4, 5])
        3
        >>> Solution().longestMonotonicSubarray([9, 8, 7, 6, 5])
        5
        >>> Solution().longestMonotonicSubarray([1, 1, 1, 1])
        1
        """

        if not nums:
            return 0  # Edge case: empty list
        
        inc_len = 1  # Length of increasing subarray
        dec_len = 1  # Length of decreasing subarray
        max_len = 1  # Stores the longest monotonic subarray length

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc_len += 1
                dec_len = 1  # Reset decreasing length
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec_len += 1
                inc_len = 1  # Reset increasing length
            else:  # Neither increasing nor decreasing (equal elements)
                inc_len = 1
                dec_len = 1

            max_len = max(max_len, inc_len, dec_len)  # Update max length

        return max_len


# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 2, 1, 4, 5], 3),
        ([9, 8, 7, 6, 5], 5),
        ([1, 1, 1, 1], 1),
        ([10, 20, 30, 40, 50], 5),
        ([100, 90, 80, 70, 60, 50, 40], 7),
        ([], 0),  # Edge case: empty list
        ([5], 1),  # Edge case: single element
    ]

    for nums, expected in test_cases:
        result = solution.longestMonotonicSubarray(nums)
        print(f"longestMonotonicSubarray({nums}) = {result} | Expected: {expected}")
