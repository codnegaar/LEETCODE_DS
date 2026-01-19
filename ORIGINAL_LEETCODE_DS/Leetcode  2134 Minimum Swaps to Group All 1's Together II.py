'''
Leetcode  2134 Minimum Swaps to Group All 1's Together II

A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location. 

Example 1:
        Input: nums = [0,1,0,1,1,0,0]
        Output: 1
        Explanation: Here are a few of the ways to group all the 1's together:
        [0,0,1,1,1,0,0] using 1 swap.
        [0,1,1,1,0,0,0] using 1 swap.
        [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
        There is no way to group all 1's together with 0 swaps.
        Thus, the minimum number of swaps required is 1.

Example 2:
        Input: nums = [0,1,1,1,0,0,1,1,0]
        Output: 2
        Explanation: Here are a few of the ways to group all the 1's together:
        [1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
        [1,1,1,1,1,0,0,0,0] using 2 swaps.
        There is no way to group all 1's together with 0 or 1 swaps.
        Thus, the minimum number of swaps required is 2.

Example 3:
        Input: nums = [1,1,0,0,1]
        Output: 0
        Explanation: All the 1's are already grouped together due to the circular property of the array.
        Thus, the minimum number of swaps required is 0.
 
Constraints:
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.

'''

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)  # Count the number of 1s in the array
        n = len(nums)
        
        # Calculate the number of 1s in the first window of size k
        current_window_sum = sum(nums[:k])
        max_ones_in_window = current_window_sum
        
        # Use a sliding window to find the maximum number of 1s in any window of size k
        for i in range(1, n):
            # Slide the window: add the next element and remove the first element of the previous window
            current_window_sum += nums[(i + k - 1) % n] - nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_window_sum)
        
        # The minimum swaps needed is the difference between the total number of 1s and the maximum number of 1s in any window of size k
        return k - max_ones_in_window
