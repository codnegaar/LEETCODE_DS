'''
Leetcode 2416 Sum of Prefix Scores of Strings

        You are given an array words of size n consisting of non-empty strings.        
        We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].        
        For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
        Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].        
        Note that a string is considered as a prefix of itself. 

Example 1:
        Input: words = ["abc","ab","bc","b"]
        Output: [5,4,3,2]
        Explanation: The answer for each string is the following:
        - "abc" has 3 prefixes: "a", "ab", and "abc".
        - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
        The total is answer[0] = 2 + 2 + 1 = 5.
        - "ab" has 2 prefixes: "a" and "ab".
        - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
        The total is answer[1] = 2 + 2 = 4.
        - "bc" has 2 prefixes: "b" and "bc".
        - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
        The total is answer[2] = 2 + 1 = 3.
        - "b" has 1 prefix: "b".
        - There are 2 strings with the prefix "b".
        The total is answer[3] = 2.
        
Example 2:
        Input: words = ["abcd"]
        Output: [4]
        Explanation:
        "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
        Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4. 

Constraints:
        1 <= words.length <= 1000
        1 <= words[i].length <= 1000
        words[i] consists of lowercase English letters.
'''

class Node:
    def __init__(self):
        self.count = 0  # Number of words passing through this node
        self.children = [None] * 26  # Trie children for each letter 'a' to 'z'

    def containsKey(self, ch):
        return self.children[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.children[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.children[ord(ch) - ord('a')] = node

    def incrementCount(self):
        self.count += 1

    def getCount(self):
        return self.count


class Solution:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """Inserts a word into the Trie and updates prefix counts."""
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node.incrementCount()  # Increment count at the current node
            node = node.get(ch)
        node.incrementCount()  # Increment count at the last node

    def searchPrefixScore(self, word):
        """Calculates the prefix score for the given word."""
        node = self.root
        total_count = 0
        for ch in word:
            node = node.get(ch)
            total_count += node.getCount()
        return total_count

    def sumPrefixScores(self, words):
        """Returns a list of prefix scores for each word in the input list."""
        # First, build the Trie by inserting all words
        for word in words:
            self.insert(word)

        # Then, calculate the prefix score for each word
        result = []
        for word in words:
            result.append(self.searchPrefixScore(word))

        return result
