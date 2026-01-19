'''
Leetcode 1749 Maximum Absolute Sum of Any Subarray

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
        If x is a negative integer, then abs(x) = -x.
        If x is a non-negative integer, then abs(x) = x.
 
Example 1:
        Input: nums = [1,-3,2,3,-4]
        Output: 5
        Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:        
        Input: nums = [2,-5,1,-4,3,-2]
        Output: 8
        Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
         

Constraints:        
        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
'''

class Solution:
    """
    This class provides a method to compute the maximum absolute sum 
    of any subarray within a given integer array.
    """

    def maxAbsoluteSum(self, nums):
        """
        Finds the maximum absolute sum of any subarray in the given list.
        
        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        int: The maximum absolute sum of any subarray.
        """

        # Initialize tracking variables for max and min subarray sums
        max_sum = min_sum = max_abs_sum = 0

        # KadaneΓÇÖs Algorithm to find the max and min subarray sums
        for num in nums:
            # Update the max subarray sum ending at the current index
            max_sum = max(num, max_sum + num)
            # Update the min subarray sum ending at the current index
            min_sum = min(num, min_sum + num)
            # Update the maximum absolute sum encountered
            max_abs_sum = max(max_abs_sum, abs(max_sum), abs(min_sum))

        return max_abs_sum


# Example usage
nums = [1, -3, 2, 3, -4]
solution = Solution()
result = solution.maxAbsoluteSum(nums)
print(f"Maximum Absolute Sum of Any Subarray: {result}")

