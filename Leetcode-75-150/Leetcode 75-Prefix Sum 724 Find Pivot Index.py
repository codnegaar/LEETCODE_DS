'''
Leetcode 75-Prefix Sum 724 Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1. 

Example 1:
        Input: nums = [1,7,3,6,5,6]
        Output: 3
        Explanation:
                  The pivot index is 3.
                  Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
                  Right sum = nums[4] + nums[5] = 5 + 6 = 11
        
Example 2:
        Input: nums = [1,2,3]
        Output: -1
        Explanation:
        No index satisfies the conditions in the problem statement.
        
Example 3:
        Input: nums = [2,1,-1]
        Output: 0
        Explanation:
                  The pivot index is 0.
                  Left sum = 0 (no elements to the left of index 0)
                  Right sum = nums[1] + nums[2] = 1 + -1 = 0 

Constraints:
        1 <= nums.length <= 104
        -1000 <= nums[i] <= 1000
 
 '''
 
 class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    summ = sum(nums)
    prefix = 0

    for i, num in enumerate(nums):
      if prefix == summ - prefix - num:
        return i
      prefix += num

    return -1


# Second solution

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total= sum(nums)
        temp = 0
        for i in range(len(nums)):
            if(nums[i] == total - 2*temp): 
                return i
            temp += nums[i]
        return -1

 # Third Solution

# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def pivotIndex(self, nums):
        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        return -1       # If there is no index that satisfies the conditions in the problem statement...
 
