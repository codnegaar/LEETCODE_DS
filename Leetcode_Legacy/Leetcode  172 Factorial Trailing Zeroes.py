'''

Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
        Input: n = 3
        Output: 0
        Explanation: 3! = 6, no trailing zero.
        
Example 2:
        Input: n = 5
        Output: 1
        Explanation: 5! = 120, one trailing zero.
        
Example 3:
        Input: n = 0
        Output: 0

Constraints:
        0 <= n <= 104

'''

class Solution:
  def trailingZeroes(self, n: int) -> int:
    return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


# Secon solution
class Solution:
    """
    A solution to calculate the number of trailing zeroes in the factorial of a given number.

    Methods
    -------
    trailingZeroes(n: int) -> int:
        Recursively calculates the number of trailing zeroes in n!.
    """
    def trailingZeroes(self, n: int) -> int:
        """
        Calculates the number of trailing zeroes in the factorial of n.
        Trailing zeroes are caused by factors of 10, which result from multiplying 2 and 5.
        Since there are usually more factors of 2 than 5 in factorials, we only count the factors of 5.

        Parameters
        ----------
        n : int
            A non-negative integer representing the number for which factorial is calculated.

        Returns
        -------
        int
            The number of trailing zeroes in n!.
        """
        # Base case: if n is 0, there are no trailing zeroes
        if n == 0:
            return 0
        
        # Recursive step: count the number of factors of 5 in n and recursively process n // 5
        return n // 5 + self.trailingZeroes(n // 5)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_n = 100
    print(f"Number of trailing zeroes in {example_n}!: {solution.trailingZeroes(example_n)}")
