'''
Leetcode 2109 Adding Spaces to a String
 
You are given a 0-indexed string s and a 0-indexed integer array of spaces that describes the indices in the original string where spaces will be added. 
Each space should be inserted before the character at the given index.
For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively.
Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added. 

Example 1:
        Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
        Output: "Leetcode Helps Me Learn"
        Explanation: 
        The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
        We then place spaces before those characters.

Example 2:
        Input: s = "icodeinpython", spaces = [1,5,7,9]
        Output: "i code in py thon"
        Explanation:
        The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
        We then place spaces before those characters.

Example 3:
        Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
        Output: " s p a c i n g"
        Explanation:
        We are also able to place spaces before the first character of the string.
 
Constraints:
        1 <= s.length <= 3 * 105
        s consists only of lowercase and uppercase English letters.
        1 <= spaces.length <= 3 * 105
        0 <= spaces[i] <= s.length - 1
        All the values of spaces are strictly increasing.

'''

from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        Adds spaces to a string at specific positions defined in the spaces list.
        
        Parameters:
        s (str): The input string without any spaces.
        spaces (List[int]): A list of positions where spaces should be added.
        
        Returns:
        str: The resulting string after adding spaces.
        """
        # List to hold characters of the final result
        result = []

        # Pointer to track the current space to be added
        space_index = 0

        # Iterate over each character in the input string
        for i in range(len(s)):
            # Add a space if the current index matches the next space position
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')  # Add the space
                space_index += 1  # Move to the next space in the list

            # Add the current character from the string
            result.append(s[i])

        # Join all characters into the final string
        return "".join(result)

# Example of usage
if __name__ == "__main__":
    solution = Solution()
    s = "helloworld"
    spaces = [5]
    print(solution.addSpaces(s, spaces))  # Expected output: "hello world"

# Unit test to verify the correctness of the solution
import unittest

class TestAddSpaces(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "helloworld"
        spaces = [5]
        expected = "hello world"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)
        
    def test_example_2(self):
        s = "leetcodeiscool"
        spaces = [8, 10]
        expected = "leetcode is cool"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)
        
    def test_example_3(self):
        s = "abc"
        spaces = [1, 2]
        expected = "a b c"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)
        
    def test_empty_string(self):
        s = ""
        spaces = []
        expected = ""
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)
        
    def test_no_spaces(self):
        s = "test"
        spaces = []
        expected = "test"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
