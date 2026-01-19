'''
Leetcode 2337 Move Pieces to Obtain a String

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
        The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, 
        and a piece 'R' can move to the right only if there is a blank space directly to its right.
        The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
        Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

Example 1:
          Input: start = "_L__R__R_", target = "L______RR"
          Output: true
          Explanation: We can obtain the string target from start by doing the following moves:
          - Move the first piece one step to the left, start becomes equal to "L___R__R_".
          - Move the last piece one step to the right, start becomes equal to "L___R___R".
          - Move the second piece three steps to the right, start becomes equal to "L______RR".
          Since it is possible to get the string target from start, we return true.

Example 2:
        Input: start = "R_L_", target = "__LR"
        Output: false
        Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
        After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

Example 3:
        Input: start = "_R", target = "R_"
        Output: false
        Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
         
Constraints:
        n == start.length == target.length
        1 <= n <= 105
        start and target consist of the characters 'L', 'R', and '_'.

'''

class Solution:
    def canChange(self, s: str, t: str) -> bool:
        """
        Determines if it is possible to transform the given string `s` to string `t` 
        by shifting 'L' and 'R' characters to the left or right under the given conditions.
        
        Parameters:
        - s (str): The initial string with characters 'L', 'R', and '_' (representing empty spaces).
        - t (str): The target string with the same set of characters to be transformed.
        
        Returns:
        - bool: True if `s` can be transformed to `t` using the given rules, otherwise False.
        """
        
        # Length of the input strings
        n = len(s)
        
        # Append '@' to both strings to mark the end boundary for easier comparisons
        s += '@'
        t += '@'
        
        # Initialize two pointers to traverse both strings
        i, j = 0, 0
        
        # Traverse both strings until we reach the end
        while i < n or j < n:
            
            # Skip all underscores in `s`
            while i < n and s[i] == '_':
                i += 1
            
            # Skip all underscores in `t`
            while j < n and t[j] == '_':
                j += 1
            
            # If characters don't match, transformation is not possible
            if s[i] != t[j]:
                return False
            
            # If the character is 'L' and `i` is less than `j`, transformation is not possible
            # (since 'L' can only move left)
            if s[i] == 'L' and i < j:
                return False
            
            # If the character is 'R' and `i` is greater than `j`, transformation is not possible
            # (since 'R' can only move right)
            if s[i] == 'R' and i > j:
                return False
            
            # Move both pointers forward
            i += 1
            j += 1
        
        # If we reach this point, transformation is possible
        return True

# Unit test
import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_can_change_basic(self):
        self.assertTrue(self.solution.canChange("_L__R__R_", "L______RR"))
    
    def test_can_change_impossible_L(self):
        self.assertFalse(self.solution.canChange("_L__R__R_", "_L_R_R__R"))

    def test_can_change_impossible_R(self):
        self.assertFalse(self.solution.canChange("R_L_", "_RL_"))

    def test_can_change_equal(self):
        self.assertTrue(self.solution.canChange("_L_R_", "_L_R_"))

    def test_can_change_no_LR(self):
        self.assertTrue(self.solution.canChange("____", "____"))

    def test_can_change_extra_case(self):
        self.assertFalse(self.solution.canChange("L_R_", "R_L_"))

# Run the unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
