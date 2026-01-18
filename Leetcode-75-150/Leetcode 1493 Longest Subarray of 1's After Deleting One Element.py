'''
Leetcode 1493 Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray. 

Example 1:
        Input: nums = [1,1,0,1]
        Output: 3
        Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
        
Example 2:
        Input: nums = [0,1,1,1,0,1,1,0,1]
        Output: 5
        Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
        
Example 3:
        Input: nums = [1,1,1]
        Output: 2
        Explanation: You must delete one element.
 
Constraints:
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
        
'''
class Solution:
  def longestSubarray(self, nums: List[int]) -> int:

    left_pointer = 0
    count_zero = 0

    for num in nums:
      if num == 0:
        count_zero += 1
      if count_zero > 1:
        if nums[left_pointer] == 0:
          count_zero -= 1
        left_pointer += 1

    return len(nums) - left_pointer - 1

# Second solution
from typing import List, Tuple


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Compute the length of the longest subarray consisting of 1s after deleting exactly one element.
        (LeetCode 1493: Longest Subarray of 1's After Deleting One Element)

        Parameters
        ----------
        nums : List[int]
            A list of integers containing only 0s and 1s.

        Returns
        -------
        int
            The maximum length of a subarray containing only 1s after deleting one element.

        Notes
        -----
        - Uses a sliding-window that keeps at most one zero inside the window.
        - Because we must delete exactly one element, the candidate length for any valid window
          is `window_size - 1`, which simplifies to `right - left` when the window is [left, right].
        - Time Complexity: O(n) — each index moves left→right at most once.
        - Space Complexity: O(1).

        Examples
        --------
        >>> Solution().longestSubarray([1,1,0,1])
        3
        >>> Solution().longestSubarray([0,0,0])
        0
        >>> Solution().longestSubarray([1,1,1])
        2
        """
        left = 0              # Left edge of the sliding window
        zeros = 0             # Number of zeros inside the current window
        best = 0              # Best (max) result found so far

        for right, val in enumerate(nums):
            if val == 0:      # Expand window: include nums[right]
                zeros += 1

            # Shrink window while it contains more than one zero
            left, zeros = self._shrink_window(nums, left, zeros)

            # Candidate length = window_size - 1 = (right - left + 1) - 1 = right - left
            best = max(best, right - left)

        return best

    @staticmethod
    def _shrink_window(nums: List[int], left: int, zeros: int) -> Tuple[int, int]:
        """
        Move the left pointer rightward until the window contains at most one zero.

        Parameters
        ----------
        nums : List[int]
            The original binary array.
        left : int
            Current left edge of the window (inclusive).
        zeros : int
            Current count of zeros inside the window.

        Returns
        -------
        Tuple[int, int]
            The updated (left, zeros) after shrinking as needed.
        """
        # Advance 'left' until we have at most one zero in the window
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1    # We drop a zero from the window
            left += 1
        return left, zeros


if __name__ == "__main__":
    # Quick sanity checks
    assert Solution().longestSubarray([1, 1, 0, 1]) == 3
    assert Solution().longestSubarray([0, 0, 0]) == 0
    assert Solution().longestSubarray([1, 1, 1]) == 2
    assert Solution().longestSubarray([1, 0, 1, 1, 0, 1]) == 3
    print("All tests passed.")

