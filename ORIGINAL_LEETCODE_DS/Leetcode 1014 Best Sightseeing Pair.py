'''
Leetcode 1014 Best Sightseeing Pair
 
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots. 

Example 1:
        Input: values = [8,1,5,2,6]
        Output: 11
        Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:
        Input: values = [1,2]
        Output: 2
 
Constraints:
        2 <= values.length <= 5 * 104
        1 <= values[i] <= 1000

'''
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Find the maximum score of a sightseeing pair from the given values.

        Parameters:
        - values (List[int]): List of integers where each element represents the value of a sightseeing spot.

        Returns:
        - int: The maximum score of a sightseeing pair.
        """
        n = len(values)  # Length of the input array
        dp = 0  # Represents the best value for values[i] + i seen so far
        score = 0  # Maximum score for a sightseeing pair

        # Iterate through the array to calculate the maximum score
        for i, x in enumerate(values):
            # Update the score considering the current spot (x) and previous max (dp)
            score = max(score, dp + x - i)

            # Update dp to hold the maximum values[i] + i seen so far
            dp = max(dp, x + i)

        return score

# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Example Test Case 1
    values = [8, 1, 5, 2, 6]
    print("Test Case 1:", solution.maxScoreSightseeingPair(values))  # Expected Output: 11

    # Example Test Case 2
    values = [1, 2]
    print("Test Case 2:", solution.maxScoreSightseeingPair(values))  # Expected Output: 2
