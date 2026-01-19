'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution:
  def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and not s[l].isalnum():
        l += 1
      while l < r and not s[r].isalnum():
        r -= 1
      if s[l].lower() != s[r].lower():
        return False
      l += 1
      r -= 1

    return True


# second solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome, considering only alphanumeric characters
        and ignoring case sensitivity.

        Parameters:
        s (str): The input string.

        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        
        left, right = 0, len(s) - 1  # Initialize pointers at the start and end of the string

        while left < right:
            # Move left pointer until an alphanumeric character is found
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer until an alphanumeric character is found
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters, ignoring case
            if s[left].lower() != s[right].lower():
                return False  # Return False if characters don't match

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If all characters match, it's a palindrome
        return True

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
