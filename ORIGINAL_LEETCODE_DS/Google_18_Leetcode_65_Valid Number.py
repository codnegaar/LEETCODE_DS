# Google_15_Leetcode_65_Valid Number
'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
    One of the following formats:
    One or more digits, followed by a dot '.'.
    One or more digits, followed by a dot '.', followed by one or more digits.
    A dot '.', followed by one or more digits.
    An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given an input string, determine if it makes a valid number or not. For simplicity, assume that white spaces are not present in the input.
    4.325 is a valid number.
    1.1.1 is NOT a valid number.
    222 is a valid number.
    is NOT a valid number.
    0.1 is a valid number.
    22.22. is NOT a valid number.

Solution
Runtime complexity: O(N)
Space complexity: O(1)
 
To check if a number is valid, weΓÇÖll use the state machine below. The initial state is start, and weΓÇÖll process each character to identify 
the next state. If the state ever ends up at unknown or in a decimal, the number is not valid. add state machine visual



'''
class Solution:
    def isNumber(self, s: str) -> bool:
        digit, dec, e, symbol = False, False, False, False        
        for c in s:
            if c in '0123456789':
                digit = True                
            elif c in '+-':
                if symbol or digit or dec:
                    return False                
                else:
                    symbol = True                    
            elif c in "Ee":
                if not digit or e: return False
                else:
                    e = True
                    symbol = False
                    digit = False
                    dec = False 
                                        
            elif c == '.':
                if dec or e: return False 
                else:
                    dec = True                    
            else:
                return False            
        return digit
            
                    
                    
                
        
