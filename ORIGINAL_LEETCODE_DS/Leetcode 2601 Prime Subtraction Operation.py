'''
Leetcode 2601 Prime Subtraction Operation

You are given a 0-indexed integer array nums of length n.
You can perform the following operation as many times as you want:
        Pick an index i that you havenΓÇÖt picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
        Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
        A strictly increasing array is an array whose each element is strictly greater than its preceding element.     

Example 1:
        Input: nums = [4,9,6,10]
        Output: true
        Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
        In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
        After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:
        Input: nums = [6,8,11,12]
        Output: true
        Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:
        Input: nums = [5,8,3]
        Output: false
        Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
         

Constraints:
        1 <= nums.length <= 1000
        1 <= nums[i] <= 1000
        nums.length == n

'''

from typing import List

class Solution:
    def check_prime(self, x: int) -> bool:
        """
        Checks if a given number x is prime.
        
        Parameters:
        x (int): The integer to check for primality.
        
        Returns:
        bool: True if x is prime, otherwise False.
        """
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        """
        Determines if the list nums can be made strictly increasing by subtracting 
        prime numbers less than or equal to the current number.

        For each element in nums, subtract the largest prime less than or equal to the element 
        such that the result is greater than the previous element in nums. If possible for all 
        elements, return True. Otherwise, return False.
        
        Parameters:
        nums (List[int]): A list of integers to modify.
        
        Returns:
        bool: True if the list can be made strictly increasing, otherwise False.
        """
        for i in range(len(nums)):
            # Determine the bound for the largest prime to subtract from nums[i].
            bound = nums[i] if i == 0 else nums[i] - nums[i - 1]

            # If bound is non-positive, return False as nums can't be made strictly increasing.
            if bound <= 0:
                return False

            # Find the largest prime less than the bound by iterating downwards from bound - 1.
            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if self.check_prime(j):
                    largest_prime = j
                    break

            # Subtract the found prime from the current element in nums.
            nums[i] -= largest_prime

        return True
