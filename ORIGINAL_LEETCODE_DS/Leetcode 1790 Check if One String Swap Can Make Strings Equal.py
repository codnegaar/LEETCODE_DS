'''
Leetcode 1790 Check if One String Swap Can Make Strings Equal
 
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
        Input: s1 = "bank", s2 = "kanb"
        Output: true
        Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
        Input: s1 = "attack", s2 = "defend"
        Output: false
        Explanation: It is impossible to make them equal with one string swap.

Example 3:
        Input: s1 = "kelb", s2 = "kelb"
        Output: true
        Explanation: The two strings are already equal, so no string swap operation is required.         

Constraints:
        1 <= s1.length, s2.length <= 100
        s1.length == s2.length
        s1 and s2 consist of only lowercase English letters.
'''
class Solution:
    """
    A class to determine if two strings are almost equal by swapping at most one pair of characters.
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Checks if two given strings can be made equal by swapping exactly one pair of characters.

        Parameters:
        s1 (str): The first input string.
        s2 (str): The second input string.

        Returns:
        bool: True if the strings can be made equal with at most one swap, otherwise False.
        """
        # If both strings are already equal, return True
        if s1 == s2:
            return True

        # Collect differing character pairs
        diff_pairs = [(a, b) for a, b in zip(s1, s2) if a != b]

        # The strings can only be equal if there are exactly two mismatched pairs,
        # and they must be reverses of each other (i.e., a swap can fix them)
        return len(diff_pairs) == 2 and diff_pairs[0] == diff_pairs[1][::-1]


# Example implementation
solution = Solution()
s1 = "bank"
s2 = "kanb"
print(solution.areAlmostEqual(s1, s2))  # Output: True
