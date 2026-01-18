'''

Leetcode (75) 238 Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp=[]
        product=1
        for i in nums:
            dp.append(product)
            product*=i
        product=1
            '''
            The code for i in range(len(array)-1,-1,-1) is a for loop that iterates over the indices of a list array in reverse order.
            The loop starts at the index len(array)-1 and ends at index 0 (inclusive) with a step of -1. This means that the loop will
            iterate over the indices of the list in reverse order, starting from the last element and ending at the first element.
            array = [1, 2, 3, 4, 5]
            for i in range(len(array)-1, -1, -1):
                    print(array[i]) --> 5,4,3,2,1
            '''
        for i in range(len(nums)-1,-1,-1):
            dp[i]=dp[i]*product
            product*=nums[i]
        return dp
 
            
            
            
            
        
        
