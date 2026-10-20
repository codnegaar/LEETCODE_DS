'''
Leetcode 3886. Sum of Sortable Integers

You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

Partition nums into consecutive subarrays of length k.
Cyclically rotate each subarray independently any number of times to the left or to the right.
Return an integer denoting the sum of all possible sortable integers k.

 

Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:​​​​​​​

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
Only k = 3 is sortable. Hence, the answer is 3.
Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
No k is sortable. Hence, the answer is 0.
Example 3:

Input: nums = [5,8]

Output: 3

Explanation:​​​​​​​

For n = 2, possible divisors are 1 and 2.
Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 105


'''


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        # Prefix maximums
        premax = [0] * n
        premax[0] = nums[0]
        for i in range(1, n):
            premax[i] = max(premax[i - 1], nums[i])

        # Suffix minimums
        sufmin = [0] * n
        sufmin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            sufmin[i] = min(sufmin[i + 1], nums[i])

        # Valid block boundaries
        cut = [True] * n
        for i in range(1, n):
            cut[i] = premax[i - 1] <= sufmin[i]

        # Count descents in each prefix
        desc = [0] * n
        for i in range(1, n):
            desc[i] = desc[i - 1] + (nums[i - 1] > nums[i])

        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for left in range(0, n, k):
                right = left + k - 1

                # The block must start at a valid boundary
                if not cut[left]:
                    valid = False
                    break

                # Count internal descents plus the cyclic descent
                rotations = (
                    desc[right] - desc[left]
                    + (nums[right] > nums[left])
                )

                if rotations > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans

