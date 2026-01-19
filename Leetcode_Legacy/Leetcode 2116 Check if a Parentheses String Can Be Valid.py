'''
Leetcode 2116 Check if a Parentheses String Can Be Valid

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false. 

Example 1:
        Input: s = "))()))", locked = "010100"
        Output: true
        Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
        We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:
        Input: s = "()()", locked = "0000"
        Output: true
        Explanation: We do not need to make any changes because s is already valid.

Example 3:        
        Input: s = ")", locked = "0"
        Output: false
        Explanation: locked permits us to change s[0]. 
        Changing s[0] to either '(' or ')' will not make s valid.
 
Constraints:
        n == s.length == locked.length
        1 <= n <= 105
        s[i] is either '(' or ')'.
        locked[i] is either '0' or '1'.
'''
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        Determines if a string can be valid after adjusting unlocked parentheses.

        Parameters:
        s (str): A string of parentheses.
        locked (str): A string of binary characters indicating whether the character in `s` is locked (1) or unlocked (0).

        Returns:
        bool: True if the string can be valid, otherwise False.
        """
        n = len(s)
        # If the string length is odd, it's impossible to balance
        if n % 2 != 0:
            return False

        # Left-to-right pass: Ensure there are enough open parentheses
        open_balance = 0  # Tracks effective open parentheses
        for i in range(n):
            if locked[i] == '0':  # Unlocked slot can be treated as "(" or ")"
                open_balance += 1  # Treat it as "(" for now
            elif s[i] == '(':
                open_balance += 1  # Increase open count for "("
            else:  # s[i] == ")"
                open_balance -= 1  # Decrease open count for ")"
            
            if open_balance < 0:  # More ")" than "(" so far
                return False

        # Right-to-left pass: Ensure there are enough close parentheses
        close_balance = 0  # Tracks effective close parentheses
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':  # Unlocked slot can be treated as "(" or ")"
                close_balance += 1  # Treat it as ")" for now
            elif s[i] == ')':
                close_balance += 1  # Increase close count for ")"
            else:  # s[i] == "("
                close_balance -= 1  # Decrease close count for "("
            
            if close_balance < 0:  # More "(" than ")" so far
                return False

        # If both passes succeed, the string can be valid
        return True

 
