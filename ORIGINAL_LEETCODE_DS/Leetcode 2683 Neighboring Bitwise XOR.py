'''

Leetcode 2683 Neighboring Bitwise XOR
 
A 0-indexed array derived with length n is derived by computing the bitwise XOR (Γèò) of adjacent values in a binary array original of length n.
Specifically, for each index i in the range [0, n - 1]:
If i = n - 1, then derived[i] = original[i] Γèò original[0].
Otherwise, derived[i] = original[i] Γèò original[i + 1].
Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.
Return true if such an array exists or false otherwise.
A binary array is an array containing only 0's and 1's
 

Example 1:
        Input: derived = [1,1,0]
        Output: true
        Explanation: A valid original array that gives derived is [0,1,0].
        derived[0] = original[0] Γèò original[1] = 0 Γèò 1 = 1 
        derived[1] = original[1] Γèò original[2] = 1 Γèò 0 = 1
        derived[2] = original[2] Γèò original[0] = 0 Γèò 0 = 0

Example 2:
        Input: derived = [1,1]
        Output: true
        Explanation: A valid original array that gives derived is [0,1].
        derived[0] = original[0] Γèò original[1] = 1
        derived[1] = original[1] Γèò original[0] = 1

Example 3:
        Input: derived = [1,0]
        Output: false
        Explanation: There is no valid original array that gives derived.
         
Constraints:
        n == derived.length
        1 <= n <= 105
        The values in derived are either 0's or 1's

'''

from functools import reduce
from operator import xor
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Check if a valid original array exists given a derived array.

        Parameters:
        derived (List[int]): The derived array containing XOR results.

        Returns:
        bool: True if a valid original array exists, False otherwise.
        """
        # If the XOR of all elements in the derived array is 0,
        # it is possible to construct a valid original array.
        return reduce(xor, derived) == 0


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    derived = [1, 1, 0]
    result = solution.doesValidArrayExist(derived)
    print(f"Does a valid array exist? {result}")  # Expected output: True


 
