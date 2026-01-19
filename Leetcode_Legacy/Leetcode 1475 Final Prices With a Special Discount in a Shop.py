'''
Leetcode 1475 Final Prices With a Special Discount in a Shop

You are given an integer array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such 
that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount. 

Example 1:
        Input: prices = [8,4,6,2,3]
        Output: [4,2,4,2,3]
        Explanation: 
        For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
        For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
        For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
        For items 3 and 4 you will not receive any discount at all.

Example 2:
        Input: prices = [1,2,3,4,5]
        Output: [1,2,3,4,5]
        Explanation: In this case, for all items, you will not receive any discount at all.

Example 3:
        Input: prices = [10,1,1,6]
        Output: [9,0,1,6]
 
Constraints:
        1 <= prices.length <= 500
        1 <= prices[i] <= 1000

'''
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Computes the final prices with a discount applied for each item.
        The discount is the price of the first item to the right that is less than or equal to the current item.
        If no such item exists, no discount is applied.

        Parameters:
            prices (List[int]): List of integers representing prices of items.

        Returns:
            List[int]: List of final prices after applying the discount.
        """
        n = len(prices)
        result = prices[:]  # Copy of the original prices
        stack = []  # Monotonic stack to keep track of indices of prices

        # Traverse prices from left to right
        for i in range(n):
            # Check for discounts with prices in the stack
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                result[j] -= prices[i]  # Apply discount for price at index j
            
            # Add current price index to the stack
            stack.append(i)
        
        return result


# Unit Tests
def test_finalPrices():
    solution = Solution()

    # Test Case 1: General case
    assert solution.finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3], "Test Case 1 Failed"

    # Test Case 2: All decreasing prices
    assert solution.finalPrices([10, 9, 8, 7]) == [1, 1, 1, 7], "Test Case 2 Failed"

    # Test Case 3: All increasing prices
    assert solution.finalPrices([1, 2, 3, 4]) == [1, 2, 3, 4], "Test Case 3 Failed"

    # Test Case 4: Single price
    assert solution.finalPrices([5]) == [5], "Test Case 4 Failed"

    # Test Case 5: Mixed prices
    assert solution.finalPrices([3, 1, 2, 3, 1]) == [2, 1, 1, 3, 1], "Test Case 5 Failed"

    print("All test cases passed!")


# Run Tests
if __name__ == "__main__":
    test_finalPrices()
