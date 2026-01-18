'''
Leetcode AWS-Spring 2405 Optimal Partition of String

Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition. Note that each character should belong to exactly one substring in a partition.

Example 1:
        Input: s = "abacaba"
        Output: 4
        Explanation:
        Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
        It can be shown that 4 is the minimum number of substrings needed.

Example 2:
        Input: s = "ssssss"
        Output: 6
        Explanation:
        The only valid partition is ("s","s","s","s","s","s").

Constraints:
        1 <= s.length <= 105
        s consists of only English lowercase letters.

'''

class Solution:
    def partitionString(self, s: str) -> int:
        last_pos = [0] * 26
        partitions = 0
        last_end = 0
        for i in range(len(s)):
            if last_pos[ord(s[i]) - ord('a')] >= last_end:
                partitions += 1
                last_end = i + 1
            last_pos[ord(s[i]) - ord('a')] = i + 1
        return partitions

# Second Solution 
class Solution:
    def partitionString(self, s: str) -> int:
        temp = ""
        count = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
            else:
                temp = s[i]
                count += 1
        if len(temp) != 0:
            count += 1
        return count

