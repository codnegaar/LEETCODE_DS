'''
Leetcode 1262 Greatest Sum Divisible by Three
 
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:
        Input: nums = [3,6,5,1,8]
        Output: 18
        Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:
        Input: nums = [4]
        Output: 0
        Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
        Input: nums = [1,2,3,4,4]
        Output: 12
        Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
         
Constraints:
        1 <= nums.length <= 4 * 104
        1 <= nums[i] <= 104

'''
from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        INF = 10**9
        r1_min1 = INF
        r1_min2 = INF
        r2_min1 = INF
        r2_min2 = INF

        for x in nums:
            total += x
            r = x % 3
            if r == 1:
                if x < r1_min1:
                    r1_min2 = r1_min1
                    r1_min1 = x
                elif x < r1_min2:
                    r1_min2 = x
            elif r == 2:
                if x < r2_min1:
                    r2_min2 = r2_min1
                    r2_min1 = x
                elif x < r2_min2:
                    r2_min2 = x

        mod = total % 3
        if mod == 0:
            return total

        remove_cost = 10**18

        if mod == 1:
            if r1_min1 != INF:
                remove_cost = min(remove_cost, r1_min1)
            if r2_min2 != INF:
                remove_cost = min(remove_cost, r2_min1 + r2_min2)
        else:  # mod == 2
            if r2_min1 != INF:
                remove_cost = min(remove_cost, r2_min1)
            if r1_min2 != INF:
                remove_cost = min(remove_cost, r1_min1 + r1_min2)

        if remove_cost >= 10**18:
            return 0
        return total - remove_cost
 
