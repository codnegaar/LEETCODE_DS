'''
Leetcode 1408 String Matching in an Array

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Example 1:
        Input: words = ["mass","as","hero","superhero"]
        Output: ["as","hero"]
        Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".

["hero","as"] is also a valid answer.
Example 2:        
        Input: words = ["leetcode","et","code"]
        Output: ["et","code"]
        Explanation: "et", "code" are substring of "leetcode".

Example 3:
        Input: words = ["blue","green","bu"]
        Output: []
        Explanation: No string of words is substring of another string.

Constraints:        
        1 <= words.length <= 100
        1 <= words[i].length <= 30
        words[i] contains only lowercase English letters.
        All the strings of words are unique.
'''
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Finds all substrings in the given list of words.

        Parameters:
        words (List[str]): A list of strings to check for substrings.

        Returns:
        List[str]: A list of words that are substrings of other words in the input list.
        """
        # Sort words by length, as substrings must be smaller or equal to other words
        words.sort(key=len)
        substrings = set()  # Use a set to avoid duplicates efficiently
        
        # Iterate through the sorted list
        for i, word in enumerate(words):
            # Check if the current word is a substring of any longer word
            for j in range(i + 1, len(words)):
                if word in words[j]:
                    substrings.add(word)  # Add substring to the result set
                    break  # No need to check further once found
                
        return list(substrings)  # Convert set to list for the final output

# Unit Tests
def test_string_matching():
    solution = Solution()

    # Test cases
    assert solution.stringMatching(["blue", "green", "bu"]) == []
    print("All test cases passed!")

# Run Unit Tests
test_string_matching()

