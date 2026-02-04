'''
Leetcode 3640 Trionic Array II
 
You are given an integer array nums of length n.
A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:
        nums[l...p] is strictly increasing,
        nums[p...q] is strictly decreasing,
        nums[q...r] is strictly increasing.
        Return the maximum sum of any trionic subarray in nums.

 

Example 1:
        Input: nums = [0,-2,-1,-3,0,2,-1]
        Output: -4
        Explanation: 
        Pick l = 1, p = 2, q = 3, r = 5:
                nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
                nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
                nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
                Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.

Example 2:
        Input: nums = [1,4,2,7]
        Output: 14
        Explanation:
        Pick l = 0, p = 1, q = 2, r = 3:
                nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
                nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
                nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
                Sum = 1 + 4 + 2 + 7 = 14.
 
Constraints:
        4 <= n = nums.length <= 105
        -109 <= nums[i] <= 109
        It is guaranteed that at least one trionic subarray exists.
'''

class Solution:
    def decompose(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        n = len(nums)
        subarrays: List[Tuple[int, int, int]] = []

        l = 0
        s = nums[0]

        for i in range(1, n):
            # If we fail strict decreasing at boundary i-1 -> i, end the current subarray.
            if nums[i - 1] <= nums[i]:
                subarrays.append((l, i - 1, s))
                l = i
                s = 0
            s += nums[i]

        # last subarray
        subarrays.append((l, n - 1, s))
        return subarrays

    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        maxEndingAt = [0] * n
        for i in range(n):
            maxEndingAt[i] = nums[i]
            if i > 0 and nums[i - 1] < nums[i]:
                if maxEndingAt[i - 1] > 0:
                    maxEndingAt[i] += maxEndingAt[i - 1]

        maxStartingAt = [0] * n
        for i in range(n - 1, -1, -1):
            maxStartingAt[i] = nums[i]
            if i < n - 1 and nums[i] < nums[i + 1]:
                if maxStartingAt[i + 1] > 0:
                    maxStartingAt[i] += maxStartingAt[i + 1]

        PQS = self.decompose(nums)
        ans = -10**30  
        for (p, q, s) in PQS:
            if (p > 0 and nums[p - 1] < nums[p] and
                q < n - 1 and nums[q] < nums[q + 1] and
                p < q):
                cand = maxEndingAt[p - 1] + s + maxStartingAt[q + 1]
                if cand > ans:
                    ans = cand

        return ans
