'''

Leetcode 1863 Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:
        Input: nums = [1,3]
        Output: 6
        Explanation: The 4 subsets of [1,3] are:
        - The empty subset has an XOR total of 0.
        - [1] has an XOR total of 1.
        - [3] has an XOR total of 3.
        - [1,3] has an XOR total of 1 XOR 3 = 2.
        0 + 1 + 3 + 2 = 6

Example 2:
        Input: nums = [5,1,6]
        Output: 28
        Explanation: The 8 subsets of [5,1,6] are:
        - The empty subset has an XOR total of 0.
        - [5] has an XOR total of 5.
        - [1] has an XOR total of 1.
        - [6] has an XOR total of 6.
        - [5,1] has an XOR total of 5 XOR 1 = 4.
        - [5,6] has an XOR total of 5 XOR 6 = 3.
        - [1,6] has an XOR total of 1 XOR 6 = 7.
        - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
        0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

Example 3:
        Input: nums = [3,4,5,6,7,8]
        Output: 480
        Explanation: The sum of all XOR totals for every subset is 480.
         

Constraints:
        1 <= nums.length <= 12
        1 <= nums[i] <= 20

'''
# New solution
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through all possible subsets
        for i in range(1 << n):
            subset_xor = 0
            for j in range(n):
                # If the j-th element is in the i-th subset, include it in the XOR calculation
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
            
        return total_sum

# Old Solution
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        # Iterate through all possible subsets
        for i in range(1 << n):
            subset_xor = 0
            for j in range(n):
                # Check if the j-th element is in the i-th subset
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        return total_sum
