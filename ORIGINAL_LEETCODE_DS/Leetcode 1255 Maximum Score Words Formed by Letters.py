'''

Leetcode 1255 Maximum Score Words Formed by Letters
 
Given a list of words, list of  single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z'
is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        Output: 23
        Explanation:
                Score  a=1, c=9, d=5, g=3, o=2
                Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
                Words "dad" and "dog" only get a score of 21.

        
Example 2:
        Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
        Output: 27
        Explanation:
                Score  a=4, b=4, c=4, x=5, z=10
                Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
                Word "xxxz" only get a score of 25.

Example 3:        
        Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
        Output: 0
        Explanation:
                Letter "e" can only be used once.
 
Constraints:
        1 <= words.length <= 14
        1 <= words[i].length <= 15
        1 <= letters.length <= 100
        letters[i].length == 1
        score.length == 26
        0 <= score[i] <= 10
        words[i], letters[i] contains only lower case English letters.

'''

from typing import List
from collections import Counter
import copy

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Calculate the maximum score by forming words from a specified list using available letters.
        Each letter has a corresponding score, and each word can only be formed if all its characters
        can be provided by the letters available, each used no more than once.

        Args:
        words (List[str]): List of words that can be formed.
        letters (List[str]): Available letters that can be used to form words.
        score (List[int]): Scores corresponding to each letter from 'a' to 'z'.

        Returns:
        int: The maximum score possible by forming words from the given list.
        """
        
        # Create a counter for the letters to keep track of the counts of each available letter
        lettersCounter = Counter(letters)
        totalScore = 0  # Initialize total score

        def explore(index, letterCounter, currScore):
            nonlocal totalScore
            totalScore = max(totalScore, currScore)  # Update the global maximum score
            if index == len(words):
                return  # End recursion if all words are considered

            for i in range(index, len(words)):
                tmpCounter = copy.deepcopy(letterCounter)  # Copy letter counter for backtracking
                word = words[i]
                wordScore = 0
                isValid = True  # Flag to check if the word can be formed

                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord('a')]  # Calculate score for the word
                    else:
                        isValid = False  # Break if a letter is missing
                        break

                if isValid:
                    explore(i + 1, tmpCounter, currScore + wordScore)  # Recurse with the next word

        explore(0, lettersCounter, 0)  # Start recursion
        return totalScore

# Example usage:
sol = Solution()
print(sol.maxScoreWords(["dog", "cat"], ["d", "o", "g", "c", "a", "t"], [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
