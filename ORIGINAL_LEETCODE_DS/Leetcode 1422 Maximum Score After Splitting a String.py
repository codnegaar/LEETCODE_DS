'''
Leetcode 1422 Maximum Score After Splitting a String
 
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring. 

Example 1:
          Input: s = "011101"
          Output: 5 
          Explanation: 
                    All possible ways of splitting s into two non-empty substrings are:
                    left = "0" and right = "11101", score = 1 + 4 = 5 
                    left = "01" and right = "1101", score = 1 + 3 = 4 
                    left = "011" and right = "101", score = 1 + 2 = 3 
                    left = "0111" and right = "01", score = 1 + 1 = 2 
                    left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
        Input: s = "00111"
        Output: 5
        Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
        Input: s = "1111"
        Output: 3 

Constraints:
        2 <= s.length <= 500
        The string s consists of characters '0' and '1' only.
        
'''
class Solution:
    def maxScore(self, s: str) -> int:
      
        """
        Calculate the maximum score by splitting a binary string into two non-empty parts.        
        The score is calculated as the sum of zeros in the left part and ones in the right part.        
        Parameters:
        s (str): The input binary string containing only '0's and '1's.        
        Returns:
        int: The maximum score obtainable.
        """
      
        # Initialize counts
        zeros_left = 0
        ones_right = s.count('1')  # Count all ones initially in the right segment
        max_score = 0

        # Traverse the string excluding the last character
        for i in range(len(s) - 1):
            # Update counts based on the current character
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
            # Calculate and update maximum score
            max_score = max(max_score, zeros_left + ones_right)

        return max_score
