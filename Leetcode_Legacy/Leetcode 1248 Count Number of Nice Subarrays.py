'''

Leetcode 1248 Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
 

Example 1:
        Input: nums = [1,1,2,1,1], k = 3
        Output: 2
        Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
        Input: nums = [2,4,6], k = 1
        Output: 0
        Explanation: There are no odd numbers in the array.

Example 3:
        Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
        Output: 16 

Constraints:
        1 <= nums.length <= 50000
        1 <= nums[i] <= 10^5
        1 <= k <= nums.length

'''
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = count = left = 0
        
        for right in range(len(nums)):
            # Check if the current number is odd
            if nums[right] % 2 == 1:
                k -= 1
                count = 0
            
            # When k is 0, it means we have found k odd numbers
            while k == 0:
                # If the left number is odd, increment k
                k += nums[left] % 2
                count += 1
                left += 1
            
            # Add the count of valid subarrays ending at right
            res += count
        
        return res

