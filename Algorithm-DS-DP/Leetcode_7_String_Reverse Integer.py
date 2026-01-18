'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit
integers (signed or unsigned).

Example 1:
        Input: x = 123
        Output: 321
Example 2:
        Input: x = -123
        Output: -321
Example 3:
        Input: x = 120
        Output: 21
 
Constraints:
        -231 <= x <= 231 - 1

'''

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX =  2147483648
        result = 0
        while x:
            digit = int(math.fmod(x,10)) # -1 % 10 = 9 , -1 // 10 = -1
            x=int(x/10)
            if (result >MAX // 10 or (result == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (result< MIN // 10 or (result == MIN // 10 and digit <= MIN % 10)):
                return 0
            result = (result * 10) + digit
        return  result



# Second Solution:

class Solution:
  def reverse(self, x: int) -> int:
        
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign

    while x:
      ans = ans * 10 + x % 10
      x //= 10

    return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans

