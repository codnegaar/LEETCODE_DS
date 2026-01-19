'''
Leetcode 1267 Count Servers that Communicate

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Example 1:
        Input: grid = [[1,0],[0,1]]
        Output: 0
        Explanation: No servers can communicate with others.

Example 2:
        Input: grid = [[1,0],[1,1]]
        Output: 3
        Explanation: All three servers can communicate with at least one other server.

Example 3:
        Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
        Output: 4
        Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m <= 250
        1 <= n <= 250
        grid[i][j] == 0 or 1
'''
class Solution:
    """
    A class to count the number of servers that can communicate with at least one other server.
    """

    def countServers(self, grid):
        """
        Count the number of servers that can communicate with at least one other server.

        :param grid: List[List[int]] - 2D grid where 1 represents a server and 0 represents empty space
        :return: int - Count of communicating servers
        """

        # Grid dimensions
        rows, cols = len(grid), len(grid[0])

        # Count of servers in each row and column
        row_count = [0] * rows
        col_count = [0] * cols

        # First pass: Count the number of servers in rows and columns
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Second pass: Count servers that can communicate
        total_communicating = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # A server can communicate if its row or column has more than one server
                    if row_count[i] > 1 or col_count[j] > 1:
                        total_communicating += 1

        return total_communicating


# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test Example 1
    grid1 = [
        [1, 0],
        [0, 1]
    ]
    print("Communicating servers in grid1:", solution.countServers(grid1))  # Output: 0

    # Test Example 2
    grid2 = [
        [1, 0],
        [1, 1]
    ]
    print("Communicating servers in grid2:", solution.countServers(grid2))  # Output: 3

    # Test Example 3
    grid3 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    print("Communicating servers in grid3:", solution.countServers(grid3))  # Output: 4


# Unit Tests
def test_count_servers():
    solution = Solution()

    assert solution.countServers([[0, 0], [0, 0]]) == 0, "Test Case 1 Failed"
    assert solution.countServers([[1, 0], [0, 1]]) == 0, "Test Case 2 Failed"
    assert solution.countServers([[1, 0], [1, 1]]) == 3, "Test Case 3 Failed"
    assert solution.countServers([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 4, "Test Case 4 Failed"
    assert solution.countServers([[1]]) == 0, "Test Case 5 Failed"
    assert solution.countServers([[1, 1], [0, 1]]) == 3, "Test Case 6 Failed"

    print("All unit tests passed!")


# Run Unit Tests
test_count_servers()

"""
Improvements and Changes:
1. Removed `object` from class declaration to comply with modern Python 3 standards.
2. Improved variable naming for clarity (`rows`, `cols`, `total_communicating`).
3. Added proper docstrings for class and methods for better documentation.
4. Kept the algorithm efficient with O(m * n) complexity (optimal for this problem).
5. Added example usage with meaningful test cases.
6. Included unit tests with descriptive failure messages to ensure functionality.

Python Documentation Reference:
- https://docs.python.org/3/tutorial/classes.html
"""


