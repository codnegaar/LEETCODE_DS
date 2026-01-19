'''
Leetcode 1531 String Compression II

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the c
oncatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc"
we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".
Notice that in this problem, we are not adding '1' after single characters.
Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Example 1:
        Input: s = "aaabcccd", k = 2
        Output: 4
        Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or
        'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" 
        which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

Example 2:        
        Input: s = "aabbaa", k = 2
        Output: 2
        Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

Example 3:
        Input: s = "aaaaaaaaaaa", k = 0
        Output: 3
        Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
         

Constraints:
      1 <= s.length <= 100
      0 <= k <= s.length
      s contains only lowercase English letters.


'''




from functools import cache

class Solution:
    def __init__(self):
        # Initialize any necessary attributes or states here if needed
        pass

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Lambda function to calculate the length of the run-length encoding for the frequency x
        getLength = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4

        @cache
        def recur(i: int, remaining_k: int) -> int:
            if i < 0:
                return 0
            res = recur(i - 1, remaining_k - 1) if remaining_k else float('inf')
            freq = 0
            local_k = remaining_k  # Use a local copy of k to track changes within this path
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    freq += 1
                elif local_k == 0:
                    break
                else:
                    local_k -= 1
                res = min(res, recur(j - 1, local_k) + getLength(freq))

            return res

        return recur(len(s) - 1, k)

# Example usage:
# solution = Solution()
# print(solution.getLengthOfOptimalCompression("abracadabra", 1))
