'''

2466 Count Ways To Build Good Strings
 
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
        Append the character '0' zero times.
        Append the character '1' one time.
        This can be performed any number of times.
A good string is a string constructed by the above process having a length between low and high (inclusive).
Return the number of different good strings that can be constructed to satisfy these properties. Since the answer can be large, return it modulo 109 + 7.

 

Example 1:
        Input: low = 3, high = 3, zero = 1, one = 1
        Output: 8
        Explanation: 
        One possible valid good string is "011". 
        It can be constructed as follows: "" -> "0" -> "01" -> "011". 
        All binary strings from "000" to "111" are good strings in this example.
        
Example 2:
        Input: low = 2, high = 3, zero = 1, one = 2
        Output: 5
        Explanation: The good strings are "00", "11", "000", "110", and "011".
 
Constraints:
        1 <= low <= high <= 105
        1 <= zero, one <= low

'''
class Solution:
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    kMod = 1_000_000_007
    ans = 0
    # dp[i] := # of good strings with length i
    dp = [1] + [0] * high

    for i in range(1, high + 1):
      if i >= zero:
        dp[i] = (dp[i] + dp[i - zero]) % kMod
      if i >= one:
        dp[i] = (dp[i] + dp[i - one]) % kMod
      if i >= low:
        ans = (ans + dp[i]) % kMod

    return ans


# Second Solution
from functools import lru_cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Count the number of good strings of lengths between low and high inclusive,
        where a good string can be constructed using blocks of `zero` zeros or `one` ones.
        
        Args:
        low (int): The minimum length of a good string.
        high (int): The maximum length of a good string.
        zero (int): The block size of zeros allowed in the string.
        one (int): The block size of ones allowed in the string.

        Returns:
        int: The total count of good strings modulo 1,000,000,007.
        """
        MOD = 1_000_000_007  # Modulus for large numbers

        @lru_cache(None)  # Cache results of recursive calls
        def count(length: int) -> int:
            # Base case: A valid string of length 0 exists (empty string)
            if length == 0:
                return 1
            # Invalid case: Negative length means no valid strings
            if length < 0:
                return 0
            # Recursive case: Add ways to form string by reducing zero or one block
            return (count(length - zero) + count(length - one)) % MOD

        # Accumulate results for lengths in the range [low, high]
        result = 0
        for length in range(low, high + 1):
            result = (result + count(length)) % MOD
        return result


# Unit Test
def test_countGoodStrings():
    sol = Solution()
    # Test cases
    assert sol.countGoodStrings(3, 3, 1, 1) == 4, "Test Case 1 Failed"
    assert sol.countGoodStrings(2, 3, 1, 2) == 5, "Test Case 2 Failed"
    assert sol.countGoodStrings(5, 10, 2, 3) == 37, "Test Case 3 Failed"
    print("All test cases passed!")


# Example usage
if __name__ == "__main__":
    test_countGoodStrings()  # Run unit tests

    # Example outputs
    solution = Solution()
    print(solution.countGoodStrings(3, 3, 1, 1))  # Output: 4
    print(solution.countGoodStrings(5, 10, 2, 3))  # Output: 37
