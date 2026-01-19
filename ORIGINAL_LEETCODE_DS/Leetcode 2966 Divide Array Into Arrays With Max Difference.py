'''
Leetcode 2966 Divide Array Into Arrays With Max Difference

You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.
Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

Example 1:        
        Input: nums = [1,3,4,8,7,9,3,5,1], k = 2        
        Output: [[1,1,3],[3,4,5],[7,8,9]]        
        Explanation:        
                    The difference between any two elements in each array is less than or equal to 2.

Example 2:

            Input: nums = [2,4,2,2,5,2], k = 2            
            Output: []            
            Explanation:            
                        Different ways to divide nums into 2 arrays of size 3 are:            
                                    [[2,2,2],[2,4,5]] (and its permutations)
                                    [[2,2,4],[2,2,5]] (and its permutations)
                                    Because there are four 2s there will be an array with the elements 2 and 5 no matter how we divide it. since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.

Example 3:

        Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14        
        Output: [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]        
        Explanation:        
                    The difference between any two elements in each array is less than or equal to 14.

 

Constraints:

        n == nums.length
        1 <= n <= 105
        n is a multiple of 3
        1 <= nums[i] <= 105
        1 <= k <= 105


'''

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        # Check if the length of nums is a multiple of 3
        if n % 3 != 0:
            return []

        result = []

        for i in range(0, n, 3):
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return result
