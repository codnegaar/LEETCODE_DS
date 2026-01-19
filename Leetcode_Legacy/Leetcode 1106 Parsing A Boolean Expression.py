'''
Leetcode 1106 Parsing A Boolean Expression
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:
        Input: expression = "&(|(f))"
        Output: false
        Explanation: 
        First, evaluate |(f) --> f. The expression is now "&(f)".
        Then, evaluate &(f) --> f. The expression is now "f".
        Finally, return false.

Example 2:        
        Input: expression = "|(f,f,f,t)"
        Output: true
        Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:
        Input: expression = "!(&(f,t))"
        Output: true
        Explanation: 
        First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
        Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:
        1 <= expression.length <= 2 * 104
        expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
'''
from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        Parses a boolean expression represented in the form of strings 't', 'f', '!', '&', '|' and returns the evaluated boolean value.
        
        @param self: Reference to the current instance of the class.
        @param expression: A string representing the boolean expression.
        @return: A boolean value representing the result of the evaluated expression.
        """
        # Stack to maintain intermediate values during parsing.
        stack = deque()

        for char in expression:
            # Skip comma and opening parenthesis since they do not affect the logic directly.
            if char == ',' or char == '(':
                continue
            # If the character is one of the boolean operators or boolean values, push it onto the stack.
            if char in ["t", "f", "!", "&", "|"]:
                stack.append(char)
            # When encountering a closing parenthesis, evaluate the sub-expression.
            elif char == ')':
                # Track if the sub-expression has a true or false value.
                has_true = False
                has_false = False
                
                # Pop elements until we reach an operator.
                while stack[-1] not in ["!", "&", "|"]:
                    top_value = stack.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True
                
                # Pop the operator from the stack.
                operator = stack.pop()
                
                # Evaluate the result based on the operator.
                if operator == "!":
                    # '!' negates the value, if there is any 'true', negate it.
                    stack.append("t" if not has_true else "f")
                elif operator == "&":
                    # '&' results in 'true' if there are no 'false' values.
                    stack.append("f" if has_false else "t")
                elif operator == "|":
                    # '|' results in 'true' if there is at least one 'true' value.
                    stack.append("t" if has_true else "f")
        
        # Return the final result as a boolean value ('t' -> True, 'f' -> False).
        return stack[-1] == "t"

# Example usage:
# sol = Solution()
# result = sol.parseBoolExpr("|(&(t,f,t),!(t))")
# print(result)
