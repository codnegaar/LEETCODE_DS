'''
Leetcode 1945 Sum of Digits of String After Convert

You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
        Convert: "zbax" Γ₧¥ "(26)(2)(1)(24)" Γ₧¥ "262124" Γ₧¥ 262124
        Transform #1: 262124 Γ₧¥ 2 + 6 + 2 + 1 + 2 + 4 Γ₧¥ 17
        Transform #2: 17 Γ₧¥ 1 + 7 Γ₧¥ 8
        Return the resulting integer after performing the operations described above.

Example 1:
        Input: s = "iiii", k = 1
        Output: 36
        Explanation: The operations are as follows:
        - Convert: "iiii" Γ₧¥ "(9)(9)(9)(9)" Γ₧¥ "9999" Γ₧¥ 9999
        - Transform #1: 9999 Γ₧¥ 9 + 9 + 9 + 9 Γ₧¥ 36
        Thus the resulting integer is 36.

Example 2:
        Input: s = "leetcode", k = 2
        Output: 6
        Explanation: The operations are as follows:
        - Convert: "leetcode" Γ₧¥ "(12)(5)(5)(20)(3)(15)(4)(5)" Γ₧¥ "12552031545" Γ₧¥ 12552031545
        - Transform #1: 12552031545 Γ₧¥ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 Γ₧¥ 33
        - Transform #2: 33 Γ₧¥ 3 + 3 Γ₧¥ 6
        Thus the resulting integer is 6.

Example 3:
        Input: s = "zbax", k = 2
        Output: 8
 
Constraints:
        1 <= s.length <= 100
        1 <= k <= 10
        s consists of lowercase English letters.

'''

class Solution(object):

    def getLucky(self, s, k):

        # Convert each character in the string to its corresponding numeric value in one step
        number = ''.join(str(ord(x) - ord('a') + 1) for x in s)
        
        # Perform the transformation `k` times
        for _ in range(k):

            # Sum the digits and convert back to string
            number = str(sum(int(digit) for digit in number))  

        # Return the final result as an integer
        return int(number)  
