'''

Leetcode 1758 Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
        Input: s = "0100"
        Output: 1
        Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
        Input: s = "10"
        Output: 0
        Explanation: s is already alternating.

Example 3:
        Input: s = "1111"
        Output: 2
        Explanation: You need two operations to reach "0101" or "1010".         

Constraints:
        1 <= s.length <= 104
        s[i] is either '0' or '1'.

'''

class Solution:
    def minOperations(self, s: str) -> int:
        changes01 = 0  # Count of changes to convert to pattern "010101..."
        changes10 = 0  # Count of changes to convert to pattern "101010..."
        
        for i in range(len(s)):
            if s[i] != str(i % 2):
                changes01 += 1
            if s[i] != str((i + 1) % 2):
                changes10 += 1
        
        return min(changes01, changes10)

# Testing the function
solution = Solution()

# Test case 1
s = "0100"
print(solution.minOperations(s))  # Expected output: 1

# Test case 2
s = "1111"
print(solution.minOperations(s))  # Expected output: 2

# Test case 3
s = "1001"
print(solution.minOperations(s))  # Expected output: 1

# Test case 4
s = "01010101"
print(solution.minOperations(s))  # Expected output: 0


