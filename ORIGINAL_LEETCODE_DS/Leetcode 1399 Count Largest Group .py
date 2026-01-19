'''
Leetcode 1399 Count Largest Group 
 
You are given an integer n.
Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size. 

Example 1:
        Input: n = 13
        Output: 4
        Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
        [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
        There are 4 groups with largest size.

Example 2:
        Input: n = 2
        Output: 2
        Explanation: There are 2 groups [1], [2] of size 1.
 
Constraints:
        1 <= n <= 104

'''

from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Count how many groups (based on the sum of digits of numbers from 1 to n) 
        have the largest size.
        
        Parameters:
        n (int): The upper bound of the range (inclusive) of numbers to analyze.
        
        Returns:
        int: The number of groups that have the maximum size.
        """
        # Dictionary to store frequency of each digit sum
        digit_sum_counts = defaultdict(int)
        
        # Track the maximum size of any group
        max_group_size = 0
        
        for i in range(1, n + 1):
            # Calculate digit sum using integer operations (more efficient)
            digit_sum = 0
            x = i
            while x > 0:
                digit_sum += x % 10
                x //= 10

            # Update the count for this digit sum
            digit_sum_counts[digit_sum] += 1
            
            # Update the maximum group size if necessary
            max_group_size = max(max_group_size, digit_sum_counts[digit_sum])
        
        # Count how many groups have the maximum size
        return sum(1 for count in digit_sum_counts.values() if count == max_group_size)
