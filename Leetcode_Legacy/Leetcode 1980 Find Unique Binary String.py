'''
Leetcode 1980 Find Unique Binary String
 
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
If there are multiple answers, you may return any of them. 

Example 1:
        Input: nums = ["01","10"]
        Output: "11"
        Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
        Input: nums = ["00","01"]
        Output: "11"
        Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
        Input: nums = ["111","011","001"]
        Output: "101"
        Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
         
Constraints:
        n == nums.length
        1 <= n <= 16
        nums[i].length == n
        nums[i] is either '0' or '1'.
        All the strings of nums are unique.




'''

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Finds a binary string that is not present in the given list of binary strings.

        Uses Cantor's Diagonalization method to ensure uniqueness.

        Parameters:
        -----------
        nums : List[str]
            A list of unique binary strings, each of length `n`.

        Returns:
        --------
        str
            A binary string of length `n` that is guaranteed to be different from all in `nums`.
        """
        n = len(nums)  # The length of each binary string and number of strings

        # Ensure each binary string has the correct length
        assert all(len(num) == n for num in nums), "All strings must have length `n`"

        # Generate a unique binary string using Cantor's diagonalization technique
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))

 
