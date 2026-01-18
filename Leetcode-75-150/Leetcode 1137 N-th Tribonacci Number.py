'''
1137 N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
        Input: n = 4
        Output: 4
        Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4
Example 2:
        Input: n = 25
        Output: 1389537

 Constraints:
        0 <= n <= 37
        The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

'''
class Solution:
    
    def __init__(self):
        self.func_table = dict()
        
        # base case:
        self.func_table[0] = 0
        self.func_table[1] = 1
        self.func_table[2] = 1
        
    
    def tribonacci(self, n: int) -> int:
        
        if n in self.func_table:
            # qucik resonse if tribonacci(n) has been computed before
            return self.func_table[n]
        
        else:
            # recusrion with memorization 
            self.func_table[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            return self.func_table[n]
