'''
Leetcode 1750 Minimum Length of String After Deleting Similar Ends
  
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

        Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        The prefix and the suffix should not intersect at any index.
        The characters from the prefix and suffix must be the same.
        Delete both the prefix and the suffix.
        Return the minimum length of s after performing the above operation any number of times (possibly zero times).
        
Example 1:
        Input: s = "ca"
        Output: 2
        Explanation: You can't remove any characters, so the string stays as is.

Example 2:
        Input: s = "cabaabac"
        Output: 0
        Explanation: An optimal sequence of operations is:
        - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
        - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
        - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
        - Take prefix = "a" and suffix = "a" and remove them, s = "".
        
Example 3:
        Input: s = "aabccabba"
        Output: 3
        Explanation: An optimal sequence of operations is:
        - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
        - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
         

Constraints:
        1 <= s.length <= 105
        s only consists of characters 'a', 'b', and 'c'.

'''

class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        # Continue processing while the left pointer is less than the right pointer
        while left < right and s[left] == s[right]:
            # Store the current character to be removed
            current_char = s[left]
            
            # Increment the left pointer past all identical characters
            while left <= right and s[left] == current_char:
                left += 1
            
            # Decrement the right pointer past all identical characters
            while right >= left and s[right] == current_char:
                right -= 1
        
        # Calculate remaining length, account for the case when left > right
        return max(0, right - left + 1)
