'''

Leetcode 1590 Make Sum Divisible by P

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.

Example 1:
        Input: nums = [3,1,4,2], p = 6
        Output: 1
        Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
        Input: nums = [6,3,5,2], p = 9
        Output: 2
        Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:
        Input: nums = [1,2,3], p = 3
        Output: 0
        Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
         

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109
        1 <= p <= 109

'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Calculate total sum and its remainder when divided by p
        total_sum = sum(nums)
        remainder = total_sum % p

        # If the total sum is already divisible by p, return 0 (no subarray removal required)
        if remainder == 0:
            return 0

        # Dictionary to store prefix sum modulo p and its index
        prefix_mod_map = {0: -1}
        prefix_sum = 0
        min_length = len(nums)

        # Iterate through nums to calculate prefix sums and check for target subarrays
        for i, num in enumerate(nums):
            prefix_sum += num
            current_mod = prefix_sum % p
            target_mod = (current_mod - remainder + p) % p

            # If a prefix with the required mod was seen before, calculate subarray length
            if target_mod in prefix_mod_map:
                min_length = min(min_length, i - prefix_mod_map[target_mod])

            # Store the current prefix mod and its index
            prefix_mod_map[current_mod] = i

        # If min_length is smaller than the entire array, return it, otherwise return -1
        return min_length if min_length < len(nums) else -1
