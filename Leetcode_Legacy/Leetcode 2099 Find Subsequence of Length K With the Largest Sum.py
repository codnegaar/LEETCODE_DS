'''
Leetcode 2099 Find Subsequence of Length K With the Largest Sum

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. 

Example 1:
        Input: nums = [2,1,3,3], k = 2
        Output: [3,3]
        Explanation:
        The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
        Input: nums = [-1,-2,3,4], k = 3
        Output: [-1,3,4]
        Explanation: 
        The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
        Input: nums = [3,4,3,3], k = 2
        Output: [3,4]
        Explanation:
        The subsequence has the largest sum of 3 + 4 = 7. 
        Another possible subsequence is [4, 3]. 

Constraints:
        1 <= nums.length <= 1000
        -105 <= nums[i] <= 105
        1 <= k <= nums.length
'''
from typing import List
from heapq import nlargest

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the subsequence of length k from the input list `nums` that has the
        maximum possible sum, while preserving the original order of elements.

        Parameters:
        nums (List[int]): List of integers to extract the subsequence from.
        k (int): Length of the desired subsequence.

        Returns:
        List[int]: Subsequence of length k with the maximum sum in original order.
        """

        # Step 1: Get the k largest elements along with their original indices
        # Using heapq.nlargest ensures this step is O(n log k)
        top_k_with_index = nlargest(k, enumerate(nums), key=lambda x: x[1])

        # Step 2: Sort the k selected elements by their original indices
        # to preserve the order they appeared in `nums`
        top_k_sorted = sorted(top_k_with_index, key=lambda x: x[0])

        # Step 3: Extract and return only the values from the sorted pairs
        return [value for index, value in top_k_sorted]
