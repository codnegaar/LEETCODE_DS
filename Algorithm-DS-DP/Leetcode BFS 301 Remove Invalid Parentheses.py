'''
Leetcode BFS 301 Remove Invalid Parentheses

Hint: Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example 1:        
        Input: s = "()())()"
        Output: ["(())()","()()()"]

Example 2:        
        Input: s = "(a)())()"
        Output: ["(a())()","(a)()()"]

Example 3:          
          Input: s = ")("
          Output: [""]
 

Constraints:          
          1 <= s.length <= 25
          s consists of lowercase English letters and parentheses '(' and ')'.
          There will be at most 20 parentheses in s.

'''

class Solution:
  def removeInvalidParentheses(self, s: str) -> List[str]:
    # Similar to 921. Minimum Add to Make Parentheses Valid
    def getLeftAndRightCounts(s: str) -> Tuple[int, int]:
      """Returns how many '(' and ')' need to be deleted."""
      l = 0
      r = 0

      for c in s:
        if c == '(':
          l += 1
        elif c == ')':
          if l == 0:
            r += 1
          else:
            l -= 1

      return l, r

    def isValid(s: str):
      opened = 0  # the number of '(' - # of ')'
      for c in s:
        if c == '(':
          opened += 1
        elif c == ')':
          opened -= 1
        if opened < 0:
          return False
      return True  # opened == 0

    ans = []

    def dfs(s: str, start: int, l: int, r: int) -> None:
      if l == 0 and r == 0 and isValid(s):
        ans.append(s)
        return

      for i in range(start, len(s)):
        if i > start and s[i] == s[i - 1]:
          continue
        if r > 0 and s[i] == ')':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l, r - 1)
        elif l > 0 and s[i] == '(':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l - 1, r)

    l, r = getLeftAndRightCounts(s)
    dfs(s, 0, l, r)
    return ans
