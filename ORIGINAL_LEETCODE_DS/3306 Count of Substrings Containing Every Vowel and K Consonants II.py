'''
3306 Count of Substrings Containing Every Vowel and K Consonants II

You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
        Input: word = "aeioqq", k = 1
        Output: 0
        Explanation:
                There is no substring with every vowel.

Example 2:
        Input: word = "aeiou", k = 0
        Output: 1
        Explanation:
                The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
        Input: word = "ieaouqqieaouqq", k = 1        
        Output: 3        
        Explanation:        
                The substrings with every vowel and one consonant are:        
                        word[0..5], which is "ieaouq".
                        word[6..11], which is "qieaou".
                        word[7..12], which is "ieaouq".
        
Constraints:
        5 <= word.length <= 2 * 105
        word consists only of lowercase English letters.
        0 <= k <= word.length - 5

'''

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        result = 0
         # Precompute next_consonant: for every index, store the next index where a consonant occurs.
        next_consonant = [n] * n
        next_cons_index = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next_cons_index
            if word[i] not in vowels:
                next_cons_index = i

        vowel_count = {}
        cons_count = 0
        left = 0  # left pointer for the sliding window

        for right in range(n):
            ch = word[right]
            if ch in vowels:
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                cons_count += 1

            # If too many consonants, shrink from the left.
            while cons_count > k and left <= right:
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

            # When the current window has exactly k consonants and contains all vowels,
            # count all valid substrings formed by extending the window with following vowels.
            while left <= right and cons_count == k and len(vowel_count) == 5:
                # All substrings from current valid window ending at 'right' and extending till
                # right before the next consonant are valid.
                result += next_consonant[right] - right

                # Move left pointer to try for a new valid window.
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

        return result
