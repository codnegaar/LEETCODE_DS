class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        length = m + n - 1

        if (length % 2 == 1 or grid[0][0] != "(" or
                grid[m - 1][n - 1] != ")"):
            return False

        @lru_cache(None)
        def dfs(row: int, col: int, balance: int) -> bool:
            balance += 1 if grid[row][col] == "(" else -1
            remaining = (m - 1 - row) + (n - 1 - col)

            if balance < 0 or balance > remaining:
                return False
            if row == m - 1 and col == n - 1:
                return balance == 0

            return (
                (row + 1 < m and dfs(row + 1, col, balance)) or
                (col + 1 < n and dfs(row, col + 1, balance))
            )

        return dfs(0, 0, 0)
