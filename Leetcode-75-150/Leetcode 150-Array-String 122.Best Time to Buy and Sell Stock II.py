'''
Leetcode 150-Array-String 122.Best Time to Buy and Sell Stock II

You are given an integer array of prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and then immediately sell it on the same day.
Find and return the maximum profit you can achieve.


Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                     Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
                     Total profit is 4 + 3 = 7.

Example 2:
        Input: prices = [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                     Total profit is 4.

Example 3:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
        
Constraints:
        1 <= prices.length <= 3 * 104
        0 <= prices[i] <= 104

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold



# Second and easy solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                profit+=(prices[i]-prices[i-1])
        return profit
