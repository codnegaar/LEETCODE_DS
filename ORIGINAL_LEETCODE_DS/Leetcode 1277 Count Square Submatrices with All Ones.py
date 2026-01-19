'''

Leetcode 1277 Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
Example 1:
        Input: matrix =
                        [
                          [0,1,1,1],
                          [1,1,1,1],
                          [0,1,1,1]
                        ]
        Output: 15
        Explanation: 
        There are 10 squares of side 1.
        There are 4 squares of side 2.
        There is  1 square of side 3.
        Total number of squares = 10 + 4 + 1 = 15.

Example 2:        
        Input: matrix = 
                        [
                          [1,0,1],
                          [1,1,0],
                          [1,1,0]
                        ]
        Output: 7
        Explanation: 
        There are 6 squares of side 1.  
        There is 1 square of side 2. 
        Total number of squares = 6 + 1 = 7.
 

Constraints:
        1 <= arr.length <= 300
        1 <= arr[0].length <= 300
        0 <= arr[i][j] <= 1
'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Function to count the total number of square submatrices with all ones.
        
        Parameters:
        matrix (List[List[int]]): A 2D list representing the binary matrix where each element is either 0 or 1.
        
        Returns:
        int: The total number of square submatrices with all ones.
        """
        n, m = len(matrix), len(matrix[0])
        # Initialize the answer with the sum of the first row elements.
        total_squares = sum(matrix[0])
        
        # Iterate over each row starting from the second row.
        for i in range(1, n):
            # Add the first element of each row to the total count.
            total_squares += matrix[i][0]
            for j in range(1, m):
                # If the current element is 1, update it to reflect the size of the largest square ending at that position.
                if matrix[i][j]:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    # Add the value of the current cell to the total count of squares.
                    total_squares += matrix[i][j]
        
        return total_squares

