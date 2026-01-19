'''
Leetcode 1717 Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.
        Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
        Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".
        Return the maximum points you can gain after applying the above operations on s.

Example 1:
        Input: s = "cdbcbbaaabab", x = 4, y = 5
        Output: 19
        Explanation:
        - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
        - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
        - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
        - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
        Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
        Input: s = "aabbaaxybbaabb", x = 5, y = 4
        Output: 20 

Constraints:
        1 <= s.length <= 105
        1 <= x, y <= 104
        s consists of lowercase English letters.

'''

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            first_pair, first_score = "ba", y
            second_pair, second_score = "ab", x
        else:
            first_pair, first_score = "ab", x
            second_pair, second_score = "ba", y

        def remove_and_score(s: str, pair: str, score: int) -> (str, int):
            stack = []
            local_res = 0
            for char in s:
                if char == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    local_res += score
                else:
                    stack.append(char)
            return "".join(stack), local_res

        # First pass to remove the higher-scoring substrings
        remaining_string, gain = remove_and_score(s, first_pair, first_score)
        res += gain

        # Second pass to remove the lower-scoring substrings
        _, gain = remove_and_score(remaining_string, second_pair, second_score)
        res += gain

        return res

