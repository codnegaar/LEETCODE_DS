'''
Leetcode 1636 Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Example 1:
        Input: nums = [1,1,2,2,2,3]
        Output: [3,1,1,2,2,2]
        Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
        
Example 2:
        Input: nums = [2,3,1,3,2]
        Output: [1,3,3,2,2]
        Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
        
Example 3:
        Input: nums = [-1,1,-6,4,5,-6,1,4,1]
        Output: [5,-1,4,4,-6,-6,1,1,1] 

Constraints:
        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
'''
from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Get frequency of each number using Counter
        freq = Counter(nums)
        
        # Sort nums based on two criteria:
        # 1. Frequency in ascending order (less frequent first).
        # 2. If frequencies are the same, sort by the number itself in descending order.
        return sorted(nums, key=lambda x: (freq[x], -x))
