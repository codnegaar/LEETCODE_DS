
'''
383 Ransom Note 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote. 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''
class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    count1 = collections.Counter(ransomNote)
    count2 = collections.Counter(magazine)
    return all(count1[c] <= count2[c] for c in string.ascii_lowercase)


# Second solution
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Time complexity (TC) for Counter is O(n)
        hashmap = Counter(magazine) 

        for c in ransomNote:
            if hashmap[c] > 0:
                hashmap[c]-=1
            else:
                return False
        return True

# Time Complexity: O(R + M)  -> R = len(ransomNote), M = len(magazine)
# Space Complexity: O(M)     -> we're using a hashmap 

# Third Solution:
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if the given ransomNote can be constructed using the letters from the magazine.
        
        Parameters:
        ransomNote (str): The string that represents the ransom note you are trying to construct.
        magazine (str): The string containing the letters that can be used to construct the ransom note.

        Returns:
        bool: True if the ransomNote can be constructed from the letters in the magazine, False otherwise.
        """
        # Create frequency counters for ransomNote and magazine using collections.Counter
        count1 = collections.Counter(ransomNote)
        count2 = collections.Counter(magazine)
        
        # Check if all character counts in ransomNote are less than or equal to those in magazine
        return all(count1[c] <= count2[c] for c in count1)

# Instantiate the Solution class
solution = Solution()

# Test cases to check if ransomNote can be constructed from magazine
print(solution.canConstruct("aa", "aab"))  # Output: True
# Explanation: The magazine contains two 'a' characters, enough to construct the ransom note "aa".

print(solution.canConstruct("aa", "ab"))   # Output: False
# Explanation: The magazine contains only one 'a' character, which is insufficient to construct "aa".
