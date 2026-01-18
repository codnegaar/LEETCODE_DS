





673 Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.
 
Example 1:
        Input: nums = [1,3,5,4,7]
        Output: 2
        Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
        Input: nums = [2,2,2,2,2]
        Output: 5
        Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 
Constraints:
        1 <= nums.length <= 2000
        -106 <= nums[i] <= 106

class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    # initialize two arrays to store the length of the longest increasing subsequence
    # and the number of such subsequences ending at each index
    dp = [1] * len(nums)
    count = [1] * len(nums)
    # iterate over the input array
    for i in range(len(nums)):
        # iterate over all indices before i
        for j in range(i):
            # check if the current element at i is greater than the element at j
            if nums[i] > nums[j]:
                # if the length of the LIS ending at j plus 1 is greater than
                # the length of the LIS ending at i, update the length of the LIS ending at i
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    # update the number of subsequences ending at i
                    count[i] = count[j]
                # if the length of the LIS ending at j plus 1 is equal to
                # the length of the LIS ending at i, add the number of subsequences
                # ending at j to the number of subsequences ending at i
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]

    # find the length of the longest increasing subsequence
    max_len = max(dp)
    # find the number of subsequences with length equal to the length of the longest increasing subsequence
    return sum([count[i] for i in range(len(nums)) if dp[i] == max_len])
