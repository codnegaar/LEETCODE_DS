'''
Leetcode 127 Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 Example 1:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
         

Constraints:
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.

'''

import collections
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], alphabet: str = string.ascii_lowercase) -> int:
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        
        # If the endWord is not in the wordList, we can't transform to it
        if endWord not in wordSet:
            return 0

        # Initialize the queue for BFS starting with the beginWord
        queue = collections.deque([beginWord])
        steps = 1  # Track the transformation steps (start with 1 to count beginWord)

        while queue:
            # Iterate over all current words in the queue
            for _ in range(len(queue)):
                currentWord = queue.popleft()
                
                # Try changing each letter in the current word
                for i in range(len(currentWord)):
                    original_char = currentWord[i]
                    
                    # Try every possible letter in the alphabet (default a-z)
                    for char in alphabet:
                        # Skip if the character is the same as the original
                        if char == original_char:
                            continue
                        
                        # Form the new word by replacing the i-th character
                        newWord = currentWord[:i] + char + currentWord[i+1:]
                        
                        # If we find the endWord, return the steps count + 1
                        if newWord == endWord:
                            return steps + 1
                        
                        # If the new word is in the wordSet, it's a valid transformation
                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.remove(newWord)  # Remove to prevent revisiting

            # Increment the step count after exploring all current possibilities
            steps += 1

        # If no transformation sequence is found, return 0
        return 0
