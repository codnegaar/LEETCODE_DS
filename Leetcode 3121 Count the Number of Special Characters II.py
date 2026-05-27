'''
Leetcode 3121 Count the Number of Special Characters II

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word. 

Example 1:
        Input: word = "aaAbcBC"
        Output: 3
        Explanation: The special characters are 'a', 'b', and 'c'.

Example 2:
          Input: word = "abc"
          Output: 0
          Explanation: There are no special characters in word.

Example 3:
          Input: word = "AbBCab"
          Output: 0
          Explanation: There are no special characters in word.

Constraints:
        1 <= word.length <= 2 * 105
        word consists of only lowercase and uppercase English letters.
'''

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        invalid = set()

        for i, ch in enumerate(word):
            letter = ch.lower()

            if ch.islower():
                last_lower[letter] = i

                # lowercase appeared after uppercase
                if letter in first_upper:
                    invalid.add(letter)

            else:
                # store only first uppercase occurrence
                if letter not in first_upper:
                    first_upper[letter] = i

        special_count = 0

        for letter in last_lower:
            if letter in first_upper and letter not in invalid:
                special_count += 1

        return special_count
