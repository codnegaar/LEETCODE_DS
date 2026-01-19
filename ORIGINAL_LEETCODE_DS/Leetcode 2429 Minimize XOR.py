'''
Leetcode 2429 Minimize XOR

Given two positive integers num1 and num2, find the positive integer x such that:
        x has the same number of set bits as num2, and
        The value x XOR num1 is minimal.
        Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.
The number of set bits of an integer is the number of 1's in its binary representation.

Example 1:
        Input: num1 = 3, num2 = 5
        Output: 3
        Explanation:
        The binary representations of num1 and num2 are 0011 and 0101, respectively.
        The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:
        Input: num1 = 1, num2 = 12
        Output: 3
        Explanation:
        The binary representations of num1 and num2 are 0001 and 1100, respectively.
        The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
     
Constraints:
        1 <= num1, num2 <= 109

'''
class Solution:
    def minimizeXor(self, num1, num2):
        """
        Minimize the XOR result between num1 and a number x by adjusting
        the number of set bits (1s) in x to match the number of set bits in num2.

        Parameters:
        num1 (int): The first input number.
        num2 (int): The second input number whose set bits count is used as reference.

        Returns:
        int: The minimized XOR result.
        """
        # Count the number of 1s (set bits) in binary representations of num1 and num2
        target_set_bits = bin(num2).count('1')

        # Start with num1, keeping its bits as close as possible to minimize XOR
        result = 0
        # List of bits in num1 from least significant to most significant
        num1_bits = [i for i in range(31, -1, -1) if num1 & (1 << i)]

        # First, turn on bits that already exist in num1 (prioritize minimizing XOR)
        for i in num1_bits:
            if target_set_bits > 0:
                result |= (1 << i)
                target_set_bits -= 1

        # If more bits are needed, turn on lower-order unset bits to minimize XOR further
        for i in range(32):
            if target_set_bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                target_set_bits -= 1

        return result

 
