'''
Leetcode 1007 Minimum Domino Rotations For Equal Row
 
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1. 

Example 1:
        Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
        Output: 2
        Explanation: 
        The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
        If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
        Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
        Output: -1
        Explanation: 
        In this case, it is not possible to rotate the dominoes to make one row of values equal.
         
Constraints:
        2 <= tops.length <= 2 * 104
        bottoms.length == tops.length
        1 <= tops[i], bottoms[i] <= 6
'''
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Determines the minimum number of rotations required to make all values in either
        the top or bottom row of dominoes the same.

        Parameters:
        tops (List[int]): List representing the top values of dominoes.
        bottoms (List[int]): List representing the bottom values of dominoes.

        Returns:
        int: Minimum number of rotations needed, or -1 if not possible.
        """
        def count_rotations(target: int, A: List[int], B: List[int]) -> int:
            """
            Count the number of rotations to make all values in A equal to `target`.
            Swaps with B[i] if needed. Returns infinity if impossible.

            Parameters:
            target (int): Value to align all elements in A to.
            A (List[int]): Current top or bottom list to make uniform.
            B (List[int]): The complementary list to swap with.

            Returns:
            int: Number of rotations needed or float('inf') if not possible.
            """
            rotations = 0
            for i in range(len(A)):
                if A[i] == target:
                    continue  # No rotation needed
                elif B[i] == target:
                    rotations += 1  # Rotation needed
                else:
                    return float('inf')  # Cannot align this domino
            return rotations

        # Candidates to align with: either the first top or bottom value
        candidates = {tops[0], bottoms[0]}

        # Try each candidate and find the minimal rotation
        min_rotations = float('inf')
        for candidate in candidates:
            min_rotations = min(
                min_rotations,
                count_rotations(candidate, tops, bottoms),
                count_rotations(candidate, bottoms, tops)
            )

        return min_rotations if min_rotations != float('inf') else -1


