'''


'''
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        lvl = 0

        for c in s:
            if (c == '(' and lvl > 0) or (c == ')' and lvl > 1):
                res.append(c)
            lvl += (c == '(') - (c == ')')

        return "".join(res)
