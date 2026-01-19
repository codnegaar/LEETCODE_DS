'''
Leetcode 1358 Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
        Input: s = "abcabc"
        Output: 10
        Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
        Input: s = "aaacb"
        Output: 3
        Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:        
        Input: s = "abc"
        Output: 1 

Constraints:
        3 <= s.length <= 5 x 10^4
        s only consists of a, b or c characters.

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Calculates the number of substrings containing at least one of each character
        'a', 'b', and 'c'.

        Args:
        s (str): The input string consisting of characters 'a', 'b', and 'c'.

        Returns:
        int: The number of substrings containing at least one of each character.
        """
        count = 0  # Initialize the count of valid substrings
        left = 0  # Initialize the left pointer of the sliding window
        char_count = [0, 0, 0]  # Array to count occurrences of 'a', 'b', 'c'

        # Iterate over each character in the string using 'right' as the right pointer
        for right in range(len(s)):
            # Increment the count for the current character in the sliding window
            char_count[ord(s[right]) - ord('a')] += 1

            # Contract the window until it no longer contains all three characters
            while all(char_count):  # all() is true if none of the counts are zero
                char_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            # For each valid position of 'left', add possible substrings starting from those points
            count += left  # Adding the number of valid start positions for substrings

        return count
