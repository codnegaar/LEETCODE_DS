'''
Leetcode 128 Longest Consecutive Sequence 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time. 

Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
 
Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109

'''
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    ans = 0
    seen = set(nums)

    for num in nums:
      if num - 1 in seen:
        continue
      length = 0
      while num in seen:
        num += 1
        length += 1
      ans = max(ans, length)

    return and



# Second solution
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence in an unsorted list of integers.

        Parameters:
        - nums (List[int]): A list of integers.

        Returns:
        - int: The length of the longest consecutive sequence.
        """

        # Use a set for fast lookups
        num_set = set(nums)
        longest_streak = 0

        # Iterate through the set to find the start of each sequence
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:  
                current_num = num
                current_streak = 1

                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak found so far
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Second solution
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Returns the length of the longest consecutive sequence in an unsorted list of integers.

        Parameters:
        - nums (List[int]): A list of integers (can be unsorted and contain duplicates).

        Returns:
        - int: Length of the longest sequence of consecutive integers.
        """

        # Convert the list to a set for O(1) lookup times
        num_set = set(nums)
        longest = 0

        # Iterate through each unique number in the set
        for num in num_set:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                # Continue counting consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    count += 1

                # Update the maximum sequence length
                longest = max(longest, count)

        return longest
