'''
Leetcode 2044 Count Number of Maximum Bitwise-OR Subsets

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example 1:
        Input: nums = [3,1]
        Output: 2
        Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
        - [3]
        - [3,1]

Example 2:
        Input: nums = [2,2,2]
        Output: 7
        Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:
        Input: nums = [3,2,1,5]
        Output: 6
        Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
        - [3,5]
        - [3,1,5]
        - [3,2,5]
        - [3,2,1,5]
        - [2,5]
        - [2,1,5]
 
Constraints:
        1 <= nums.length <= 16
        1 <= nums[i] <= 105

'''

from typing import List

class Solution:
    def backtrack(self, nums: List[int], index: int, currentOR: int, maxOR: int) -> int:
        # Base case: If the current OR equals maxOR, return 1
        if currentOR == maxOR:
            return 1
        
        count = 0
        
        # Recursive case: Explore all possible subsets
        for i in range(index, len(nums)):
            newOR = currentOR | nums[i]
            count += self.backtrack(nums, i + 1, newOR, maxOR)
        
        # Even if the current subset doesn't match maxOR, still count it as 0
        return count
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Compute the maximum OR across all numbers
        maxOR = 0
        for num in nums:
            maxOR |= num
        
        # Step 2: Initialize the backtracking process
        count = self.backtrackHelper(nums, 0, 0, maxOR)
        return count

    def backtrackHelper(self, nums: List[int], index: int, currentOR: int, maxOR: int) -> int:
        # If we reached the end of the list, check if the current OR matches the max OR
        if index == len(nums):
            return 1 if currentOR == maxOR else 0

        # Option 1: Include nums[index] in the current subset
        include_count = self.backtrackHelper(nums, index + 1, currentOR | nums[index], maxOR)
        
        # Option 2: Exclude nums[index] from the current subset
        exclude_count = self.backtrackHelper(nums, index + 1, currentOR, maxOR)

        return include_count + exclude_count


# second solution:

from typing import List
import unittest

class Solution:
    """
    Solution to count the number of subsets with the maximum possible bitwise OR value.
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        Returns the number of subsets whose bitwise OR is equal to the maximum possible OR 
        from any subset of the list.

        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        int: Count of subsets with the maximum OR.
        """
        max_or = 0
        for num in nums:
            max_or |= num  # Compute the global maximum OR value
        
        self.count = 0  # Initialize counter for valid subsets

        def backtrack(index: int, current_or: int) -> None:
            """
            Backtracking helper to explore all subsets and count those matching max_or.

            Parameters:
            index (int): Current index in nums list.
            current_or (int): OR value of the current subset.
            """
            if index == len(nums):
                if current_or == max_or:
                    self.count += 1  # Valid subset found
                return
            
            # Include current number in the subset
            backtrack(index + 1, current_or | nums[index])
            # Exclude current number from the subset
            backtrack(index + 1, current_or)

        backtrack(0, 0)  # Start backtracking from index 0 with OR 0
        return self.count


# --- Usage Example ---

if __name__ == "__main__":
    sol = Solution()
    example = [3, 1]
    print(f"Number of subsets with max OR from {example}: {sol.countMaxOrSubsets(example)}")


# --- Unit Tests ---

class TestCountMaxOrSubsets(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.countMaxOrSubsets([3, 1]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.countMaxOrSubsets([2, 2, 2]), 7)

    def test_example3(self):
        self.assertEqual(self.solution.countMaxOrSubsets([1, 2, 3]), 6)

    def test_all_zeroes(self):
        self.assertEqual(self.solution.countMaxOrSubsets([0, 0, 0]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.countMaxOrSubsets([7]), 1)



