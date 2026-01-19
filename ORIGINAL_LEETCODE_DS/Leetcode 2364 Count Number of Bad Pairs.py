'''
Leetcode 2364 Count Number of Bad Pairs
 
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
Return the total number of bad pairs in nums. 

Example 1:
        Input: nums = [4,1,3,3]
        Output: 5
        Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
        The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
        The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
        The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
        The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
        There are a total of 5 bad pairs, so we return 5.

Example 2:
        Input: nums = [1,2,3,4,5]
        Output: 0
        Explanation: There are no bad pairs.
 
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109

'''
import unittest
from collections import defaultdict
from typing import List

class Solution:
    """
    A class containing a method to count the number of 'bad pairs' in an array.
    """

    def countBadPairs(self, nums: List[int]) -> int:
        """
        Count the number of 'bad pairs' in an array.

        A pair (i, j) is considered 'bad' if:
            j - i Γëá nums[j] - nums[i]

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: The number of bad pairs.

        Time Complexity:
            Optimized to O(n) using a hashmap to track frequency differences.
        """
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2  # Compute total number of pairs
        
        good_pairs = 0
        freq = defaultdict(int)  # Using defaultdict to simplify key existence check

        for i, num in enumerate(nums):
            diff = num - i  # Compute difference nums[i] - i
            good_pairs += freq[diff]  # Count previously seen occurrences
            freq[diff] += 1  # Update frequency map
        
        return total_pairs - good_pairs  # Compute bad pairs

# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 3, 3]
    print("Number of bad pairs:", solution.countBadPairs(nums))  # Expected Output: 5

    # Run unit tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
