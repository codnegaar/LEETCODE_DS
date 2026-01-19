'''
Leetcode 2338 Count the Number of Ideal Arrays

You are given two integers n and maxValue, which are used to describe an ideal array.
A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
        Input: n = 2, maxValue = 5
        Output: 10
        Explanation: The following are the possible ideal arrays:
        - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
        - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
        - Arrays starting with the value 3 (1 array): [3,3]
        - Arrays starting with the value 4 (1 array): [4,4]
        - Arrays starting with the value 5 (1 array): [5,5]
        There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

Example 2:        
        Input: n = 5, maxValue = 3
        Output: 11
        Explanation: The following are the possible ideal arrays:
        - Arrays starting with the value 1 (9 arrays): 
           - With no other distinct values (1 array): [1,1,1,1,1] 
           - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
           - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
        - Arrays starting with the value 2 (1 array): [2,2,2,2,2]
        - Arrays starting with the value 3 (1 array): [3,3,3,3,3]
        There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
         
Constraints:
        2 <= n <= 104
        1 <= maxValue <= 104
'''
import math

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        Efficient solution to count the number of ideal arrays of length `n` 
        where each element divides the next, and values are <= maxValue.
        Uses dynamic programming with divisor-based expansion.
        """
        MOD = 10**9 + 7
        max_len = 14  # Log2(10^4) is around 14, based on divisor tree depth

        # Precompute binomial coefficients C(n-1, k) using Pascal's triangle
        C = [[0] * (max_len + 1) for _ in range(n)]
        for i in range(n):
            C[i][0] = 1
            for j in range(1, min(i + 1, max_len + 1)):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        # dp[i] = number of ways to build an ideal array ending in i
        dp = [0] * (maxValue + 1)
        for i in range(1, maxValue + 1):
            dp[i] = 1  # Each number alone is an array of length 1

        total = 0
        for length in range(max_len + 1):  # max depth of multiplication chain
            for i in range(1, maxValue + 1):
                total = (total + dp[i] * C[n - 1][length]) % MOD

            # Expand dp[i] to next length using multiples
            new_dp = [0] * (maxValue + 1)
            for i in range(1, maxValue + 1):
                for j in range(2 * i, maxValue + 1, i):
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return total

# Test the optimized version
Solution().idealArrays(5, 10)


