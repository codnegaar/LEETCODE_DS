'''
Leetcode 1593 Split a String Into the Max Number of Unique Substrings

Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.

Example 1:
        Input: s = "ababccc"
        Output: 5
        Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:
        Input: s = "aba"
        Output: 2
        Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
        Input: s = "aa"
        Output: 1
        Explanation: It is impossible to split the string any further.
         
Constraints:
        1 <= s.length <= 16
        s contains only lower case English letters.

'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        This function finds the maximum number of unique splits that can be made from the input string.

        @param self: Represents the instance of the class Solution.
        @param s: The input string that needs to be split into unique substrings.
        @return: Maximum number of unique splits of the input string.
        """
        
        def backtrack(start: int, seen: set) -> int:
            """
            A helper function that recursively finds the maximum number of unique splits.

            @param start: The current starting index from which to split the string.
            @param seen: A set containing all unique substrings seen so far.
            @return: The maximum number of unique splits from the current start index.
            """
            # If we have reached the end of the string, there are no more splits possible.
            if start == len(s):
                return 0

            # Variable to track the maximum number of unique splits.
            max_splits = 0

            # Iterate from the current start to the end of the string to find substrings.
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]  # Generate the substring from start to end index.
                
                # If this substring has not been seen before, we attempt to use it.
                if substring not in seen:
                    seen.add(substring)  # Add the substring to the set of seen substrings.
                    # Recursively call backtrack to continue splitting from the current end index.
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    seen.remove(substring)  # Remove the substring to backtrack and try other options.
            
            return max_splits
        
        # Start the backtracking process from index 0 with an empty set for unique substrings.
        return backtrack(0, set())

# Example usage:
# sol = Solution()
# result = sol.maxUniqueSplit("ababccc")
# print(result)  # Output: 5
