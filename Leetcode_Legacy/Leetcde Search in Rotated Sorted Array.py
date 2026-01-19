'''
Leetcode Search in Rotated Sorted Array
 
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity. 

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1 

Constraints:
    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# Second solution
from typing import List
import unittest

class Solution:
    """
    This class provides a method to search for a given target in a rotated sorted array.
    It uses a modified binary search approach.
    """
    
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for a target value in a rotated sorted array and return its index 
        if found, otherwise return -1.

        The input array is assumed to have been rotated an unknown number of times, 
        but was originally sorted in ascending order.

        :param nums: A list of integers, representing the rotated sorted array.
        :type nums: List[int]
        :param target: The integer value to search for in nums.
        :type target: int
        :return: The index of the target if found, else -1.
        :rtype: int
        """
        # Initialize two pointers for the search range.
        left, right = 0, len(nums) - 1

        # Use binary search to find the target.
        while left <= right:
            mid = (left + right) // 2  # Calculate the midpoint.
            
            # If the target is found, return its index immediately.
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted in ascending order.
            if nums[left] <= nums[mid]:
                # If the target is within the left half, move the right pointer.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, search in the right half.
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted.
            else:
                # If the target is within the right half, move the left pointer.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, search in the left half.
                else:
                    right = mid - 1

        # If we exit the loop without returning, the target is not in the list.
        return -1


class TestSolution(unittest.TestCase):
    """
    This class provides unit tests for the Solution class.
    """

    def setUp(self):
        """
        Create a Solution object for testing.
        """
        self.solution = Solution()

    def test_example_1(self):
        """
        Test searching for a target present in the array.
        """
        nums = [4,5,6,7,0,1,2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example_2(self):
        """
        Test searching for a target not present in the array.
        """
        nums = [4,5,6,7,0,1,2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_3(self):
        """
        Test searching in a single-element array.
        """
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_4(self):
        """
        Test when target is the first element in rotated array.
        """
        nums = [3,1]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_example_5(self):
        """
        Test when target is the last element in rotated array.
        """
        nums = [3,1,2]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 2)


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

        
