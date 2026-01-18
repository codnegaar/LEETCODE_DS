'''
Leetcode DFS 385. Mini Parser

Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.
Each element is either an integer or a list whose elements may also be integers or other lists.

Example 1:
        Input: s = "324"
        Output: 324
        Explanation: You should return a NestedInteger object which contains a single integer 324.

Example 2:
        Input: s = "[123,[456,[789]]]"
        Output: [123,[456,[789]]]
        Explanation: Return a NestedInteger object containing a nested list with 2 elements:
        1. An integer containing value 123.
        2. A nested list containing two elements:
            i.  An integer containing value 456.
            ii. A nested list with one element:
                 a. An integer containing value 789

Constraints:
        1 <= s.length <= 5 * 104
        s consists of digits, square brackets "[]", negative sign '-', and commas ','.
        s is the serialization of valid NestedInteger.
        All the values in the input are in the range [-106, 106].

'''

class Solution:
  def deserialize(self, s: str) -> NestedInteger:
    if s[0] != '[':
      return NestedInteger(int(s))

    stack = []

    for i, c in enumerate(s):
      if c == '[':
        stack.append(NestedInteger())
        start = i + 1
      elif c == ',':
        if i > start:
          num = int(s[start:i])
          stack[-1].add(NestedInteger(num))
        start = i + 1
      elif c == ']':
        popped = stack.pop()
        if i > start:
          num = int(s[start:i])
          popped.add(NestedInteger(num))
        if stack:
          stack[-1].add(popped)
        else:
          return popped
        start = i + 1


