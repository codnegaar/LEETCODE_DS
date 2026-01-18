'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
Example 2:
        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]

Constraints:
        1 <= s.length <= 105
        s[i] is a printable ascii character.

'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # recursive function
        def reverse(l,r):
            if l<r:
                s[l],s[r] = s[r],s[l]
                reverse(l+1 , r-1)
        reverse(0, len(s)-1)
                
        
        #using stack
        stack =[]
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i]= stack.pop()
            i += 1
        
        
  
       # Easy solution
        l,r =0, len(s) -1
        
        while l<r:
            s[l],s[r] = s[r],s[l]
            l , r = l+1, r -1 


# Second solution

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the given list of characters in-place.
        
        Args:
        s (List[str]): List of characters to be reversed.
        
        Returns:
        None: The input list is modified in-place.
        """
        # Initialize two pointers: one at the beginning (left) and one at the end (right)
        left, right = 0, len(s) - 1
        
        # Continue swapping elements while left pointer is less than the right pointer
        while left < right:
            # Swap the characters at positions left and right
            s[left], s[right] = s[right], s[left]
            # Move the left pointer one step to the right
            left += 1
            # Move the right pointer one step to the left
            right -= 1

# Unit tests
if __name__ == "__main__":
    # Helper function for testing
    def test_case(input_list, expected_output):
        Solution().reverseString(input_list)
        assert input_list == expected_output, f"Failed for input {input_list}"
    
    # Example test cases
    test_case(['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h'])  # Reverse "hello"
    test_case(['H', 'a', 'n', 'n', 'a', 'h'], ['h', 'a', 'n', 'n', 'a', 'H'])  # Reverse "Hannah"
    test_case([], [])  # Empty list
    test_case(['a'], ['a'])  # Single character
    test_case(['a', 'b'], ['b', 'a'])  # Two characters

    print("All test cases passed!")
