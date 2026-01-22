'''
Leetcode 3507 Minimum Pair Removal to Sort Array I
 
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:
        Input: nums = [5,2,3,1]        
        Output: 2        
        Explanation:        
                The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
                The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
                The array nums became non-decreasing in two operations.

Example 2:
        Input: nums = [1,2,2]
        Output: 0
        Explanation: The array nums is already sorted.

Constraints:
        1 <= nums.length <= 50
        -1000 <= nums[i] <= 1000

'''

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted():
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True
        res = 0
        while not is_sorted():
            index = 0
            prev = nums[0] + nums[1]
            for i in range(2, len(nums)):
                new_sum = nums[i - 1] + nums[i]
                if new_sum < prev:
                    index, prev = i - 1, new_sum
            nums[index : index + 2] = [nums[index] + nums[index + 1]]
            res += 1
        return res
