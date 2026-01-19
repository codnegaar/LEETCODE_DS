'''
Leetcode 2275 Largest Combination With Bitwise AND Greater Than Zero

The bitwise AND of an array nums is the bitwise AND of all integers in nums.
For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1. Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of 
candidates. Each number in candidates may only be used once in each combination.
Return the size of the largest combination of candidates with a bitwise AND greater than 0.

Example 1:
        Input: candidates = [16,17,71,62,12,24,14]
        Output: 4
        Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
        The size of the combination is 4.
        It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
        Note that more than one combination may have the largest size.
        For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

Example 2:
        Input: candidates = [8,8]
        Output: 2
        Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
        The size of the combination is 2, so we return 2.
      
Constraints:
        1 <= candidates.length <= 105
        1 <= candidates[i] <= 107

'''
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        Finds the largest combination where the count of set bits is maximized across all candidates.

        Parameters:
        candidates (List[int]): A list of positive integers representing the candidates.

        Returns:
        int: The maximum number of candidates that have a particular bit set at the same position.
        """
        
        # The number of bits we need to check depends on the input range, assuming 32 bits is enough.
        max_bit_count = 0
        
        # Loop through each bit position (0 to 31)
        for bit_position in range(32):
            bit_count = 0  # Counter to track how many candidates have the current bit set
            
            # Count how many candidates have the 'bit_position'-th bit set
            for candidate in candidates:
                if candidate & (1 << bit_position):
                    bit_count += 1

            # Update max_bit_count if current bit count is larger
            max_bit_count = max(max_bit_count, bit_count)

        return max_bit_count
