'''
Leetcode 2501 Longest Square Streak in an Array

You are given an integer array nums. A subsequence of nums is called a square streak if:
The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
        Input: nums = [4,3,6,16,8,2]
        Output: 3
        Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
        - 4 = 2 * 2.
        - 16 = 4 * 4.
        Therefore, [4,16,2] is a square streak.
        It can be shown that every subsequence of length 4 is not a square streak.

Example 2:        
        Input: nums = [2,3,5,6,7]
        Output: -1
        Explanation: There is no square streak in nums so return -1.
         

Constraints:
        2 <= nums.length <= 105
        2 <= nums[i] <= 105


'''

 from math import isqrt

class Solution:
    def longestSquareStreak(self, nums):
        """
        Finds the longest streak in the input list where each element is a perfect square of the previous element.

        Parameters:
        nums (List[int]): A list of positive integers.

        Returns:
        int: The length of the longest streak of perfect squares. Returns -1 if no such streak exists.
        """
        # Dictionary to keep track of streak length for each number
        streak_map = {}
        nums.sort()  # Sort the numbers to ensure we can identify streaks sequentially
        max_streak = -1  # Initialize the result as -1 (no streak found)

        for num in nums:
            # Calculate the integer square root of the current number
            sqrt = isqrt(num)

            # Check if current number is a perfect square and the square root has been seen before
            if sqrt * sqrt == num and sqrt in streak_map:
                streak_map[num] = streak_map[sqrt] + 1
                max_streak = max(max_streak, streak_map[num])
            else:
                streak_map[num] = 1

        return max_streak

# Example usage
sol = Solution()
print(sol.longestSquareStreak([4, 2, 16, 256, 65536]))  # Example input
