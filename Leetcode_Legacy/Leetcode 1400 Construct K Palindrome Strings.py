'''
Leetcode 1400 Construct K Palindrome Strings

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise. 

Example 1:
        Input: s = "annabelle", k = 2
        Output: true
        Explanation: You can construct two palindromes using all characters in s.
        Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
        Input: s = "leetcode", k = 3
        Output: false
        Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
        Input: s = "true", k = 4
        Output: true
        Explanation: The only possible solution is to put each character in a separate string.
         
Constraints:
        1 <= s.length <= 105
        s consists of lowercase English letters.
        1 <= k <= 105

'''
class Solution:
    def canConstruct(self, s, k):
        """
        Determines if all characters in a string `s` can be used to construct `k` palindrome strings.

        :param s: str - The input string consisting of lowercase letters.
        :param k: int - The number of palindrome strings to construct.
        :return: bool - True if it is possible to construct `k` palindromes, otherwise False.
        """
        # If the length of the string is less than k, constructing k palindromes is impossible.
        if len(s) < k:
            return False

        # Count the frequency of each character in the string.
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Count the number of characters with odd frequencies.
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

        # The number of odd-frequency characters must not exceed `k`.
        return odd_count <= k


# Unit Tests
def test_canConstruct():
    sol = Solution()

    # Test case 1: Example 1
    s1, k1 = "annabelle", 2
    assert sol.canConstruct(s1, k1) == True, "Test Case 1 Failed"

    # Test case 2: Example 2
    s2, k2 = "leetcode", 3
    assert sol.canConstruct(s2, k2) == False, "Test Case 2 Failed"

    # Test case 3: Example 3
    s3, k3 = "true", 4
    assert sol.canConstruct(s3, k3) == True, "Test Case 3 Failed"

    # Test case 4: String length less than k
    s4, k4 = "abc", 5
    assert sol.canConstruct(s4, k4) == False, "Test Case 4 Failed"

    # Test case 5: Single character string
    s5, k5 = "a", 1
    assert sol.canConstruct(s5, k5) == True, "Test Case 5 Failed"

    # Test case 6: All characters with even counts
    s6, k6 = "aabb", 1
    assert sol.canConstruct(s6, k6) == True, "Test Case 6 Failed"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run unit tests
    test_canConstruct()
