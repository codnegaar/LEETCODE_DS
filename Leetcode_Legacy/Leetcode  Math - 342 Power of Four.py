'''
Leetcode  Math - 342 Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
        Input: n = 16
        Output: true

Example 2:
        Input: n = 5
        Output: false

Example 3:
        Input: n = 1
        Output: true 

Constraints:
        -231 <= n <= 231 - 1

'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Check if a number is a power of four.

        A number is a power of four if:
        1. It is greater than 0.
        2. It has exactly one '1' bit in binary (i.e., is a power of two).
        3. That '1' bit is in an odd position (0-indexed from the right).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

