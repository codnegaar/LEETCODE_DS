'''

Leetcode 1371 Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
 
Example 1:
        Input: s = "eleetminicoworoep"
        Output: 13
        Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
        
Example 2:
        Input: s = "leetcodeisgreat"
        Output: 5
        Explanation: The longest substring is "leetc" which contains two e's.
        
Example 3:
        Input: s = "bcbcbc"
        Output: 6
        Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 
Constraints:
        1 <= s.length <= 5 x 10^5
        s contains only lowercase English letters.

'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state_map = {0: -1}
        max_len, mask = 0, 0

        for i, char in enumerate(s):
            if char in vowels:
                mask ^= vowels[char]
            if mask in state_map:
                max_len = max(max_len, i - state_map[mask])
            else:
                state_map[mask] = i

        return max_len



# Solution II
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        mask = 0
        max_len = 0
        mask_map = {0: -1}  # Map of mask to index, initialized with mask 0 at index -1

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                mask ^= vowel_to_bit[char]  # Flip the bit corresponding to the vowel

            if mask in mask_map:
                # If this mask was seen before, calculate the length of the substring
                max_len = max(max_len, i - mask_map[mask])
            else:
                # If this is the first time we see this mask, store its index
                mask_map[mask] = i

        return max_len



'''
Explanation:
Vowel to Bit Mapping:

Each vowel is mapped to a specific bit using a dictionary:
'a' -> 1 (binary: 00001)
'e' -> 2 (binary: 00010)
'i' -> 4 (binary: 00100)
'o' -> 8 (binary: 01000)
'u' -> 16 (binary: 10000)
Mask:
    We use a mask variable to represent the current state of vowel counts. For example:
    If mask == 0, all vowels have been seen an even number of times.
    If a vowel count becomes odd, we flip the corresponding bit in the mask using XOR (^).
    Dictionary (mask_map):

   We use a dictionary mask_map to store the first occurrence of each mask. The key is the mask, and the value is the index where this mask was first seen.
   Initially, the mask 0 is stored at index -1, because a mask of 0 means an empty substring where all vowels have been seen an even number of times.

Finding the Longest Substring:
    As we iterate through the string, we update the mask based on the vowels we encounter.
    If we encounter the same mask at a later point, it means the substring between the first and current occurrence of this mask has even counts of all vowels. We calculate the length of this substring and update the max_len accordingly.

Time Complexity:
    O(n) where n is the length of the string. This is because we make a single pass over the string, and all operations (bit flipping, dictionary lookups) are O(1).
    Space Complexity:
    O(1) for the mask (since it's constant size) and O(n) for the dictionary storing first occurrences of masks.
    
Example:
    For the string "eleetminicoworoep", the function will:

Map vowels to bits and flip the corresponding bits as we traverse the string.
Use the mask_map to track when we encounter the same vowel states (masks), allowing us to find the longest valid substring.
This approach should now solve the problem efficiently and correctly, without errors.

'''
