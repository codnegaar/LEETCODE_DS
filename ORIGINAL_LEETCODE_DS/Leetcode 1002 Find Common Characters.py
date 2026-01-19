'''

Leetcode 1002 Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
        Input: words = ["bella","label","roller"]
        Output: ["e","l","l"]
        
Example 2:
        Input: words = ["cool","lock","cook"]
        Output: ["c","o"]
 
Constraints:
        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of lowercase English letters.

'''

from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Initialize the counter with the first word's character counts
        common_count = Counter(words[0])
        
        # Update the counter with the intersection of counts from the subsequent words
        for word in words[1:]:
            word_count = Counter(word)
            common_count &= word_count

        # Expand the elements in the counter to form the result list
        res = []
        for char, count in common_count.items():
            res.extend([char] * count)

        return res
