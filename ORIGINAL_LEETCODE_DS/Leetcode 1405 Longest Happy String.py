'''
Leetcode 1405 Longest Happy String

A string s is called happy if it satisfies the following conditions:
        s only contains the letters 'a', 'b', and 'c'.
        s does not contain any of "aaa", "bbb", or "ccc" as a substring.
        s contains at most a occurrences of the letter 'a'.
        s contains at most b occurrences of the letter 'b'.
        s contains at most c occurrences of the letter 'c'.
        Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string. 

Example 1:
        Input: a = 1, b = 1, c = 7
        Output: "ccaccbcc"
        Explanation: "ccbccacc" would also be a correct answer.

Example 2:
        Input: a = 7, b = 1, c = 0
        Output: "aabaa"
        Explanation: It is the only correct answer in this case.
     
Constraints:
        0 <= a, b, c <= 100
        a + b + c > 0
'''

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max heap to prioritize characters with the highest count
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []

        while pq:
            count1, char1 = heapq.heappop(pq)
            
            # Check if the last two characters are the same as the current character
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not pq:
                    break  # No alternative characters left

                # Use the second most frequent character instead
                count2, char2 = heapq.heappop(pq)
                result.append(char2)
                count2 += 1  # Decrement count (since it's negated)

                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))  # Push back if there are more of this character

                # Push the first character back to try later
                heapq.heappush(pq, (count1, char1))
            else:
                # Add the most frequent character
                result.append(char1)
                count1 += 1  # Decrement count (since it's negated)

                if count1 < 0:
                    heapq.heappush(pq, (count1, char1))  # Push back if there are more of this character

        return ''.join(result)
