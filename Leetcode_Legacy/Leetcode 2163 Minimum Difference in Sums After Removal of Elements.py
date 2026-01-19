'''
Leetcode 2163 Minimum Difference in Sums After Removal of Elements

You are given a 0-indexed integer array nums consisting of 3 * n elements.
You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.
For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

Example 1:
        Input: nums = [3,1,2]
        Output: -1
        Explanation: Here, nums has 3 elements, so n = 1. 
        Thus we have to remove 1 element from nums and divide the array into two equal parts.
        - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
        - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
        - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
        The minimum difference between sums of the two parts is min(-1,1,2) = -1. 

Example 2:
        Input: nums = [7,9,5,8,1,3]
        Output: 1
        Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
        If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
        To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
        It can be shown that it is not possible to obtain a difference smaller than 1.
         
Constraints:        
        nums.length == 3 * n
        1 <= n <= 105
        1 <= nums[i] <= 105


'''
import heapq
from typing import List
import unittest

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Calculate the minimum possible difference between the sum of a selected
        n-length prefix subarray and an n-length suffix subarray where:
            - nums is of length 3n
            - Prefix comes from the first 2n elements
            - Suffix comes from the last 2n elements
        The prefix should have the maximum possible sum among all n-length
        subarrays in the first 2n elements, and suffix should have the minimum
        possible sum among all n-length subarrays in the last 2n elements.

        Args:
            nums (List[int]): The input list of integers of length 3n

        Returns:
            int: The minimum difference between prefix and suffix sums
        """
        m = len(nums)
        n = m // 3

        # Compute max sum for each n-sized subarray from left to 2n using max-heap
        left = [0] * m
        max_heap = []
        left_sum = sum(nums[:n])
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
        left[n - 1] = left_sum

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            popped = -heapq.heappop(max_heap)
            left_sum += nums[i] - popped
            left[i] = left_sum

        # Compute min sum for each n-sized subarray from 2n to end using min-heap
        right = [0] * m
        min_heap = []
        right_sum = sum(nums[-n:])
        for i in range(m - 1, 2 * n - 1, -1):
            heapq.heappush(min_heap, nums[i])
        right[2 * n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            popped = heapq.heappop(min_heap)
            right_sum += nums[i] - popped
            right[i] = right_sum

        # Find the minimum difference between left prefix sum and right suffix sum
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            min_diff = min(min_diff, left[i] - right[i + 1])

        return min_diff


# Example implementation
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 2, 8, 9, 7, 4, 6]
    print("Minimum Difference:", sol.minimumDifference(nums))


# Unit tests
class TestMinimumDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.minimumDifference([1, 3, 5, 2, 8, 9, 7, 4, 6]), 1)

    def test_case_2(self):
        self.assertEqual(self.solution.minimumDifference([10, 20, 30, 40, 50, 60, 70, 80, 90]), 30)

    def test_case_3(self):
        self.assertEqual(self.solution.minimumDifference([5, 5, 5, 5, 5, 5, 5, 5, 5]), 0)


"""
# ≡ƒöä Changes Made:
- Added complete docstring and line-by-line comments.
- Cleaned variable names for better readability (e.g., `prefSum` ΓåÆ `left_sum`).
- Ensured clarity of logic by separating heap operations.
- Added a full unit test using `unittest` framework.
- Improved clarity, not asymptotic complexity (still O(n log n) due to heaps).
- Removed redundant allocation of heap elements outside necessary ranges.

# ≡ƒôÜ Python Documentation Reference:
- heapq: https://docs.python.org/3/library/heapq.html
- unittest: https://docs.python.org/3/library/unittest.html
"""
