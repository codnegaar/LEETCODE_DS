'''

282 Expression Add Operators
 
Given a string num that contains only digits and an integer target, return all possibilities to
insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant 
expression evaluates to the target value.
Note that operands in the returned expressions should not contain leading zeros.

Example 1:
        Input: num = "123", target = 6
        Output: ["1*2*3","1+2+3"]
        Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
        
Example 2:
        Input: num = "232", target = 8
        Output: ["2*3+2","2+3*2"]
        Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
        
Example 3:
        Input: num = "3456237490", target = 9191
        Output: []
        Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 
Constraints:
        1 <= num.length <= 10
        num consists of only digits.
        -231 <= target <= 231 - 1

'''
class Solution:
  def addOperators(self, num: str, target: int) -> List[str]:
    ans = []

    # Start index, prev value, current evaluated value
    def dfs(start: int, prev: int, eval: int, path: List[str]) -> None:
      if start == len(num):
        if eval == target:
          ans.append(''.join(path))
        return

      for i in range(start, len(num)):
        if i > start and num[start] == '0':
          return
        s = num[start:i + 1]
        curr = int(s)
        if start == 0:
          path.append(s)
          dfs(i + 1, curr, curr, path)
          path.pop()
        else:
          for op in ['+', '-', '*']:
            path.append(op + s)
            if op == '+':
              dfs(i + 1, curr, eval + curr, path)
            elif op == '-':
              dfs(i + 1, -curr, eval - curr, path)
            else:
              dfs(i + 1, prev * curr, eval - prev + prev * curr, path)
            path.pop()

    dfs(0, 0, 0, [])
    return ans
