'''
Leetcode 2762 Continuous Subarrays
 
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.
A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:
        Input: nums = [5,4,2,4]
        Output: 8
        Explanation: 
        Continuous subarray of size 1: [5], [4], [2], [4].
        Continuous subarray of size 2: [5,4], [4,2], [2,4].
        Continuous subarray of size 3: [4,2,4].
        There are no subarrays of size 4.
        Total continuous subarrays = 4 + 3 + 1 = 8.
        It can be shown that there are no more continuous subarrays.
 

Example 2:
        Input: nums = [1, 2, 3]
        Output: 6
        Explanation:
        Continuous subarray of size 1: [1], [2], [3].
        Continuous subarray of size 2: [1, 2], [2, 3].
        Continuous subarray of size 3: [1, 2, 3].
        Total continuous subarrays = 3 + 2 + 1 = 6.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

'''

from collections import deque
from typing import List
import unittest

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        Count the number of continuous subarrays where the difference between 
        the maximum and minimum elements is at most 2.

        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        int: The total number of valid continuous subarrays.
        """
        # Initialize pointers and result counter
        left = 0  # Left pointer for the sliding window
        result = 0  # Total count of valid subarrays
        
        # Deques to keep track of the indices of min and max elements in the window
        minDeque, maxDeque = deque(), deque()

        for right in range(len(nums)):
            # Maintain minDeque in increasing order
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            # Maintain maxDeque in decreasing order
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            
            # Add the current index to both deques
            minDeque.append(right)
            maxDeque.append(right)

            # Shrink the window if the difference between max and min exceeds 2
            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                left += 1
                # Remove indices that are out of the window
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()

            # Add the count of valid subarrays ending at 'right'
            result += right - left + 1

        return result

# Unit Test Class
class TestContinuousSubarrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.continuousSubarrays(nums), 6)  # All subarrays valid

    def test_case_2(self):
        nums = [4, 5, 6, 7]
        self.assertEqual(self.solution.continuousSubarrays(nums), 4)  # Only individual elements valid

    def test_case_3(self):
        nums = [1, 2, 2, 3]
        self.assertEqual(self.solution.continuousSubarrays(nums), 9)  # Mix of valid subarrays

    def test_case_4(self):
        nums = [2, 2, 2, 2]
        self.assertEqual(self.solution.continuousSubarrays(nums), 10)  # All subarrays valid

    def test_case_5(self):
        nums = [1, 4, 7]
        self.assertEqual(self.solution.continuousSubarrays(nums), 3)  # Only single-element subarrays valid

    def test_case_6(self):
        nums = [10]
        self.assertEqual(self.solution.continuousSubarrays(nums), 1)  # Single-element array

# Main execution block
if __name__ == "__main__":
    # Use unittest to run the tests
    unittest.main()
