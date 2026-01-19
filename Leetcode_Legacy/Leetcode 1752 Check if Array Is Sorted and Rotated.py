'''

Leetcode 1752 Check if the Array Is Sorted and Rotated
 
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
        Input: nums = [3,4,5,1,2]
        Output: true
        Explanation: [1,2,3,4,5] is the original sorted array.
        You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].

Example 2:
        Input: nums = [2,1,3,4]
        Output: false
        Explanation: There is no sorted array once rotated that can make nums.

Example 3:
        Input: nums = [1,2,3]
        Output: true
        Explanation: [1,2,3] is the original sorted array.
        You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
         

Constraints:        
        1 <= nums.length <= 100
        1 <= nums[i] <= 100

'''

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Determines if an array can be rotated to become non-decreasing.

        :param nums: List of integers.
        :return: True if the array can be rotated to be sorted, False otherwise.

        Conditions:
        - Count how many times `nums[i] > nums[i+1]` occurs (descents).
        - If there's **0 descent**, it's already sorted.
        - If there's **1 descent**, check if the last element is Γëñ first (valid rotation).
        - More than 1 descent ΓåÆ Not possible.

        Example:
        >>> Solution().check([3, 4, 5, 1, 2])
        True
        >>> Solution().check([2, 1, 3, 4])
        False
        >>> Solution().check([1, 2, 3, 4, 5])
        True
        """

        # Count descents (where nums[i] > nums[i+1])
        descent_count = sum(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

        # Check if the array is already sorted or can be rotated
        return descent_count == 0 or (descent_count == 1 and nums[-1] <= nums[0])


# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3, 4, 5], True),
        ([6, 10, 6], True),
        ([1, 2, 3, 4, 0, 1], False)
    ]

    for nums, expected in test_cases:
        result = solution.check(nums)
        print(f"check({nums}) = {result} | Expected: {expected}")


# Unit Tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        self.assertTrue(self.solution.check([3, 4, 5, 1, 2]))
        self.assertFalse(self.solution.check([2, 1, 3, 4]))
        self.assertTrue(self.solution.check([1, 2, 3, 4, 5]))
        self.assertTrue(self.solution.check([6, 10, 6]))  # Edge case with a valid rotation
        self.assertFalse(self.solution.check([1, 2, 3, 4, 0, 1]))  # Multiple descents

if __name__ == "__main__":
    unittest.main()

