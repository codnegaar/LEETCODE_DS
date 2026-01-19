'''
Leetcode 1931 Painting a Grid With Three Different Colors

You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7. 

Example 1:
        Input: m = 1, n = 1
        Output: 3
        Explanation: The three possible colorings are shown in the image above.

Example 2:        
        Input: m = 1, n = 2
        Output: 6
        Explanation: The six possible colorings are shown in the image above.
        
Example 3:

        Input: m = 5, n = 5
        Output: 580986         

Constraints:
        1 <= m <= 5
        1 <= n <= 1000
'''
from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Counts the number of ways to color an m x n grid such that:
        - Each cell is painted with one of 3 colors (0, 1, 2)
        - No two adjacent cells in the same row or column have the same color

        Parameters:
        m (int): number of rows
        n (int): number of columns

        Returns:
        int: total number of valid colorings modulo 10^9 + 7
        """
        MOD = 10**9 + 7

        # Generate all valid color combinations for one column using DFS
        def generate_column_states():
            states = []

            @lru_cache(None)
            def dfs(pos: int, prev_color: int, mask: int):
                if pos == m:
                    states.append(mask)
                    return
                for color in range(3):
                    if color != prev_color:
                        dfs(pos + 1, color, mask * 3 + color)

            dfs(0, -1, 0)
            return states

        # Decode a column mask into list of colors
        def decode(mask: int) -> list:
            colors = []
            for _ in range(m):
                colors.append(mask % 3)
                mask //= 3
            return colors[::-1]

        # Check compatibility between two column colorings
        def are_compatible(mask1: int, mask2: int) -> bool:
            for c1, c2 in zip(decode(mask1), decode(mask2)):
                if c1 == c2:
                    return False
            return True

        # Step 1: Generate all valid column colorings
        states = generate_column_states()
        S = len(states)

        # Step 2: Build compatibility map between column states
        compat = [[] for _ in range(S)]
        for i in range(S):
            for j in range(S):
                if are_compatible(states[i], states[j]):
                    compat[i].append(j)

        # Step 3: Dynamic programming over columns
        dp = [1] * S  # Initialize: 1 way to paint the first column with each valid coloring
        for _ in range(n - 1):  # Process each additional column
            new_dp = [0] * S
            for i in range(S):
                for j in compat[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        # Step 4: Return total valid configurations
        return sum(dp) % MOD

