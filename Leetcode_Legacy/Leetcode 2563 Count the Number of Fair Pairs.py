'''

Leetcode 2563 Count the Number of Fair Pairs

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:        
        0 <= i < j < n, and
        lower <= nums[i] + nums[j] <= upper
 

Example 1:
        Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
        Output: 6
        Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
        Input: nums = [1,7,9,2,5], lower = 11, upper = 11
        Output: 1
        Explanation: There is a single fair pair: (2,3).
         

Constraints:
        1 <= nums.length <= 105
        nums.length == n
        -109 <= nums[i] <= 109
        -109 <= lower <= upper <= 109

'''

from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        """
        Counts the number of fair pairs in the list 'v' such that 
        the sum of the pairs falls between 'lower' and 'upper' bounds.
        
        Parameters:
        v (List[int]): A list of integers.
        lower (int): The lower bound for the sum of the pairs.
        upper (int): The upper bound for the sum of the pairs.

        Returns:
        int: The count of fair pairs meeting the criteria.
        """
        # Sort the array for easier searching with binary search
        v.sort()
        ans = 0

        # Iterate through the array, treating each element as the first element in the pair
        for i in range(len(v) - 1):
            # Use bisect to find the valid range in which the second element of the pair falls
            low = bisect_left(v, lower - v[i], i + 1)    # Lower bound index for valid pairs
            up = bisect_right(v, upper - v[i], i + 1)    # Upper bound index for valid pairs
            ans += up - low                              # Add the count of valid pairs

        return ans

