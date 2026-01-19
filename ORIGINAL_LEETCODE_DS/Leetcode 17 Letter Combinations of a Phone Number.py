'''
Leetcode 17 Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
     Input: digits = "23"
     Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
 
Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

       
       
# second solution:

class Solution(object):
    def letterCombinations(self, digits):
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(digits, d, l, cur, ans):
            
            if l == len(digits):
                if l > 0:
                    ans.append("".join(cur))
                    
                return
        
            for c in d[ord(digits[l]) - ord('0')]:
                cur[l] = c
                dfs(digits, d, l + 1, cur, ans)
        
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
        cur = [' ' for _ in range(len(digits))]
        ans = []
        dfs(digits, d, 0, cur, ans)
        return ans


# 3rd solution

from typing import List
from itertools import product
import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string of digits from 2 to 9, return all possible letter combinations
        that the digits could represent on a traditional phone keypad.
        
        Parameters:
        digits (str): A string containing digits from 2 to 9.

        Returns:
        List[str]: A list of all possible letter combinations.
        """
        # Return an empty list if no digits are provided
        if not digits:
            return []
        
        # Mapping of digits to letters, following a traditional phone keypad
        phone = {
            "2": "abc", "3": "def", "4": "ghi", 
            "5": "jkl", "6": "mno", "7": "pqrs", 
            "8": "tuv", "9": "wxyz"
        }

        # Generate all combinations using itertools.product
        letters = [phone[digit] for digit in digits]
        return [''.join(comb) for comb in product(*letters)]

# Unit test to validate the solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_letter_combinations(self):
        # Test with single digit
        self.assertEqual(self.solution.letterCombinations("2"), ["a", "b", "c"])
        
        # Test with multiple digits
        self.assertEqual(
            sorted(self.solution.letterCombinations("23")),
            sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        )
        
        # Test with no input
        self.assertEqual(self.solution.letterCombinations(""), [])
        
        # Test with maximum input
        self.assertTrue(len(self.solution.letterCombinations("234")) > 0)

# Example usage and testing
if __name__ == "__main__":
    # Example
    print(Solution().letterCombinations("23"))  # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    # Run unit tests
    unittest.main(argv=[''], exit=False)

# 3rd solution
from typing import List

class Solution:
    """
    Solution for generating all possible letter combinations 
    from a given digit string based on a phone keypad mapping.
    """

    def __init__(self):
        # Mapping of digits to corresponding letters based on a phone keypad
        self.comb = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations for a given digit string.

        :param digits: A string containing digits (2-9)
        :return: A list of all possible letter combinations
        """
        if not digits:
            return []

        ans = []
        self._backtrack(0, digits, "", ans)
        return ans

    def _backtrack(self, index: int, digits: str, current_comb: str, ans: List[str]):
        """
        A recursive backtracking function to generate letter combinations.

        :param index: The current index in the digit string
        :param digits: The input digit string
        :param current_comb: The combination built so far
        :param ans: The list storing all valid letter combinations
        """
        # Base case: If we have processed all digits, add the combination to results
        if index == len(digits):
            ans.append(current_comb)
            return

        # Get the corresponding letters for the current digit
        for char in self.comb[int(digits[index])]:
            self._backtrack(index + 1, digits, current_comb + char, ans)


# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(f"Letter Combinations for '{digits}': {result}")
