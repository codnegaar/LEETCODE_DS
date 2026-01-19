'''
Leetcode 1208 Get Equal Substrings Within Budget
 
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. 
If no substring from s can be changed to its corresponding substring from t, return 0.

Example 1:
        Input: s = "abcd", t = "bcdf", maxCost = 3
        Output: 3
        Explanation: "abc" of s can change to "bcd".
        That costs 3, so the maximum length is 3.
        
Example 2:
        Input: s = "abcd", t = "cdef", maxCost = 3
        Output: 1
        Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
        
Example 3:
        Input: s = "abcd", t = "acde", maxCost = 0
        Output: 1
        Explanation: You cannot make any change, so the maximum length is 1.         

Constraints:
        1 <= s.length <= 105
        t.length == s.length
        0 <= maxCost <= 106
        s and t consist of only lowercase English letters.

'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # Length of the strings (assumed to be of equal length)
        n = len(s) 

        # Initialize the starting index of the sliding window
        start = 0  

        # Tracks the current cost of converting substring of s to substring of t
        current_cost = 0  

        # Stores the maximum length of substring that fits the cost condition
        max_length = 0  

        for end in range(n):

            # Update the cost to include the character at the current end of the window
            current_cost += abs(ord(s[end]) - ord(t[end]))

            # If the current cost exceeds the maximum allowed cost, shrink the window from the start
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))  # Reduce the cost by the start character's cost

                # Move the start of the window to the right
                start += 1  

            # Calculate the length of the current valid window and update max_length if it's the largest found so far
            max_length = max(max_length, end - start + 1)

        # Return the maximum length of substring found
        return max_length  

