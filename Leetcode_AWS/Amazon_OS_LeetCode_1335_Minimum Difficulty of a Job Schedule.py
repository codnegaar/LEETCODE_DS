'''

LeetCode 1335: Minimum Difficulty of a Job Schedule Solution Amazon OA 2021
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty
of a day is the maximum difficulty of a job done on that day. You are given an integer array jobDifficulty and an integer d. The difficulty of the ith 
job is jobDifficulty[i]. Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
             Second day you can finish the last job, total difficulty = 1.
             The difficulty of the schedule = 6 + 1 = 7 
Note: having factorial in question it means dynamic programming will be useful     
dp(i,j) = at ith job abd J remaining days min difficulty can be calculated

'''


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:        
        # @lru_cache(maxsize=128, typed=False): creating a thin wrapper around a dictionary lookup for the function arguments. 
        @lru_cache(None) 
        def dp(index, remaiDays):
            # first condition
            if remaiDays == 0:
                if index == n:
                    return 0
                else:
                    return sys.maxsize # represent invalid scenario                
            # second condtion    
            if index == n:
                if remaiDays == 0:
                    return 0
                else: 
                    return sys.maxsize
                
            ans = sys.maxsize
            curMax = 0
            for i in range(index, n):
                curMax=max(curMax, jobDifficulty[i])
                ans = min(ans, curMax + dp(i+1, remaiDays-1))
            return ans       
                       
        n =len(jobDifficulty)
        if n < d:
            return -1
        return dp(0,d)   
        
