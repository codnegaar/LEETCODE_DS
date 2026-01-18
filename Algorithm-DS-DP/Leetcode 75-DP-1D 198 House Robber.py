'''
Leetcode 75-DP-1D 198 House Robber

 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer
array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police. 

Example 1:
        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
Example 2:
        Input: nums = [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.
Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 400

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        indx1, indx2 = 0,0

        # [indx1, indx2, n, n+1, ...]
        for n in nums:
            temp=max(n + indx1, indx2)
            indx1=indx2
            indx2=temp
        return indx2

# Second Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]

# second solution
from typing import List

class Solution:
    """
    A solution for the House Robber problem using dynamic programming.
    This class provides an optimized approach to calculate the maximum amount 
    of money that can be robbed without robbing two adjacent houses.

    Methods:
    --------
    rob(nums: List[int]) -> int:
        Calculates the maximum amount of money that can be robbed.
    """
    
    def rob(self, nums: List[int]) -> int:
        """
        Computes the maximum amount of money that can be robbed from a list of houses.
        
        Parameters:
        -----------
        nums : List[int]
            A list of integers where nums[i] represents the amount of money in the i-th house.

        Returns:
        --------
        int
            The maximum amount of money that can be robbed without robbing two adjacent houses.

        Time Complexity:
        ----------------
        O(n): The algorithm iterates through the list once.

        Space Complexity:
        -----------------
        O(1): Only two variables are used to store the state.
        """
        # Handle edge cases for empty or small input lists
        if not nums:
            return 0  # No houses to rob
        if len(nums) == 1:
            return nums[0]  # Only one house, rob it
        
        # Initialize two variables to keep track of maximum robbed amounts
        prev1, prev2 = 0, 0  # prev1 = max money robbed up to i-1, prev2 = up to i-2

        # Iterate over each house's money in nums
        for num in nums:
            # Compute the new maximum amount by either skipping or robbing the current house
            new_rob = max(prev1, prev2 + num)
            prev2 = prev1  # Update prev2 to the previous value of prev1
            prev1 = new_rob  # Update prev1 to the newly calculated max value

        # Return the maximum amount that can be robbed
        return prev1


# Example Implementation
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input: List of house values
    houses = [2, 7, 9, 3, 1]
    
    # Call the rob method and print the result
    print("Maximum money that can be robbed:", solution.rob(houses))


# Unit Tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.rob([]), 0, "Should return 0 for an empty list")

    def test_single_house(self):
        self.assertEqual(self.solution.rob([5]), 5, "Should return the house value for a single house")

    def test_two_houses(self):
        self.assertEqual(self.solution.rob([2, 3]), 3, "Should return the max value of the two houses")

    def test_multiple_houses(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12, "Should return the correct max value")
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4, "Should return the correct max value")
        self.assertEqual(self.solution.rob([10, 2, 2, 100]), 110, "Should return the correct max value")

    def test_all_houses_same_value(self):
        self.assertEqual(self.solution.rob([10, 10, 10, 10]), 20, "Should correctly handle all houses having the same value")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)


"""
### Changes Made:
1. **Efficiency Improvement**: Optimized space complexity from `O(n)` to `O(1)` by using two variables (`prev1` and `prev2`).
2. **Added Documentation**: Included docstrings for the class and method to provide clear explanations.
3. **Code Formatting**: Applied proper indentation, spacing, and comments for better readability.
4. **Example Implementation**: Added a practical implementation example in the `if __name__ == "__main__"` block.
5. **Unit Testing**: Implemented `unittest` to ensure correctness across multiple test cases.

### Reference:
For more on the `max` function and dynamic programming, see:
https://docs.python.org/3/library/functions.html#max
"""

