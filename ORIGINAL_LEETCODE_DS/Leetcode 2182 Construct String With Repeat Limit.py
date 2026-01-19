'''

Leetcode 2182 Construct String With Repeat Limit

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
Return the lexicographically largest repeatLimitedString possible.
A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) 
characters do not differ, then the longer string is the lexicographically larger one.

Example 1:
        Input: s = "cczazcc", repeatLimit = 3
        Output: "zzcccac"
        Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
        The letter 'a' appears at most 1 time in a row.
        The letter 'c' appears at most 3 times in a row.
        The letter 'z' appears at most 2 times in a row.
        Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
        The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
        Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

Example 2:
        Input: s = "aababab", repeatLimit = 2
        Output: "bbabaa"
        Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
        The letter 'a' appears at most 2 times in a row.
        The letter 'b' appears at most 2 times in a row.
        Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
        The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
        Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
         
Constraints:        
        1 <= repeatLimit <= s.length <= 105
        s consists of lowercase English letters.

'''
import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        """
        Constructs a lexicographically largest string under the following constraints:
        - The same character can appear consecutively at most `k` times.
        - Input string `s` is composed of lowercase English letters.

        Parameters:
            s (str): Input string consisting of lowercase letters.
            k (int): Maximum consecutive occurrences of the same character allowed.

        Returns:
            str: The lexicographically largest string adhering to the constraints.
        """
        # Count frequency of characters in the input string
        freq = Counter(s)

        # Create a max-heap using negative ASCII values for lexicographically largest sorting
        pq = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(pq)  # Convert the list into a heap

        result = []  # List to store the final result

        while pq:
            # Pop the character with the highest lexicographical order
            ch, count = heapq.heappop(pq)
            ch = chr(-ch)  # Convert back to the character
            use_count = min(count, k)  # Use the character up to `k` times

            # Append the character `use_count` times to the result
            result.append(ch * use_count)
            count -= use_count  # Update the remaining count for this character

            # If there's still a count left for this character, handle next character
            if count > 0:
                if not pq:  # If no other characters are available, stop
                    break

                # Pop the next lexicographically largest character
                next_ch, next_count = heapq.heappop(pq)
                next_ch = chr(-next_ch)
                
                # Append the next character once to separate repeated `ch`
                result.append(next_ch)
                next_count -= 1  # Reduce count for this character

                # Push back updated counts to the heap
                if next_count > 0:
                    heapq.heappush(pq, (-ord(next_ch), next_count))
                heapq.heappush(pq, (-ord(ch), count))  # Push back the remaining count for `ch`

        # Join the result list into a single string
        return "".join(result)


# Unit Tests
def test_repeatLimitedString():
    solution = Solution()

    # Example 1
    s = "cczazcc"
    k = 3
    assert solution.repeatLimitedString(s, k) == "zzcccac", "Test Case 1 Failed"

    # Example 2
    s = "aababab"
    k = 2
    assert solution.repeatLimitedString(s, k) == "bbabaa", "Test Case 2 Failed"

    # Edge Case 1: Single character
    s = "aaaaa"
    k = 1
    assert solution.repeatLimitedString(s, k) == "a", "Edge Case 1 Failed"

    # Edge Case 2: All unique characters
    s = "abcdef"
    k = 3
    assert solution.repeatLimitedString(s, k) == "fedcba", "Edge Case 2 Failed"

    # Edge Case 3: Consecutive same characters with limit
    s = "bbbbbccccc"
    k = 2
    assert solution.repeatLimitedString(s, k) == "ccbbccbb", "Edge Case 3 Failed"

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_repeatLimitedString()

