'''
Leetcode 1189 Maximum Number of Balloons
 
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed. 

        Example 1:
                Input: text = "nlaebolko"
                Output: 1

        Example 2:
                Input: text = "loonbalxballpoon"
                Output: 2

        Example 3:
                Input: text = "leetcode"
                Output: 0 

        Constraints:
                1 <= text.length <= 104
                text consists of lower case English letters only.

'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"
        
        for c in text:
            if c in balloon:
                counter[c] += 1
        
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])

# Time Complexity: O(n)
# Space Complexity: O(1)
