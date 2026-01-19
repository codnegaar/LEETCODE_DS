'''

Leetcode 1235 Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
        Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
        Output: 120
        Explanation: The subset chosen is the first and fourth job. 
        Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
        Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
        Output: 150
        Explanation: The subset chosen is the first, fourth and fifth job. 
        Profit obtained 150 = 20 + 70 + 60.

Example 3:
        Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
        Output: 6
         
Constraints:
        1 <= startTime.length == endTime.length == profit.length <= 5 * 104
        1 <= startTime[i] < endTime[i] <= 109
        1 <= profit[i] <= 104

'''

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Step 1: Prepare jobs data and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        endTimes = [job[1] for job in jobs]  # Sorted end times for binary search
        n = len(jobs)
        dp = [0] * (n + 1)  # dp[i] stores the max profit using first i jobs
        
        # Step 2: Build the dp array iteratively
        for i in range(1, n + 1):
            # Include current job
            # Binary search to find the first job that does not overlap with current job
            # bisect_right to get the index where current job's start can fit
            index = bisect_right(endTimes, jobs[i-1][0])  # Find the first job that ends before the current job starts
            profit_including_current = jobs[i-1][2] + dp[index]
            
            # Exclude current job (take the profit calculated up to the previous job)
            profit_excluding_current = dp[i-1]
            
            # Max profit of including or not including the current job
            dp[i] = max(profit_including_current, profit_excluding_current)

        # The last element of dp contains the maximum profit obtainable
        return dp[n]

# Example usage:
startTime = [1, 2, 3, 4]
endTime = [3, 5, 4, 6]
profit = [50, 20, 40, 70]
sol = Solution()
print(sol.jobScheduling(startTime, endTime, profit))  # Output should be the maximum profit possible


