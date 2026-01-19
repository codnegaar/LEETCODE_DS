'''
Leetcode 1404 Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
        If the current number is even, you have to divide it by 2.
        If the current number is odd, you have to add 1 to it.
        It is guaranteed that you can always reach one for all test cases.

 

Example 1:
        Input: s = "1101"
        Output: 6
        Explanation: "1101" corressponds to number 13 in their decimal representation.
        Step 1) 13 is odd, add 1 and obtain 14. 
        Step 2) 14 is even, divide by 2 and obtain 7.
        Step 3) 7 is odd, add 1 and obtain 8.
        Step 4) 8 is even, divide by 2 and obtain 4.  
        Step 5) 4 is even, divide by 2 and obtain 2. 
        Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
        Input: s = "10"
        Output: 1
        Explanation: "10" corressponds to number 2 in their decimal representation.
        Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
        Input: s = "1"
        Output: 0
 

Constraints:
        1 <= s.length <= 500
        s consists of characters '0' or '1'
        s[0] == '1'


'''

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0  # Initialize step counter
        carry = 0  # Initialize carry which will be used for addition operations
        n = len(s) - 1  # Calculate the last index of the string
        
        # Iterate from the last index to the first index (excluding the first character)
        for i in range(n, 0, -1):
            # Convert the current character to an integer and add any carry from previous operations
            if int(s[i]) + carry == 1:
                # If the sum is 1, set carry to 1 because we would need to add 1 to make it 0 (odd number +1 then /2)
                carry = 1
                steps += 2  # Increment steps by 2 (1 for adding and 1 for dividing by 2)
            else:
                # If the sum is 0 or 2 (0 with carry 0, or 0 with carry 1), only need to divide by 2
                steps += 1  # Increment steps by 1 (just divide by 2)
        
        # After the loop, we must add the remaining carry to the first bit and take one more step if there's a carry
        return steps + carry  # Return the total number of steps

