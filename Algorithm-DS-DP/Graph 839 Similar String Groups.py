'''
Graph 839 Similar String Groups

Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.
For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:
        Input: strs = ["tars","rats","arts","star"]
        Output: 2

Example 2:
        Input: strs = ["omv","ovm"]
        Output: 1 

Constraints:
        1 <= strs.length <= 300
        1 <= strs[i].length <= 300
        strs[i] consists of lowercase letters only.
        All words in strs have the same length and are anagrams of each other.

'''

from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        """
        Find the number of similar groups among a list of strings.
        
        Parameters:
        strs (List[str]): A list of strings containing only lowercase English letters.

        Returns:
        int: The number of groups where each group contains similar strings.
        """
        n = len(strs)
        visited = [False] * n
        groups = 0

        # Loop through each string and use DFS if the string hasn't been visited
        for i in range(n):
            if not visited[i]:
                groups += 1
                self.iterative_dfs(i, strs, visited)

        return groups

    def iterative_dfs(self, index: int, strs: List[str], visited: List[bool]) -> None:
        """
        Perform iterative DFS to mark all strings that are in the same group.

        Parameters:
        index (int): Index of the starting string.
        strs (List[str]): List of all strings.
        visited (List[bool]): List tracking visited strings.
        """
        stack = [index]
        visited[index] = True

        while stack:
            current = stack.pop()

            # Check all other strings to see if they're similar
            for j in range(len(strs)):
                if not visited[j] and self.is_similar(strs[current], strs[j]):
                    visited[j] = True
                    stack.append(j)

    def is_similar(self, a: str, b: str) -> bool:
        """
        Check if two strings are similar. Two strings are similar if they are identical
        or if exactly two characters differ.

        Parameters:
        a (str): First string.
        b (str): Second string.

        Returns:
        bool: True if strings are similar, False otherwise.
        """
        # A quick check: if more than 2 characters differ, they're not similar
        diff_count = sum(1 for x, y in zip(a, b) if x != y)
        return diff_count == 2 or diff_count == 0



