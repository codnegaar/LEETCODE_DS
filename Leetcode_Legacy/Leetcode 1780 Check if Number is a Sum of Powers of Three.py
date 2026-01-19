'''
Leetcode 1780 Check if Number is a Sum of Powers of Three

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
        Input: n = 12
        Output: true
        Explanation: 12 = 31 + 32

Example 2:
        Input: n = 91
        Output: true
        Explanation: 91 = 30 + 32 + 34

Example 3:
        Input: n = 21
        Output: false
 
Constraints:
        1 <= n <= 107

'''

import unittest

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Checks if a given integer `n` can be represented as a sum of distinct powers of three.

        Parameters:
        n (int): The number to be checked.

        Returns:
        bool: True if `n` can be represented as a sum of distinct powers of three, False otherwise.
        """
        # Iteratively check if n contains any digit '2' in base-3 representation
        while n:
            if n % 3 == 2:  # If remainder is 2, it's impossible to form using distinct 3^x
                return False
            n //= 3  # Reduce n by dividing it by 3

        return True  # If loop completes, it means n can be represented
