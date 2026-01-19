'''
Leetcode 1079 Letter Tile Possibilities
 
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
        Input: tiles = "AAB"
        Output: 8
        Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
        Input: tiles = "AAABBC"
        Output: 188

Example 3:
        Input: tiles = "V"
        Output: 1 

Constraints:
        1 <= tiles.length <= 7
        tiles consists of uppercase English letters.

'''

from typing import Dict
import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Calculates the number of unique sequences that can be formed using the given tiles.

        Parameters:
        tiles (str): A string representing the tiles, where each character can be used multiple times.

        Returns:
        int: The total number of distinct sequences that can be formed.
        """
        count = collections.Counter(tiles)  # Frequency count of each tile

        def backtrack(count: Dict[str, int]) -> int:
            """
            Backtracking function to generate all possible sequences.

            Parameters:
            count (Dict[str, int]): A dictionary tracking the remaining counts of each tile.

            Returns:
            int: The total number of sequences formed from the current state.
            """
            possible_sequences = 0

            for tile, freq in count.items():
                if freq == 0:
                    continue

                # Choose the current tile
                count[tile] -= 1
                possible_sequences += 1 + backtrack(count)  # Include current choice and recurse

                # Backtrack (undo choice)
                count[tile] += 1

            return possible_sequences

        return backtrack(count)

# Example Usage
solution = Solution()
tiles = "AAB"
result = solution.numTilePossibilities(tiles)
print(f"Total unique sequences for tiles '{tiles}': {result}")


