'''
131 Palindrome Partitioning
 
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    ans = []

    def isPalindrome(s: str) -> bool:
      return s == s[::-1]

    def dfs(s: str, j: int, path: List[str], ans: List[List[str]]) -> None:
      if j == len(s):
        ans.append(path)
        return

      for i in range(j, len(s)):
        if isPalindrome(s[j: i + 1]):
          dfs(s, i + 1, path + [s[j: i + 1]], ans)

    dfs(s, 0, [], ans)
    return ans


#second solution
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Finds all possible palindrome partitions of a given string.

        Parameters:
        -----------
        s : str
            The input string to partition.

        Returns:
        --------
        List[List[str]]
            A list containing all possible partitions where each substring is a palindrome.
        """
        result = []  # Stores all valid palindrome partitions

        def is_palindrome(sub: str) -> bool:
            """
            Checks if a given substring is a palindrome.

            Parameters:
            -----------
            sub : str
                The substring to check.

            Returns:
            --------
            bool
                True if the substring is a palindrome, otherwise False.
            """
            return sub == sub[::-1]

        def backtrack(start: int, path: List[str]) -> None:
            """
            Backtracking function to generate all valid partitions.

            Parameters:
            -----------
            start : int
                Current start index in the string.
            path : List[str]
                Current list of palindrome substrings.
            """
            if start == len(s):  # If we've processed the whole string
                result.append(path[:])  # Store a copy of the current partition
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):  # Check if it's a palindrome
                    path.append(substring)  # Choose the substring
                    backtrack(end, path)  # Explore further partitions
                    path.pop()  # Undo the last choice (backtrack)

        backtrack(0, [])
        return result

# Example Usage
solution = Solution()

# Test cases
test_cases = ["aab", "civic", "aaa", "abc"]

for s in test_cases:
    print(f"Palindrome partitions of '{s}': {solution.partition(s)}")
