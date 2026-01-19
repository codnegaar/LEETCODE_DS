'''

Leetcode 2554 Maximum Number of Integers to Choose From a Range I

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

        The chosen integers have to be in the range [1, n].
        Each integer can be chosen at most once.
        The chosen integers should not be in the array banned.
        The sum of the chosen integers should not exceed maxSum.
        Return the maximum number of integers you can choose following the mentioned rules.

 

Example 1:
        Input: banned = [1,6,5], n = 5, maxSum = 6
        Output: 2
        Explanation: You can choose the integers 2 and 4.
        2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

Example 2:
        Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
        Output: 0
        Explanation: You cannot choose any integer while following the mentioned conditions.

Example 3:
        Input: banned = [11], n = 7, maxSum = 50
        Output: 7
        Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
        They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.
         

Constraints:
        1 <= banned.length <= 104
        1 <= banned[i], n <= 104
        1 <= maxSum <= 109


'''
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        Finds the maximum count of numbers from 1 to n that can be selected 
        without exceeding maxSum and while excluding numbers from the banned list.

        Args:
        - banned (List[int]): List of integers that are not allowed to be chosen.
        - n (int): The upper limit of numbers to consider (inclusive).
        - maxSum (int): The maximum sum allowed for the chosen numbers.

        Returns:
        - int: The maximum count of numbers that can be selected.
        """

        # Convert banned list to a set for O(1) lookups
        banned_set = set(banned)

        # Initialize sum of selected numbers and count of selected numbers
        current_sum, count = 0, 0

        # Iterate through all numbers from 1 to n, selecting numbers not in the banned set
        for num in range(1, n + 1):
            if num in banned_set:
                continue  # Skip the number if it is banned

            if current_sum + num > maxSum:
                break  # Stop if adding the current number would exceed maxSum

            current_sum += num  # Add the current number to the sum
            count += 1  # Increment the count of selected numbers

        return count  # Return the total count of selected numbers



