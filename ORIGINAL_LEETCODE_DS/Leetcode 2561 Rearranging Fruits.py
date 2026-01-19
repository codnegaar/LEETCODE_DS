'''

Leetcode 2561 Rearranging Fruits

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. 
To do so, you can use the following operation as many times as you want:
        Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
        The cost of the swap is min(basket1[i],basket2[j]).
        Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.
        
        Return the minimum cost to make both the baskets equal or -1 if impossible. 

Example 1:
        Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
        Output: 1
        Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

Example 2:
        Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
        Output: -1
        Explanation: It can be shown that it is impossible to make both the baskets equal.
         
Constraints:
        basket1.length == basket2.length
        1 <= basket1.length <= 105
        1 <= basket1[i],basket2[i] <= 109

'''

from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Calculate the minimum cost to make two baskets identical by exchanging fruits.
        Each fruit type has an associated cost equal to its value.
        
        Parameters:
        basket1 (List[int]): First basket of fruits (represented by integers).
        basket2 (List[int]): Second basket of fruits.
        
        Returns:
        int: Minimum cost of exchange to make baskets equal or -1 if not possible.
        
        Reference: https://docs.python.org/3/library/collections.html#collections.defaultdict
        """
        # Step 1: Count net differences in fruit frequency
        fruits_count = defaultdict(int)
        for fruit in basket1: fruits_count[fruit] += 1
        for fruit in basket2: fruits_count[fruit] -= 1

        # Early exit if any fruit count is odd (can't balance)
        if any(v % 2 for v in fruits_count.values()):
            return -1

        # Step 2: Build list of fruits to be exchanged
        to_exchange = [fruit for fruit, count in fruits_count.items() for _ in range(abs(count) // 2)]
        
        # Step 3: Find the cheapest fruit across both baskets
        min_fruit = min(map(min, [basket1, basket2]))
        
        # Step 4: Sort and pair elements for minimum cost swap
        to_exchange.sort()
        half = len(to_exchange) // 2
        # Use min(fruit, 2 * min_fruit) for optimal swap (direct or double swap)
        return sum(min(f, 2 * min_fruit) for f in to_exchange[:half])
