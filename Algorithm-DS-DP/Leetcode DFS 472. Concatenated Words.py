'''
Leetcode DFS 472. Concatenated Words

Given an array of string words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array. 

Example 1:
        Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
        Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
        "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
        "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
        
Example 2:
        Input: words = ["cat","dog","catdog"]
        Output: ["catdog"] 

Constraints:
        1 <= words.length <= 104
        1 <= words[i].length <= 30
        words[i] consists of only lowercase English letters.
        All the strings of words are unique.
        1 <= sum(words[i].length) <= 105

'''

class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wordSet = set(words)

    @functools.lru_cache(None)
    def isConcat(word: str) -> bool:
      for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
          return True

      return False

    return [word for word in words if isConcat(word)]



