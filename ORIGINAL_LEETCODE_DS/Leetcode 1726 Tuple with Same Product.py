'''
Leetcode 1726 Tuple with Same Product
 
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:
        Input: nums = [2,3,4,6]
        Output: 8
        Explanation: There are 8 valid tuples:
        (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
        (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:
        Input: nums = [1,2,4,5,10]
        Output: 16
        Explanation: There are 16 valid tuples:
        (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
        (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
        (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
        (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
         
Constraints:
        1 <= nums.length <= 1000
        1 <= nums[i] <= 104
        All elements in nums are distinct.
'''

from typing import List
import collections

class Solution:
    """
    A class that provides a method to count valid (a, b, c, d) tuples 
    where a * b = c * d in the given list.
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Finds the number of unique (a, b, c, d) tuples such that a * b = c * d.

        Parameters:
        nums (List[int]): A list of unique positive integers.

        Returns:
        int: The count of valid tuples multiplied by 8 (as per formula).
        """
        count = collections.Counter()  # Hashmap to store product frequencies
        ans = 0  # Stores the final count

        # Iterate through all pairs (i, j) with i > j to avoid duplicates
        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]  # Compute product
                
                # If this product was seen before, add its contribution
                ans += count[prod] * 8  # Each match contributes 8 permutations
                
                # Increment count of this product
                count[prod] += 1

        return ans


# Γ£à Example Usage
solution = Solution()
nums = [2, 3, 4, 6]  # Example case
print(solution.tupleSameProduct(nums))  # Output: 8

