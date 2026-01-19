'''

Leetcode 150-string-Array 55 Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array
represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.


Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
     Input: nums = [3,2,1,0,4]
     Output: false
     Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
      
Constraints:
     1 <= nums.length <= 104
     0 <= nums[i] <= 105

'''

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    i = 0
    reach = 0

    while i < len(nums) and i <= reach:
      reach = max(reach, i + nums[i])
      i += 1

    return i == len(nums)


# Second solution

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        indx = 0
        for n in nums:
            if indx < 0:
                return False
            elif n > indx:
                indx = n
            indx -= 1
            
        return True


# 2nd solution
from typing import List
import operator
import unittest

class Solution:
    """
    Evaluate Reverse Polish Notation (RPN) expressions.

    Args:
        tokens (List[str]): List of tokens representing the RPN expression.

    Returns:
        int: The evaluated result of the RPN expression.
    """
    def evalRPN(self, tokens: List[str]) -> int:
        # Mapping operators to their respective functions for simplicity
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),  # Ensures truncation towards zero
        }
        stack = []  # Stack to keep operands during evaluation

        for token in tokens:
            if token in ops:  # If the token is an operator
                b = stack.pop()  # Pop the second operand
                a = stack.pop()  # Pop the first operand
                # Apply the operator function and push the result
                stack.append(ops[token](a, b))
            else:
                # If the token is a number, convert it to integer and push to stack
                stack.append(int(token))

        # The last remaining item in the stack is the result
        return stack[0]


# Unit Testing
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evalRPN(self):
        # Example cases
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(self.solution.evalRPN(["10", "6", "9", "3", "/", "-", "+"]), 5)
        # Case with negative numbers
        self.assertEqual(self.solution.evalRPN(["-10", "3", "/"]), -3)
        # Single operand
        self.assertEqual(self.solution.evalRPN(["42"]), 42)

# Main execution for tests and examples
if __name__ == "__main__":
    import sys
    # Prevent unittest from parsing additional CLI arguments
    sys.argv = [sys.argv[0]]
    # Run unit tests
    unittest.main(exit=False)

    # Example usage
    example_tokens = ["2", "1", "+", "3", "*"]
    solution = Solution()
    result = solution.evalRPN(example_tokens)
    print(f"Result of {example_tokens}: {result}")  # Output: 9

