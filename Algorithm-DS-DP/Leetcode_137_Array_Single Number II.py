'''
Leetcode_137_Single Number II
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
        Input: nums = [2,2,3,2]
        Output: 3
Example 2:
       Input: nums = [0,1,0,1,0,1,99]
       Output: 99
''''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:    
   
        single = 0
        repeated =0
     
        for num in nums:
          single    = single ^ num & ~repeated
          repeated  = repeated ^ num & ~single

        return single
