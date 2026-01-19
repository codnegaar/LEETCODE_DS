'''

Leetcode 188 Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000

'''

class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    if k >= len(prices) // 2:
      sell = 0
      hold = -math.inf

      for price in prices:
        sell = max(sell, hold + price)
        hold = max(hold, sell - price)

      return sell

    sell = [0] * (k + 1)
    hold = [-math.inf] * (k + 1)

    for price in prices:
      for i in range(k, 0, -1):
        sell[i] = max(sell[i], hold[i] + price)
        hold[i] = max(hold[i], sell[i - 1] - price)

    return sell[k]


# Second Solution

from typing import List
import math

class Solution:
    """
    A class to solve the 'Best Time to Buy and Sell Stock IV' problem.

    Given an integer k and a list of stock prices, the function finds the maximum
    profit that can be achieved with at most k transactions.
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Compute the maximum profit achievable with at most k transactions.

        Parameters:
            k (int): Maximum number of transactions allowed.
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum profit achievable.

        Time Complexity:
            - O(n) if k is large (i.e., acts like unlimited transactions).
            - O(k * n) in general cases due to nested loops.
        """

        n = len(prices)
        if n == 0:
            return 0  # Edge case: No prices available

        # If k is large enough, treat it as unlimited transactions
        if k >= n // 2:
            sell = 0  # Maximum profit when not holding a stock
            hold = -math.inf  # Maximum profit when holding a stock

            for price in prices:
                sell = max(sell, hold + price)  # Either sell today or continue
                hold = max(hold, sell - price)  # Either buy today or continue holding

            return sell

        # DP arrays: Sell[i] = max profit after i transactions without holding stock
        sell = [0] * (k + 1)  # Profit after selling at most i times
        hold = [-math.inf] * (k + 1)  # Profit after buying at most i times

        # Dynamic programming approach
        for price in prices:
            for i in range(k, 0, -1):  # Iterate from k down to 1 to maintain correct update order
                sell[i] = max(sell[i], hold[i] + price)  # Either sell today or keep the previous profit
                hold[i] = max(hold[i], sell[i - 1] - price)  # Either buy today or keep holding

        return sell[k]


# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print("Maximum Profit:", solution.maxProfit(k, prices))  # Expected Output: 7


# Unit Tests
import unittest

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        self.assertEqual(self.solution.maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)
        self.assertEqual(self.solution.maxProfit(2, [2, 4, 1]), 2)
        self.assertEqual(self.solution.maxProfit(0, [3, 2, 6, 5, 0, 3]), 0)  # No transactions allowed
        self.assertEqual(self.solution.maxProfit(100, [1, 2, 3, 4, 5]), 4)  # Large k (unlimited transactions)
        self.assertEqual(self.solution.maxProfit(2, [7, 6, 4, 3, 1]), 0)  # No profit possible
        self.assertEqual(self.solution.maxProfit(2, []), 0)  # Empty price list

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

