'''
Leetcode (Array-String) 1768 Merge Strings Alternately 

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string. Return the merged string.

 Example 1:
          Input: word1 = "abc", word2 = "pqr"
          Output: "apbqcr"
          Explanation: The merged string will be merged as so:
          word1:  a   b   c
          word2:    p   q   r
          merged: a p b q c r
          
Example 2:
        Input: word1 = "ab", word2 = "pqrs"
        Output: "apbqrs"
        Explanation: Notice that as word2 is longer, "rs" is appended to the end.
        word1:  a   b 
        word2:    p   q   r   s
        merged: a p b q   r   s
        
Example 3:
        Input: word1 = "abcd", word2 = "pq"
        Output: "apbqcd"
        Explanation: Notice that as word1 is longer, "cd" is appended to the end.
        word1:  a   b   c   d
        word2:    p   q 
        merged: a p b q c   d
 
Constraints:
        1 <= word1.length, word2.length <= 100
        word1 and word2 consist of lowercase English letters.
'''

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    '''

    property ma.masked_array.fill_value
    The filling value of the masked array is a scalar. When 
    setting, None will set to a default based on the data type.
    '''

    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))


# Second solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately, taking one character from each string at a time.
        When one string runs out of characters, append the remaining characters of the other string.
        
        Parameters:
        word1 (str): The first input string.
        word2 (str): The second input string.
        
        Returns:
        str: The merged string, with characters taken alternately from word1 and word2.
        
        Time Complexity: O(n), where n = len(word1) + len(word2).
        """

        # Initialize pointers for both strings and an empty list for the result
        a, b = 0, 0
        merged = []

        # Alternate appending characters from each string until one is exhausted
        while a < len(word1) and b < len(word2):
            merged.append(word1[a])
            a += 1
            merged.append(word2[b])
            b += 1

        # Append any remaining characters from word1 or word2
        merged.extend(word1[a:])
        merged.extend(word2[b:])

        # Join the list into a single string and return it
        return ''.join(merged)
