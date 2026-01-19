'''

279 Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
perfect squares while 3 and 11 are not.

 
Example 1:
        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        
Example 2:
        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9. 

Constraints:
        1 <= n <= 104

'''
class Solution:
  def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
      j = 1
      while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

    return dp[n]


# Second solution
class Solution:
    """
    Solution to the 'Perfect Squares' problem.
    
    Given an integer n, return the least number of perfect square numbers 
    (like 1, 4, 9, 16, ...) which sum to n.
    """

    def numSquares(self, n: int) -> int:
        """
        Calculates the minimum number of perfect squares that sum up to `n`.

        Parameters:
        -----------
        n : int
            The target number.

        Returns:
        --------
        int
            The minimum number of perfect square numbers that sum to `n`.

        Time Complexity: O(n * sqrt(n))
        Space Complexity: O(n)
        """

        # Initialize DP array where dp[i] = minimum number of perfect squares summing to i
        dp = [n] * (n + 1)  # Worst case: all 1^2 (so we need at most n 1's)
        dp[0] = 0           # Base case: 0 requires 0 numbers

        # Fill dp array from 1 to n
        for i in range(1, n + 1):
            j = 1
            # Try all perfect squares <= i
            while j * j <= i:
                square = j * j
                dp[i] = min(dp[i], dp[i - square] + 1)
                j += 1

        return dp[n]

