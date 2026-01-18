'''

Leetcode 66 Array Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:
        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4].
Example 2:
        Input: digits = [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
        Incrementing by one gives 4321 + 1 = 4322.
        Thus, the result should be [4,3,2,2].

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]
        carry, indx = 1, 0
        
        while carry:
            if indx <len(digits):
                if digits[indx] == 9:
                    digits[indx] = 0
                else:
                    digits[indx] +=1
                    carry = 0
                    
            else:
                digits.append(1)
                carry = 0
            indx +=1
        return digits[::-1]

# Second solution
from typing import List

class Solution:
    """
    A solution to increment a large integer represented as an array of digits by one.

    Methods
    -------
    plusOne(digits: List[int]) -> List[int]:
        Adds one to the integer represented as an array of digits.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Adds one to the number represented by the digits array.

        Parameters
        ----------
        digits : List[int]
            A list of integers where each element represents a digit of a non-negative number.

        Returns
        -------
        List[int]
            A list of integers representing the incremented number.
        """
        
        # Reverse the digits for easier manipulation starting from the least significant digit
        digits = digits[::-1]
        
        carry, index = 1, 0  # Initialize carry to 1 (to add one) and start at the first index
        
        # Iterate while there's a carry to process
        while carry:
            if index < len(digits):  # If the index is within the bounds of the digits list
                if digits[index] == 9:  # If the current digit is 9, set it to 0 and continue carry
                    digits[index] = 0
                else:  # Otherwise, increment the digit and clear the carry
                    digits[index] += 1
                    carry = 0
            else:  # If we've processed all existing digits, append 1 (new leading digit)
                digits.append(1)
                carry = 0  # Clear the carry after appending
            index += 1  # Move to the next digit
        
        # Reverse the digits back to their original order and return
        return digits[::-1]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_digits = [9, 9, 9]
    print("Result after adding one:", solution.plusOne(example_digits))

# Improvements made:
# 1. Added docstrings for clarity.
# 2. Reorganized code for better readability.
# 3. Simplified carry-handling logic to make it clearer.
# 4. Added example usage for demonstration.

