'''
Leetcode 201 Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
        Input: left = 5, right = 7
        Output: 4

Example 2:
        Input: left = 0, right = 0
        Output: 0

Example 3:
        Input: left = 1, right = 2147483647
        Output: 0
 
Constraints:
        0 <= left <= right <= 231 - 1

'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Calculates the bitwise AND of all numbers in the range [m, n].

        Parameters:
        m (int): Start of the range.
        n (int): End of the range.

        Returns:
        int: The bitwise AND of all numbers in the range.
        """
        # Recursive case: Shift both numbers right and solve the smaller problem
        if m < n:
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
        # Base case: When m equals n, return m
        return m
