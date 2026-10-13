'''
Leetcode 3727 Maximum Alternating Sum of Squares
 
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 

Constraints:

1 <= nums.length <= 105
-4 * 104 <= nums[i] <= 4 * 104

'''

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq = [x * x for x in nums]
        return sum(sq) - 2 * self.sum_smallest(sq, len(sq) // 2)  # add everything, then flip the smallest half

    def sum_smallest(self, a: list[int], k: int) -> int:  # sum of the k smallest values, O(n) on average
        if k == 0:
            return 0
        pivot = random.choice(a)
        lo = [x for x in a if x < pivot]
        if k <= len(lo):
            return self.sum_smallest(lo, k)  # all k are below the pivot
        take = min(k - len(lo), a.count(pivot))  # then as many pivot copies as needed
        hi = [x for x in a if x > pivot]
        return sum(lo) + take * pivot + self.sum_smallest(hi, k - len(lo) - take)  # the rest come from above
