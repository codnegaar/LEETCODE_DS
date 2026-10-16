'''

Leetcode 2916 Subarrays Distinct Element Sum of Squares II
 
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105


'''
MOD = 1_000_000_007


class SegmentTreeNode:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.val = 0
        self.lazy = 0
        if lo + 1 < hi:
            mid = (lo + hi) // 2
            self.left = SegmentTreeNode(lo, mid)
            self.right = SegmentTreeNode(mid, hi)

    def update(self, val):
        self.lazy += val
        self.val += val * (self.hi - self.lo)

    def query(self, lo, hi):
        if self.lo >= lo and self.hi <= hi:
            res = self.val
            self.update(1)
            return res
        mid = (self.lo + self.hi) // 2
        res = 0
        self.left.update(self.lazy)
        self.right.update(self.lazy)
        self.lazy = 0
        if lo < mid:
            res += self.left.query(lo, hi)
        if hi > mid:
            res += self.right.query(lo, hi)
        self.val = self.left.val + self.right.val
        return res


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        last_idx_dict = {}
        segment_tree = SegmentTreeNode(0, len(nums))
        res = 0
        curr_res = 0
        for i, num in enumerate(nums):
            last_idx = last_idx_dict.get(num, -1) + 1
            curr_res = (
                curr_res + i - last_idx + 1 + 2 * segment_tree.query(last_idx, i + 1)
            ) % MOD
            res += curr_res
            last_idx_dict[num] = i
        return res % MOD
