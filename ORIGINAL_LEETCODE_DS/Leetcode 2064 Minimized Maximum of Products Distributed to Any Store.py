'''
Leetcode 2064 Minimized Maximum of Products Distributed to Any Store

You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts,
which are given as 0-indexed integer array quantities, where quantities[i] represent the number of products of the ith product type.
You need to distribute all products to the retail stores following these rules:
A store can only be given at most one product type but can be given any amount of it.
                After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given 
                to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
                Return the minimum possible x. 

Example 1:
        Input: n = 6, quantities = [11,6]
        Output: 3
        Explanation: One optimal way is:
        - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
        - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
        The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

Example 2:
        Input: n = 7, quantities = [15,10,10]
        Output: 5
        Explanation: One optimal way is:
        - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
        - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
        - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
        The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

Example 3:
        Input: n = 1, quantities = [100000]
        Output: 100000
        Explanation: The only optimal way is:
        - The 100000 products of type 0 are distributed to the only store.
        The maximum number of products given to any store is max(100000) = 100000.
         
Constraints:
        m == quantities.length
        1 <= m <= n <= 105
        1 <= quantities[i] <= 105
'''
import math
from typing import List

class Solution:
    def _binarySearchSolution(self, stores: int, products: List[int]) -> int:
        """
        Finds the minimized maximum number of products that each store can hold
        using a binary search approach.

        Parameters:
        - stores (int): The total number of stores available.
        - products (List[int]): A list of product quantities to be distributed.

        Returns:
        - int: The minimized maximum products per store.
        """
        # Sort products in descending order for efficient processing
        products.sort(reverse=True)
        
        # Set binary search bounds
        left, right = 1, max(products)
        result = right

        # Perform binary search on possible maximum products per store
        while left <= right:
            mid = (left + right) // 2
            extra_stores = stores - len(products)  # Extra stores initially available
            
            # Calculate additional stores needed to maintain max products per store <= mid
            for p in products:
                # Calculate how many additional stores are needed for each product
                extra_stores -= (math.ceil(p / mid) - 1)
                if extra_stores < 0:
                    break  # Exit early if extra stores are insufficient
            
            # Adjust binary search bounds based on feasibility of current mid value
            if extra_stores < 0:
                left = mid + 1  # Increase mid if not enough stores
            else:
                result = mid     # Record feasible result
                right = mid - 1  # Decrease mid to check for smaller possible result
                
        return result

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        Determines the minimized maximum number of products that can be allocated
        to each store to ensure all products are distributed evenly.

        Parameters:
        - n (int): The total number of stores.
        - quantities (List[int]): A list of quantities representing products to be distributed.

        Returns:
        - int: The minimized maximum number of products per store.
        """
        # Direct return if number of stores equals number of products
        if n == len(quantities):
            return max(quantities)
        return self._binarySearchSolution(n, quantities)
