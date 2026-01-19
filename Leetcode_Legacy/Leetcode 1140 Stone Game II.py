'''
Leetcode 1140 Stone Game II

Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 
The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get. 

Example 1:
        Input: piles = [2,7,9,4,4]
        Output: 10
        Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total.
        If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
        
Example 2:
        Input: piles = [1,2,3,4,5,100]
        Output: 104 

Constraints:
        1 <= piles.length <= 100
        1 <= piles[i] <= 104
'''

from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        total_piles = len(piles)
        suffix_sums = [0] * (total_piles + 1)
        
        # Calculate suffix sums
        for i in range(total_piles - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        
        # Use lru_cache to simplify memoization
        @lru_cache(None)
        def max_stones_alice_can_get(current_pile: int, m: int) -> int:
            if current_pile >= total_piles:
                return 0
            
            if current_pile + 2 * m >= total_piles:
                return suffix_sums[current_pile]
            
            max_stones = 0
            current_suffix_sum = suffix_sums[current_pile]
            
            # Try all possible moves (x from 1 to 2*m)
            for x in range(1, 2 * m + 1):
                next_m = max(m, x)
                current_stones = current_suffix_sum - max_stones_alice_can_get(current_pile + x, next_m)
                max_stones = max(max_stones, current_stones)
            
            return max_stones
        
        return max_stones_alice_can_get(0, 1)
