'''
Leetcode 2379 Minimum Recolors to Get K Consecutive Black Blocks
 
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks. 

Example 1:
        Input: blocks = "WBBWWBBWBW", k = 7
        Output: 3
        Explanation:
        One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
        so that blocks = "BBBBBBBWBW". 
        It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
        Therefore, we return 3.

Example 2:
        Input: blocks = "WBWBBBW", k = 2
        Output: 0
        Explanation:
        No changes need to be made, since 2 consecutive black blocks already exist.
        Therefore, we return 0. 

Constraints:
        n == blocks.length
        1 <= n <= 100
        blocks[i] is either 'W' or 'B'.
        1 <= k <= n

'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Determines the minimum number of 'W' (white) blocks that need to be recolored 
        to form a contiguous substring of length k consisting entirely of 'B' (black) blocks.
        
        Parameters:
        blocks (str): A string consisting of 'B' (black) and 'W' (white) blocks.
        k (int): The required length of the contiguous substring of 'B' blocks.
        
        Returns:
        int: The minimum number of recolors required.
        """

        # Initial count of 'W' in the first window of size k
        min_recolor = cur_w_count = blocks[:k].count('W')

        # Sliding window approach: iterate through the remaining blocks
        for i in range(k, len(blocks)):
            # Update count: remove leftmost and add rightmost character in the window
            if blocks[i - k] == 'W':
                cur_w_count -= 1  # Remove outgoing 'W'
            if blocks[i] == 'W':
                cur_w_count += 1  # Add incoming 'W'

            # Update the minimum number of recolors found
            min_recolor = min(min_recolor, cur_w_count)

            # If we find a perfect window with 0 'W', we can break early
            if min_recolor == 0:
                break

        return min_recolor
