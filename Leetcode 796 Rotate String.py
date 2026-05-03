'''
Leetcode 796 Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example 1:        
        Input: s = "abcde", goal = "cdeab"
        Output: true

Example 2:
        Input: s = "abcde", goal = "abced"
        Output: false 

Constraints:
        1 <= s.length, goal.length <= 100
        s and goal consist of lowercase English letters.


'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Checks if the string `goal` is a rotation of the string `s`.
        
        Parameters:
        s (str): The original string.
        goal (str): The target string to check as a rotation of `s`.
        
        Returns:
        bool: True if `goal` is a rotation of `s`, False otherwise.
        
        A string `goal` is considered a rotation of `s` if `goal` can be obtained by 
        shifting `s` some number of times. For example, "abcde" rotated once becomes "bcdea".
        """
        
        # Check if both strings have the same length; if not, `goal` can't be a rotation of `s`
        # Concatenate `s` with itself. If `goal` is a rotation of `s`, it will appear in `s + s`
        return len(s) == len(goal) and goal in (s + s)

