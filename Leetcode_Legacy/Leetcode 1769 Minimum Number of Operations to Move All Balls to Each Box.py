'''
Leetcode 1769 Minimum Number of Operations to Move All Balls to Each Box

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
Each answer[i] is calculated considering the initial state of the boxes.

Example 1:
        Input: boxes = "110"
        Output: [1,1,3]
        Explanation: The answer for each box is as follows:
        1) First box: you will have to move one ball from the second box to the first box in one operation.
        2) Second box: you will have to move one ball from the first box to the second box in one operation.
        3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

Example 2:
        Input: boxes = "001011"
        Output: [11,8,5,4,3,4]
 
Constraints:
        n == boxes.length
        1 <= n <= 2000
        boxes[i] is either '0' or '1'.

'''

from typing import List
import unittest

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Calculate the minimum number of operations to move all balls to each box.

        Parameters:
        - boxes (str): A string of '0's and '1's where '1' represents a ball and '0' represents an empty box.

        Returns:
        - List[int]: A list of integers where the ith value represents the minimum number of operations 
                     to move all balls to the ith box.
        """
        n = len(boxes)
        distances = [0] * n  # Result array to store minimum operations for each box

        # Left-to-right pass
        count = 0  # Number of balls encountered so far
        operations = 0  # Accumulated operations to move balls
        for i in range(n):
            distances[i] = operations
            if boxes[i] == '1':  # If the current box has a ball
                count += 1
            operations += count  # Add count to operations as we move to the next box

        # Right-to-left pass
        count = 0  # Reset number of balls encountered
        operations = 0  # Reset accumulated operations
        for i in range(n - 1, -1, -1):
            distances[i] += operations
            if boxes[i] == '1':  # If the current box has a ball
                count += 1
            operations += count  # Add count to operations as we move to the previous box

        return distances


# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        # Test case 1
        boxes = "110"
        expected = [1, 1, 3]
        self.assertEqual(self.solution.minOperations(boxes), expected)

        # Test case 2
        boxes = "001011"
        expected = [11, 8, 5, 4, 3, 4]
        self.assertEqual(self.solution.minOperations(boxes), expected)

        # Test case 3
        boxes = "0"
        expected = [0]
        self.assertEqual(self.solution.minOperations(boxes), expected)

        # Test case 4
        boxes = "111"
        expected = [3, 2, 3]
        self.assertEqual(self.solution.minOperations(boxes), expected)

if __name__ == "__main__":
    unittest.main()
