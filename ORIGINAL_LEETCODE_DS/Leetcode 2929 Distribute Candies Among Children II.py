'''
Leetcode 2929 Distribute Candies Among Children II

You are given two positive integers n and limit.
Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

Example 1:
        Input: n = 5, limit = 2
        Output: 3
        Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
        
Example 2:
        Input: n = 3, limit = 3
        Output: 10
        Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
         
Constraints:
        1 <= n <= 106
        1 <= limit <= 106

'''
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Calculates the number of ways to distribute `n` candies among 3 children
        such that no child receives more than `limit` candies.

        Parameters:
        n (int): Total number of candies to distribute.
        limit (int): Maximum number of candies any child can receive.

        Returns:
        int: Number of valid distributions.
        """

        # Helper function to compute combinations C(x, 2)
        def combinations_2(x: int) -> int:
            return (x * (x - 1)) // 2 if x >= 2 else 0

        # Total number of integer solutions to a + b + c = n where a, b, c >= 0
        total = (n + 2) * (n + 1) // 2  # This is C(n + 2, 2)

        # Now subtract cases where one or more variables exceed the limit
        # Inclusion-Exclusion Principle

        # Number of invalid solutions where one variable > limit
        over_1 = combinations_2(n - limit + 1)

        # Number of invalid solutions where two variables > limit
        over_2 = combinations_2(n - 2 * limit)

        # Number of invalid solutions where all three variables > limit
        over_3 = combinations_2(n - 3 * limit - 1)

        # Apply inclusion-exclusion
        valid = total - 3 * over_1 + 3 * over_2 - over_3

        return valid

