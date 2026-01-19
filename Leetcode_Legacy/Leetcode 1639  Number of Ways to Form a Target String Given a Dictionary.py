'''

Leetcode 1639  Number of Ways to Form a Target String Given a Dictionary
 
You are given a list of strings of the same length words and a string target.
Your task is to form a target using the given words under the following rules:
target should be formed from left to right.
To form the ith character (0-indexed) of the target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form a target from words. Since the answer may be too large, return it modulo 109 + 7.
 

Example 1:
        Input: words = ["acca","bbbb","caca"], target = "aba"
        Output: 6
        Explanation: There are 6 ways to form target.
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
        
Example 2:        
        Input: words = ["abba","baab"], target = "bab"
        Output: 4
        Explanation: There are 4 ways to form target.
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
        "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
        "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

Constraints:
        1 <= words.length <= 1000
        1 <= words[i].length <= 1000
        All strings in words have the same length.
        1 <= target.length <= 1000
        words[i] and target contain only lowercase English letters.


'''
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        Calculate the number of ways to form the target string using columns of characters from words.

        Parameters:
        - words (List[str]): List of strings of the same length.
        - target (str): The target string to form.

        Returns:
        - int: The number of ways to form the target string modulo 10^9 + 7.
        """
        n = len(words[0])  # Length of each word (same for all)
        m = len(target)  # Length of the target string
        mod = 10**9 + 7  # Modulo for large numbers

        # Dynamic programming array to store ways to form prefixes of the target
        dp = [0] * (m + 1)
        dp[0] = 1  # Base case: one way to form an empty prefix

        # Precompute frequency of each character in each column
        count = [[0] * 26 for _ in range(n)]  # 26 for 'a' to 'z'
        for i in range(n):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1  # Increment frequency of character in column `i`

        # Update DP table by iterating over columns and target characters in reverse
        for i in range(n):
            for j in range(m - 1, -1, -1):  # Reverse to avoid overwriting results for the current column
                char_index = ord(target[j]) - ord('a')
                if count[i][char_index] > 0:  # Only proceed if the character is present in the column
                    dp[j + 1] += dp[j] * count[i][char_index]
                    dp[j + 1] %= mod  # Take modulo to prevent overflow

        return dp[m]  # Return the number of ways to form the entire target

# Unit Test
def test_numWays():
    """
    Unit tests for the Solution class.
    """
    solution = Solution()

    # Test cases
    assert solution.numWays(["acca", "bbbb", "caca"], "aba") == 6, "Test case 1 failed"
    assert solution.numWays(["abcd", "efgh", "ijkl", "mnop"], "aeim") == 0, "Test case 2 failed"  # Fixing expected value
    assert solution.numWays(["a", "b", "c"], "a") == 1, "Test case 3 failed"
    assert solution.numWays(["abc", "abc", "abc"], "abc") == 27, "Test case 4 failed"
    assert solution.numWays(["aaa", "aaa", "aaa"], "aa") == 27, "Test case 5 failed"

    print("All test cases passed!")

# Example of usage
if __name__ == "__main__":
    test_numWays()
