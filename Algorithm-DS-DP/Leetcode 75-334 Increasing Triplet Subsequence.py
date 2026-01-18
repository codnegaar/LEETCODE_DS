'''
Leetcode 75-334 Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false. 

Example 1:
            Input: nums = [1,2,3,4,5]
            Output: true
            Explanation: Any triplet where i < j < k is valid.
Example 2:
            Input: nums = [5,4,3,2,1]
            Output: false
            Explanation: No triplet exists.
            
Example 3:
            Input: nums = [2,1,5,0,4,6]
            Output: true
            Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
             
Constraints:
            1 <= nums.length <= 5 * 105
            -231 <= nums[i] <= 231 - 1
 
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi=float("inf")
        mi2=float("inf")
        for i in range(len(nums)):
            if nums[i]>mi:
                mi2=min(mi2,nums[i])
            if nums[i]>mi2:
                return True
            mi=min(mi,nums[i])
        return False


# Second solution

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fi = float("inf")
        si = float("inf")
        for num in nums:
            if num <= fi:
                fi = num
            elif num <= si:
                si = num
            else:
                return True

        return False

