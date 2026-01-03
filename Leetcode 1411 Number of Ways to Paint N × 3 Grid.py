'''

Leetcode 1411 Number of Ways to Paint N × 3 Grid

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.


Example 1:
        Input: n = 1
        Output: 12
        Explanation: There are 12 possible way to paint the grid as shown.

Example 2:
        Input: n = 5000
        Output: 30228214 

Constraints:
        n == grid.length
        1 <= n <= 5000

'''
from typing import Tuple

MOD = 10**9 + 7

def step(a: int, b: int) -> Tuple[int, int]:
    """Advance one row: a=ABA count, b=ABC count."""
    na = (3 * a + 2 * b) % MOD
    nb = (2 * a + 2 * b) % MOD
    return na, nb

class Solution:
    def numOfWays(self, n: int) -> int:
        a = b = 6  # row 1: ABA=6, ABC=6
        for _ in range(1, n):
            a, b = step(a, b)
        return (a + b) % MOD
