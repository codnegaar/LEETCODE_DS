'''
Graph 864 Shortest Path to Get All Keys

You are given an m x n grid grid where:
                '.' is an empty cell.
                '#' is a wall.
                '@' is the starting point.
                Lowercase letters represent keys.
                Uppercase letters represent locks.
                You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.
                If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
                For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly
                one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
                Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
        Input: grid = ["@.a..","###.#","b.A.B"]
        Output: 8
        Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:
        Input: grid = ["@..aA","..B#.","....b"]
        Output: 6

Example 3:
          Input: grid = ["@Aa"]
          Output: -1
 
Constraints:
          m == grid.length
          n == grid[i].length
          1 <= m, n <= 30
          grid[i][j] is either an English letter, '.', '#', or '@'. 
          There is exactly one '@' in the grid.
          The number of keys in the grid is in the range [1, 6].
          Each key in the grid is unique.
          Each key in the grid has a matching lock.
'''


from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        Find the shortest path to collect all keys in a grid. The grid contains walls, empty spaces,
        keys, locks, and a starting point '@'. The keys are represented by lowercase letters and
        locks by uppercase letters.

        Parameters:
        grid (List[str]): A list of strings representing the grid layout.

        Returns:
        int: The minimum number of steps to collect all keys, or -1 if it is impossible.

        Time Complexity: O(m * n * 2^k), where m and n are the dimensions of the grid and k is the number of keys.
        Space Complexity: O(m * n * 2^k) to store the visited states.
        """
        def bfs(x, y, num_keys):
            # Queue for BFS storing (row, col, key_mask)
            q = [(x, y, 0)]
            steps = 0

            while q:
                # Process nodes level by level
                level_size = len(q)
                steps += 1
                for _ in range(level_size):
                    i, j, key_mask = q.pop(0)
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        # Check if within bounds and if we haven't visited this state
                        if 0 <= ni < m and 0 <= nj < n and key_mask not in visited[ni][nj]:
                            cell = grid[ni][nj]
                            # Skip walls
                            if cell == "#":
                                continue
                            # If cell is empty or the start point
                            if cell in ".@":
                                visited[ni][nj].add(key_mask)
                                q.append((ni, nj, key_mask))
                            # If cell is a key, add it to the key_mask
                            elif cell.islower():
                                new_key_mask = key_mask | (1 << (ord(cell) - ord('a')))
                                visited[ni][nj].add(new_key_mask)
                                # If we collected all keys, return the step count
                                if new_key_mask == (1 << num_keys) - 1:
                                    return steps
                                q.append((ni, nj, new_key_mask))
                            # If cell is a lock, check if we have the corresponding key
                            elif cell.isupper() and (key_mask & (1 << (ord(cell) - ord('A')))):
                                visited[ni][nj].add(key_mask)
                                q.append((ni, nj, key_mask))
            return -1

        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Possible movement directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_keys = 0
        # Find the starting point and count the number of keys
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    num_keys += 1
                elif grid[i][j] == "@":
                    start_i, start_j = i, j
        # Visited array to track visited states with different key masks
        visited = [[set() for _ in range(n)] for _ in range(m)]
        visited[start_i][start_j].add(0)
        # Start BFS from the starting point
        return bfs(start_i, start_j, num_keys)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverse a 2D matrix in spiral order and return the elements in a list.

        Parameters:
        matrix (List[List[int]]): A 2D list of integers to be traversed in spiral order.

        Returns:
        List[int]: A list of integers in the order they are traversed spirally.

        Time Complexity: O(n), where n is the total number of elements in the matrix (m * n for m rows and n columns).
        Space Complexity: O(1) (excluding the output list).
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Traverse the matrix while boundaries are valid
        while left < right and top < bottom:
            # Traverse from left to right along the current top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down
            
            # Traverse from top to bottom along the current right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left
            
            # If there are no more rows or columns left, break
            if not (left < right and top < bottom):
                break

            # Traverse from right to left along the current bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up
            
            # Traverse from bottom to top along the current left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right

        return res
