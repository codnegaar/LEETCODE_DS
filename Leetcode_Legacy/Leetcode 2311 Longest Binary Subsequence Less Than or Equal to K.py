'''
Leetcode 2311 Longest Binary Subsequence Less Than or Equal to K

You are given a binary string s and a positive integer k.
Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
Note:
        The subsequence can contain leading zeroes.
        The empty string is considered to be equal to 0.
        A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
         
Example 1:
        Input: s = "1001010", k = 5
        Output: 5
        Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
        Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
        The length of this subsequence is 5, so 5 is returned.

Example 2:
        Input: s = "00101001", k = 1
        Output: 6
        Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
        The length of this subsequence is 6, so 6 is returned.
         
Constraints:
        1 <= s.length <= 1000
        s[i] is either '0' or '1'.
        1 <= k <= 109
'''
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ones = []
		# Notice how I reversed the string,
		# because the binary representation is written from greatest value of 2**n
        for i, val in enumerate(s[::-1]):
            if val == '1':
                ones.append(i)
		# Initialize ans, there are already number of zeroes (num_of_zeroes = len(nums) - len(ones)
        ans = n - len(ones)
        i = 0
		# imagine k == 5 and binary string 001011
		# ones = [0, 1, 3]
		# first loop: 5 - 2**0 -> 4, ans += 1
		# second loop: 4 - 2**1 -> 2, ans +=1
		# Third loop does not occur because 2 - 2**3 -> -6 which is less than zero
		# So the ans is 3 + 2 = 5
        while i < len(ones) and k - 2 ** ones[i] >= 0:
            ans += 1
            k -= 2 ** ones[i]
            i += 1
	
        return ans
