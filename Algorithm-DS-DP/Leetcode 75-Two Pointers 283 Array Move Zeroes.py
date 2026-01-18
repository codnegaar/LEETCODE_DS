'''

Leetcode 75-Two Pointers 283 Array Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.


'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lptr = 0
        for rptr in range (len(nums)):
            if nums[rptr]:
                nums[lptr], nums [rptr] = nums [rptr],  nums[lptr]
                lptr += 1

# second solution
﻿class Solution:
    def moveZeroes (self, nums: List[int]) -> None:
        base=0
        for i in range(len(nums)):
            if nums[i]=0:
                nums[base], nums[i] = nums[i], nums[base] 
                base += 1
