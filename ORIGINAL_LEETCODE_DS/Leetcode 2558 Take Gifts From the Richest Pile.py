'''
Leetcode 2558 Take Gifts From the Richest Pile

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

Example 1:
          Input: gifts = [25,64,9,4,100], k = 4
          Output: 29
          Explanation: 
          The gifts are taken in the following way:
          - In the first second, the last pile is chosen and 10 gifts are left behind.
          - Then the second pile is chosen and 8 gifts are left behind.
          - After that the first pile is chosen and 5 gifts are left behind.
          - Finally, the last pile is chosen again and 3 gifts are left behind.
          The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

Example 2:
        Input: gifts = [1,1,1,1], k = 4
        Output: 4
        Explanation: 
        In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
        That is, you can't take any pile with you. 
        So, the total gifts remaining are 4.
         
Constraints:
        1 <= gifts.length <= 103
        1 <= gifts[i] <= 109
        1 <= k <= 103
'''


import math
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        Simulates picking and replacing the maximum gift values over k iterations.

        Parameters:
        gifts (List[int]): A list of integers representing the number of gifts in each box.
        k (int): The number of iterations to perform the operation.

        Returns:
        int: The sum of the gift values after k operations.
        """

        # Convert gifts list to a max heap by negating all values (Python supports min heap by default)
        nums = [-num for num in gifts]
        heapify(nums)

        # Perform k operations
        for _ in range(k):
            # Pop the maximum value (smallest negative value), compute its square root,
            # and push the negated square root back into the heap
            largest = -heappop(nums)
            reduced_value = math.isqrt(largest)
            heappush(nums, -reduced_value)

        # Return the sum of the final heap (convert negatives back to positives)
        return -sum(nums)

# Unit tests
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    gifts1 = [9, 7, 16]
    k1 = 2
    result1 = solution.pickGifts(gifts1, k1)
    print(f"After {k1} operations, sum of gifts: {result1}")  # Expected output: 16

    # Example 2
    gifts2 = [4, 16, 25]
    k2 = 3
    result2 = solution.pickGifts(gifts2, k2)
    print(f"After {k2} operations, sum of gifts: {result2}")  # Expected output: 12

    # Edge case: Single gift box
    gifts3 = [100]
    k3 = 5
    result3 = solution.pickGifts(gifts3, k3)
    print(f"After {k3} operations, sum of gifts: {result3}")  # Expected output: 1

    # Edge case: No operation
    gifts4 = [1, 2, 3]
    k4 = 0
    result4 = solution.pickGifts(gifts4, k4)
    print(f"After {k4} operations, sum of gifts: {result4}")  # Expected output: 6
