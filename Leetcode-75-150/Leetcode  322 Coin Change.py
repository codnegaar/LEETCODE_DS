'''

Leetcode  322 Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

Example 2:
        Input: coins = [2], amount = 3
        Output: -1

Example 3:        
        Input: coins = [1], amount = 0
        Output: 0
         
Constraints:      
        1 <= coins.length <= 12
        1 <= coins[i] <= 231 - 1
        0 <= amount <= 104

'''
from typing import List
import unittest

class Solution:
    """Solves the Coin Change problem using Dynamic Programming."""

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Computes the minimum number of coins required to make up a given amount.
        
        :param coins: List of available coin denominations.
        :param amount: The total amount to form using the given coins.
        :return: Minimum number of coins needed to make the amount, or -1 if it's impossible.
        """
        # Initialize DP table: dp[i] stores the fewest number of coins to form amount i
        dp = [0] + [float("inf")] * amount  # Use infinity to represent unreachable states

        # Process each coin denomination
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] remains infinity, it means we can't form the amount
        return dp[amount] if dp[amount] != float("inf") else -1






