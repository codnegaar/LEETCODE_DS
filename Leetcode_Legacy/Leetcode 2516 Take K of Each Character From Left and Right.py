'''

Leetcode 2516 Take K of Each Character From Left and Right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
        Input: s = "aabaaaacaabc", k = 2
        Output: 8
        Explanation: 
                    Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
                    Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
                    A total of 3 + 5 = 8 minutes is needed.
                    It can be proven that 8 is the minimum number of minutes needed.

Example 2:
        Input: s = "a", k = 1
        Output: -1
        Explanation: It is not possible to take one 'b' or 'c' so return -1.
         
Constraints:
        1 <= s.length <= 105
        s consists of only the letters 'a', 'b', and 'c'.
        0 <= k <= s.length

'''

from collections import Counter, defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        Determines the minimum time to take at least `k` occurrences of each character ('a', 'b', 'c') 
        from both ends of the string.

        Parameters:
        s (str): The input string containing only characters 'a', 'b', and 'c'.
        k (int): The minimum number of each character required.

        Returns:
        int: The minimum time required, or -1 if it is not possible.
        """
        # Edge case: no characters need to be taken
        if k == 0:
            return 0

        # Count the total occurrences of each character
        total_counts = Counter(s)

        # If any character appears fewer than `k` times, it's impossible to satisfy the condition
        if any(total_counts[char] < k for char in 'abc'):
            return -1

        # Sliding window variables
        left = 0  # Left pointer for the sliding window
        max_window = 0  # Tracks the size of the largest valid window
        current_counts = defaultdict(int)  # Tracks character counts in the current window

        # Expand the window with the right pointer
        for right, char in enumerate(s):
            current_counts[char] += 1

            # Shrink the window from the left if the remaining characters fail the condition
            while total_counts[char] - current_counts[char] < k:
                current_counts[s[left]] -= 1
                left += 1

            # Update the maximum window size
            max_window = max(max_window, right - left + 1)

        # The minimum time is the total length of the string minus the maximum valid window size
        return len(s) - max_window


