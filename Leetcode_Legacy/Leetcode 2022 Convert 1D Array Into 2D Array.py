'''
Leetcode 2022 Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked
with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from the original.
The elements from indices 0 to n - 1 (inclusive) of the original should form the first row of the constructed 2D array,
and the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible. 

Example 1:
        Input: original = [1,2,3,4], m = 2, n = 2
        Output: [[1,2],[3,4]]
        Explanation: The constructed 2D array should contain 2 rows and 2 columns.
        The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
        The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

Example 2:        
        Input: original = [1,2,3], m = 1, n = 3
        Output: [[1,2,3]]
        Explanation: The constructed 2D array should contain 1 row and 3 columns.
        Put all three elements in original into the first row of the constructed 2D array.

Example 3:
        Input: original = [1,2], m = 1, n = 1
        Output: []
        Explanation: There are 2 elements in original.
        It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array. 

Constraints:
        1 <= original.length <= 5 * 104
        1 <= original[i] <= 105
        1 <= m, n <= 4 * 104
'''
class Solution:
    def construct2DArray(self, original, m, n):
        # Check if the total number of elements matches the required 2D array dimensions
        if m * n != len(original):
            return []
        # Construct the 2D array by slicing the original list into sublists of length n
        return [original[i * n:(i + 1) * n] for i in range(m)]

def format_output(result):
    # Convert the 2D array into a string format suitable for output, removing spaces and formatting brackets
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def kdsmain():
    input_data = sys.stdin.read().strip().splitlines()  # Read all input lines from standard input
    
    results = []
    for i in range(0, len(input_data), 3):
        # Parse the original list and dimensions (m, n) from the input
        original = json.loads(input_data[i])
        m, n = int(input_data[i + 1]), int(input_data[i + 2])
        
        # Construct the 2D array using the Solution class
        result = Solution().construct2DArray(original, m, n)
        # Format the result for output
        results.append(format_output(result))
    
    # Write the formatted results to 'user.out' file, each result on a new line
    with open('user.out', 'w') as f:
        f.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    kdsmain()  # Run the main function
    exit(0)    # Exit the program
