'''
Leetcode 190 Reverse Bits
 
Reverse bits of a given 32 bits signed integer.

Example 1:
        Input: n = 43261596
        Output: 964176192
        Explanation:
        Integer	Binary
        43261596	00000010100101000001111010011100
        964176192	00111001011110000010100101000000

Example 2:
        Input: n = 2147483644
        Output: 1073741822
        Explanation:
        Integer	Binary
        2147483644	01111111111111111111111111111100
        1073741822	00111111111111111111111111111110 

Constraints:
        0 <= n <= 231 - 2
        n is even. 

'''




class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        Parameters:
        n (int): A 32-bit unsigned integer.

        Returns:
        int: The integer obtained by reversing the bits of `n`.
        """
        # Convert `n` to a 32-bit binary string, reverse the string,
        # and convert it back to an integer.
        reversed_binary = "{:032b}".format(n)[::-1]
        return int(reversed_binary, 2)
 
