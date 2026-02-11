'''
Leetcode 3721 Longest Balanced Subarray II
 
You are given an integer array nums.
A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
Return the length of the longest balanced subarray.
 
Example 1:
        Input: nums = [2,5,4,3]
        Output: 4
        Explanation:
        The longest balanced subarray is [2, 5, 4, 3].
        It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

Example 2:
        Input: nums = [3,2,2,5,4]
        Output: 5
        Explanation:
        The longest balanced subarray is [3, 2, 2, 5, 4].
        It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.

Example 3:
        Input: nums = [1,2,3,2]
        Output: 3
        Explanation:
        The longest balanced subarray is [2, 3, 2].
        It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.         

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 105
'''

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        balance = [0] * n  # first-occurrence markers for current l
        first = dict()  # val -> first occurence idx for current l

        result = 0
        for l in reversed(range(n)):
            x = nums[l]

            # If x already had a first occurrence to the right, remove that old marker.
            if x in first:
                balance[first[x]] = 0

            # Now x becomes first occurrence at l.
            first[x] = l
            balance[l] = 1 if (x & 1) == 0 else -1

            # Find rightmost r >= l such that sum(balance[l..r]) == 0
            s = 0
            for r in range(l, n):
                s += balance[r]
                if s == 0:
                    result = max(result, r - l + 1)

        return result
