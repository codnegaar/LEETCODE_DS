'''
Leetcode 2185 Counting Words With a Given Prefix
 
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s. 

Example 1:
        Input: words = ["pay","attention","practice","attend"], pref = "at"
        Output: 2
        Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
        Input: words = ["leetcode","win","loops","success"], pref = "code"
        Output: 0
        Explanation: There are no strings that contain "code" as a prefix.
         
Constraints:
        1 <= words.length <= 100
        1 <= words[i].length, pref.length <= 100
        words[i] and pref consist of lowercase English letters.
'''
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Count the number of words in a list that start with a given prefix.
        
        Parameters:
            words (List[str]): A list of words to check.
            pref (str): The prefix to look for.
        
        Returns:
            int: The number of words starting with the given prefix.
        """
        # Using sum with a generator expression for cleaner and efficient iteration
        return sum(word.startswith(pref) for word in words)


# Unit Tests
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    print(solution.prefixCount(["apple", "apricot", "banana", "app"], "ap"))  # Expected: 3
    print(solution.prefixCount(["test", "testing", "tester", "tent"], "te"))  # Expected: 4
    print(solution.prefixCount(["hello", "world", "hi", "house"], "ho"))     # Expected: 1
    print(solution.prefixCount(["prefix", "prefixed", "pre", "post"], "pre"))# Expected: 3
    print(solution.prefixCount(["cat", "dog", "fish"], "z"))                 # Expected: 0
