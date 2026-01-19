'''

Leetcode 2559 Count Vowel Strings in Ranges
 
You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
        Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
        Output: [2,3,0]
        Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
        The answer to the query [0,2] is 2 (strings "aba" and "ece").
        to query [1,4] is 3 (strings "ece", "aa", "e").
        to query [1,1] is 0.
        We return [2,3,0].

Example 2:
        Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
        Output: [3,2,1]
        Explanation: Every string satisfies the conditions, so we return [3,2,1].
         
Constraints:
        1 <= words.length <= 105
        1 <= words[i].length <= 40
        words[i] consists only of lowercase English letters.
        sum(words[i].length) <= 3 * 105
        1 <= queries.length <= 105
        0 <= li <= ri < words.length
'''
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Counts words that start and end with vowels within the given query ranges.

        Args:
        words (List[str]): List of words to process.
        queries (List[List[int]]): List of queries, where each query is [start, end].

        Returns:
        List[int]: List of counts of vowel-starting and vowel-ending words for each query.
        """
        n = len(words)  # Number of words
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels for quick lookup
        prefix = [0] * (n + 1)  # Prefix sum array, initialized to 0

        # Build prefix sum array
        for i in range(n):
            prefix[i + 1] = prefix[i]
            # Increment prefix if the word starts and ends with a vowel
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        # Answer each query
        result = []
        for start, end in queries:
            # Calculate the count in the range [start, end] using prefix sums
            result.append(prefix[end + 1] - prefix[start])

        return result


