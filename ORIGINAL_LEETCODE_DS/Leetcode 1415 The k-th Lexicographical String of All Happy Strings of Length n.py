'''
Leetcode 1415 The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
        Input: n = 1, k = 3
        Output: "c"
        Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
        Input: n = 1, k = 4
        Output: ""
        Explanation: There are only 3 happy strings of length 1.

Example 3:
        Input: n = 3, k = 9
        Output: "cab"
        Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
         
Constraints:
        1 <= n <= 10
        1 <= k <= 100

'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generates the k-th lexicographically smallest happy string of length n.
        
        A happy string is a string consisting of letters 'a', 'b', and 'c' where:
        - No two adjacent characters are the same.
        - The strings are ordered lexicographically.

        Parameters:
        n (int): The length of the happy string.
        k (int): The k-th happy string to retrieve.

        Returns:
        str: The k-th happy string if it exists, otherwise an empty string.
        """
        alphabet = ('a', 'b', 'c')  # Allowed characters

        def backtrack(current: str):
            """
            Backtracking function to generate happy strings.
            
            Parameters:
            current (str): The current happy string being built.
            
            Yields:
            str: A valid happy string when it reaches length n.
            """
            if len(current) == n:
                yield current
            else:
                for ch in alphabet:
                    if not current or ch != current[-1]:  # Ensure no adjacent duplicate
                        yield from backtrack(current + ch)

        # Generate the k-th happy string
        for index, happy_string in enumerate(backtrack(''), start=1):
            if index == k:
              
                return happy_string

        return ""  # Return empty string if k-th happy string does not exist

# Example Usage
solution = Solution()

# Test cases
test_cases = [(3, 9), (3, 1), (2, 4), (3, 20)]

for n, k in test_cases:
    print(f"getHappyString({n}, {k}): {solution.getHappyString(n, k)}")
