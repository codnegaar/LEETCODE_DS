'''
Leetcode 118 Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
	Input: numRows = 5
	Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
	Input: numRows = 1
	Output: [[1]]

Constraints:
	1 <= numRows <= 30

'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range (numRows -1):
            temp = [0] + res[-1] +[0]
            row = []
            for j in range (len(res[-1]) +1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res


# Second solution
from typing import List

class Solution:
    """
    Solution class to generate Pascal's Triangle up to a given number of rows.
    """
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates Pascal's Triangle up to numRows.

        :param numRows: Number of rows to generate.
        :return: A list of lists representing Pascal's Triangle.
        """
        if numRows <= 0:
            return []  # Edge case: No rows to generate

        res = [[1]]  # Initialize with the first row

        for i in range(1, numRows):  # Start from second row (index 1)
            prev_row = res[-1]  # Get the previous row
            row = [1]  # First element is always 1

            # Compute middle elements by summing adjacent elements from the previous row
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # Last element is always 1
            res.append(row)  # Add the new row to the result

        return res

# second solution

from typing import List

class Solution:
    """
    Class to generate Pascal's Triangle up to a specified number of rows.
    """

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates the first numRows of Pascal's Triangle.

        Parameters:
        numRows (int): Number of rows of Pascal's Triangle to generate.

        Returns:
        List[List[int]]: A list of lists representing the triangle.
        """
        if numRows <= 0:
            return []

        result = [[1]]  # First row is always [1]

        for _ in range(1, numRows):
            prev_row = result[-1]
            # Pad with 0s on both sides to simplify addition of adjacent elements
            padded = [0] + prev_row + [0]
            # Generate the next row using element-wise sum of adjacent pairs
            next_row = [padded[i] + padded[i + 1] for i in range(len(prev_row) + 1)]
            result.append(next_row)

        return result


# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    triangle = sol.generate(5)
    for row in triangle:
        print(row)

# ✅ Unit tests
def test_generate():
    sol = Solution()

    # Basic test cases
    assert sol.generate(0) == []
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]
    assert sol.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert sol.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    print("All tests passed!")

test_generate()

"""
Summary of Improvements:
- ✅ Cleaned and simplified logic using list comprehension for next row generation.
- ✅ Added docstring for the class and method.
- ✅ Improved inline comments for better clarity.
- ✅ Followed PEP 8 style guide for formatting.
- ✅ Included example usage and test cases using assertions.
- ✅ Time complexity is O(n^2), which is optimal for Pascal's Triangle generation.
- ✅ Used type hints for clarity and modern Python style.

Relevant Python Docs:
- List Comprehension: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- Typing: https://docs.python.org/3/library/typing.html
"""

