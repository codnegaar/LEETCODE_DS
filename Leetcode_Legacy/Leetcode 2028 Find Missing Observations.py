'''
Leetcode 2028 Find Missing Observations

You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls.
Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, 
return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.
Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m. 

Example 1:
        Input: rolls = [3,2,4,3], mean = 4, n = 2
        Output: [6,6]
        Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

Example 2:
        Input: rolls = [1,5,6], mean = 3, n = 4
        Output: [2,3,2,2]
        Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

Example 3:
        Input: rolls = [1,2,3,4], mean = 6, n = 4
        Output: []
        Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
         

Constraints:
        m == rolls.length
        1 <= n, m <= 105
        1 <= rolls[i], mean <= 6

'''

class Solution(object):
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Number of observed rolls
        m = len(rolls)
        
        # Calculate the required total sum for all (n + m) rolls to achieve the target mean
        required_sum = (n + m) * mean
        
        # Calculate the sum of the missing rolls
        missing_sum = required_sum - sum(rolls)
        
        # Check if the missing_sum can be achieved with n rolls, each ranging from 1 to 6
        if missing_sum < n or missing_sum > n * 6:
            return []  # Return empty list if it's not possible to achieve the missing_sum
        
        # Initialize the missing rolls array with the minimum possible value (1) for each roll
        ans = [1] * n
        
        # Calculate the remaining sum needed after initializing each roll with 1
        missing_sum -= n
        
        # Distribute the remaining sum across the rolls
        for i in range(n):
            # Add the minimum of the remaining sum or the maximum value that can be added (5)
            add_value = min(5, missing_sum)
            ans[i] += add_value
            missing_sum -= add_value
            
            # If no remaining sum, break out of the loop
            if missing_sum == 0:
                break
        
        return ans
