'''
Leetcode 3548 Equal Sum Grid Partition II
 
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.
Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

Example 1:
        Input: grid = [[1,4],[2,3]]
        Output: true
        Explanation: A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.

Example 2:
        Input: grid = [[1,2],[3,4]]        
        Output: true        
        Explanation:        
                A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
                By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:
        Input: grid = [[1,2,4],[2,3,5]]
        Output: false
        Explanation:
                A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
                By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as 
                it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:
        Input: grid = [[4,1,8],[3,2,6]]
        Output: false
        Explanation: No valid cut exists, so the answer is false.

Constraints:
        1 <= m == grid.length <= 105
        1 <= n == grid[i].length <= 105
        2 <= m * n <= 105
        1 <= grid[i][j] <= 105
        
'''
class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        total = 0
        bottom = defaultdict(int)
        top = defaultdict(int)
        left = defaultdict(int)
        right = defaultdict(int)

        # Initialize bottom and right maps
        for row in grid:
            for x in row:
                total += x
                bottom[x] += 1
                right[x] += 1

        sumTop = 0

        # 🔹 Horizontal cuts
        for i in range(m - 1):
            for j in range(n):
                val = grid[i][j]
                sumTop += val

                top[val] += 1
                bottom[val] -= 1

            sumBottom = total - sumTop

            if sumTop == sumBottom:
                return True

            diff = abs(sumTop - sumBottom)

            if sumTop > sumBottom:
                if self.check(top, grid, 0, i, 0, n - 1, diff):
                    return True
            else:
                if self.check(bottom, grid, i + 1, m - 1, 0, n - 1, diff):
                    return True

        sumLeft = 0

        # 🔹 Vertical cuts
        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                sumLeft += val

                left[val] += 1
                right[val] -= 1

            sumRight = total - sumLeft

            if sumLeft == sumRight:
                return True

            diff = abs(sumLeft - sumRight)

            if sumLeft > sumRight:
                if self.check(left, grid, 0, m - 1, 0, j, diff):
                    return True
            else:
                if self.check(right, grid, 0, m - 1, j + 1, n - 1, diff):
                    return True

        return False

    def check(self, mp, grid, r1, r2, c1, c2, diff):
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1

        # single cell
        if rows * cols == 1:
            return False

        # 1D row
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff

        # 1D column
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff

        return mp.get(diff, 0) > 0
