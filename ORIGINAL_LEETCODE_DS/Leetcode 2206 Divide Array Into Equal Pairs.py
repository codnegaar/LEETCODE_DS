'''
Leetcode 2206 Divide Array Into Equal Pairs
 
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Example 1:
        Input: nums = [3,2,3,2,2,2]
        Output: true
        Explanation: 
        There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
        If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:
        Input: nums = [1,2,3,4]
        Output: false
        Explanation: 
        There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition. 

Constraints:
        nums.length == 2 * n
        1 <= n <= 500
        1 <= nums[i] <= 500

'''

from typing import List
from collections import Counter

class Solution:
    """
    A class to determine whether an array can be divided into pairs 
    such that each pair contains equal numbers.
    """

    def divideArray(self, nums: List[int]) -> bool:
        """
        Checks if an array can be partitioned into pairs where each pair has equal elements.

        :param nums: List of integers.
        :return: True if the array can be divided into equal pairs, otherwise False.

        Approach:
        - Count occurrences of each number using `Counter` (O(n) time).
        - If any number appears an **odd number of times**, return False.
        - Otherwise, return True.

        Example:
        >>> Solution().divideArray([3, 2, 3, 2, 2, 2])
        True
        """

        # Count the frequency of each number
        freq = Counter(nums)

        # Check if all counts are even
        return all(count % 2 == 0 for count in freq.values())




