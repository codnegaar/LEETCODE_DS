'''
Leetcode 2566 Maximum Difference by Remapping a Digit

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:
        When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
        Bob can remap a digit to itself, in which case num does not change.
        Bob can remap different digits for obtaining minimum and maximum values respectively.
        The resulting number after remapping can contain leading zeroes.
 
Example 1:
        Input: num = 11891
        Output: 99009
        Explanation: 
        To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
        To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
        The difference between these two numbers is 99009.
        
Example 2:
        Input: num = 90
        Output: 99
        Explanation:
        The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
        Thus, we return 99. 

Constraints:
        1 <= num <= 108

'''
import re #optional
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        firstNon9 = re.search(r'[0-8]', s)
        firstNon0 = re.search(r'[1-9]', s)
        
        max_num = int(s.replace(s[firstNon9.start()], '9')) if firstNon9 else num
        min_num = int(s.replace(s[firstNon0.start()], '0')) if firstNon0 else num
        
        return max_num - min_num
