'''
Leetcode 1524 Number of Sub-arrays With Odd Sum

Given an array of integers arr, return the number of subarrays with an odd sum. Since the answer can be very large, return it modulo 109 + 7. 

Example 1:
        Input: arr = [1,3,5]
        Output: 4
        Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
        All sub-arrays sum are [1,4,9,3,8,5].
        Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
        Input: arr = [2,4,6]
        Output: 0
        Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
        All sub-arrays sum are [2,6,12,4,10,6].
        All sub-arrays have even sum and the answer is 0.

Example 3:
        Input: arr = [1,2,3,4,5,6,7]
        Output: 16 

Constraints:
        1 <= arr.length <= 105
        1 <= arr[i] <= 100
'''

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Counts the number of contiguous subarrays with an odd sum.

        Args:
            arr (List[int]): A list of integers.

        Returns:
            int: The number of subarrays with an odd sum, modulo (10^9 + 7).
        """
        MOD = 10**9 + 7  # Large prime number for modulo operation
        
        odd_count = 0     # Tracks the count of subarrays with odd sum
        even_count = 1    # Tracks the count of subarrays with even sum (initialized to 1 for empty prefix)
        prefix_parity = 0 # Tracks the cumulative sum's parity (0 for even, 1 for odd)
        result = 0        # Stores the final count of odd sum subarrays

        # Iterate through the array
        for num in arr:
            prefix_parity ^= (num & 1)  # Toggle parity if the number is odd
            
            if prefix_parity:  # If current prefix sum is odd
                result += even_count  # Add count of previous even subarrays
                odd_count += 1  # Increase count of odd sum subarrays
            else:  # If current prefix sum is even
                result += odd_count  # Add count of previous odd subarrays
                even_count += 1  # Increase count of even sum subarrays
            
            result %= MOD  # Keep result within modulo range

        return result

# Example Usage
arr = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.numOfSubarrays(arr))  # Output: 8




