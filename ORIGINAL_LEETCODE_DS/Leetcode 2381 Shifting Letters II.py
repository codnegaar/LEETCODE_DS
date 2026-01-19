'''
Leetcode 2381 Shifting Letters II

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i,
shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting 
a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.

Example 1:
        Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
        Output: "ace"
        Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
        Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
        Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

Example 2:
        Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
        Output: "catz"
        Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
        Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
         

Constraints:
        1 <= s.length, shifts.length <= 5 * 104
        shifts[i].length == 3
        0 <= starti <= endi < s.length
        0 <= directioni <= 1
        s consists of lowercase English letters.

'''

from typing import List

class Solution:
    """
    Given a string `s` and a list of shifts, shift each character in the string
    based on the provided operations. Each shift operation is a triplet [start, end, direction],
    where direction is either 0 (for left shift) or 1 (for right shift).
    
    Args:
        s (str): The input string.
        shifts (List[List[int]]): List of shifts where each shift is represented as [start, end, direction].

    Returns:
        str: The resulting string after all shifts are applied.
    """

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Apply all the shifts on the input string and return the modified string.

        The approach uses a "difference array" technique to apply shifts efficiently in O(n) time.
        """
        n = len(s)
        
        # Initialize a list to store cumulative changes, using n+1 for boundary convenience.
        shift_diff = [0] * (n + 1)
        
        # Apply all shifts in the shift_diff array.
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_diff[start] += shift_value
            if end + 1 < n:
                shift_diff[end + 1] -= shift_value
        
        # Accumulate the shifts to apply the total shift at each position.
        cumulative_shift = 0
        result = []
        
        for i in range(n):
            cumulative_shift += shift_diff[i]
            # Get the original character, shift it, and apply modulo 26 for wrapping.
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)
        
        # Join and return the modified string
        return ''.join(result)
