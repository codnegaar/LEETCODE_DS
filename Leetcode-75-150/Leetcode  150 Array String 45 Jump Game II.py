'''
Leetcode  150- Array-String 45 Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if
you are at nums[i], you can jump to any nums[i + j] where:

        0 <= j <= nums[i] and
        i + j < n
        Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:
        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
        Input: nums = [2,3,0,1,4]
        Output: 2
 

Constraints:
        1 <= nums.length <= 104
        0 <= nums[i] <= 1000
        It's guaranteed that you can reach nums[n - 1].

'''
# First solution DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def min_jumps(index):
            if index>=len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            ans=float('inf')
            for i in range(index,index+nums[index]):
                ans=min(ans,1+min_jumps(i+1))
            memo[index]=ans
            return ans
        return min_jumps(0)
                


# Second Solution-DP

class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n-1)]
        dp+=[0]
        for i in range(n-2,-1,-1):
            for j in range(i+1,min(n,i+nums[i]+1)):
                if dp[j]!=-1:
                    if dp[i]==-1:
                        dp[i]=dp[j]+1
                    else:
                        dp[i]=min(dp[i],dp[j]+1)
        return dp[0]


# Array Solution 
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        res = 0
        curr = 0
        farthest = nums[curr]
        barrier = 0
        while True:
            for positions in range(curr,barrier+1):
                farthest = max(farthest, positions+nums[positions])
            if farthest>=n-1:
                return res+1
            curr = barrier+1
            barrier = farthest
            res+=1
