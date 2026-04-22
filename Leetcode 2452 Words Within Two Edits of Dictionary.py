'''
Leetcode 2452 Words Within Two Edits of Dictionary

You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.
In one edit, you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from the dictionary.
Return a list of all words from queries that match some word from the dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

Example 1:
        Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
        Output: ["word","note","wood"]
        Explanation:
        - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
        - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
        - It would take more than 2 edits for "ants" to equal a dictionary word.
        - "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
        Thus, we return ["word","note","wood"].

Example 2:
        Input: queries = ["yes"], dictionary = ["not"]
        Output: []
        Explanation:
        Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
         
Constraints:
        1 <= queries.length, dictionary.length <= 100
        n == queries[i].length == dictionary[j].length
        1 <= n <= 100
        All queries[i] and dictionary[j] are composed of lowercase English letters.
'''

import numpy as np

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # All words have the same length N
        N = len(queries[0])
        
        # Convert to integer matrices: Shape (Q, N) and (D, N)
        q_vec = np.array([[ord(c) for c in w] for w in queries], dtype=np.int8)
        d_vec = np.array([[ord(c) for c in w] for w in dictionary], dtype=np.int8)
        
        results = []
        
        # We broadcast each query vector against the entire dictionary field
        # q_vec[i, None] has shape (1, N)
        # d_vec has shape (D, N)
        # Difference has shape (D, N)
        for i in range(len(queries)):
            # Displacement vectors from query[i] to all dictionary words
            diff = q_vec[i] != d_vec
            
            # Count the '1's (edits) across the word length (axis 1)
            edit_counts = np.sum(diff, axis=1)
            
            # If any dictionary word is within 2 edits
            if np.any(edit_counts <= 2):
                results.append(queries[i])
                
        return results        
