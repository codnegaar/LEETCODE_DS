'''
Given an array of distinct integer nums and a target integer target, return the number of possible combinations that add up to the target.
The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
        Input: nums = [1,2,3], target = 4
        Output: 7
        Explanation:
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.

Example 2:
        Input: nums = [9], target = 3
        Output: 0
 

Constraints:
        1 <= nums.length <= 200
        1 <= nums[i] <= 1000
        All the elements of nums are unique.
        1 <= target <= 1000

'''
class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [1] + [-1] * target

    def dfs(target: int) -> int:
      if target < 0:
        return 0
      if dp[target] != -1:
        return dp[target]

      dp[target] = sum(dfs(target - num) for num in nums)
      return dp[target]

    return dfs(target)


