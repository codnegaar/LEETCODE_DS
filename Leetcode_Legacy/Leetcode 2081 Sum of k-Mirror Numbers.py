'''
Leetcode 2081 Sum of k-Mirror Numbers

A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

Example 1:
        Input: k = 2, n = 5
        Output: 25
        Explanation:
        The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
          base-10    base-2
            1          1
            3          11
            5          101
            7          111
            9          1001
        Their sum = 1 + 3 + 5 + 7 + 9 = 25. 

Example 2:
        Input: k = 3, n = 7
        Output: 499
        Explanation:
        The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
          base-10    base-3
            1          1
            2          2
            4          11
            8          22
            121        11111
            151        12121
            212        21212
        Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.

Example 3:
        Input: k = 7, n = 17
        Output: 20379000
        Explanation: The 17 smallest 7-mirror numbers are:
        1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596      

Constraints:
        2 <= k <= 9
        1 <= n <= 30
'''

class Solution:
    """
    A class to find the sum of the first n k-palindromes.

    A k-palindrome is a number whose representation in base k is the same when read forwards or backwards.
    """

    def kMirror(self, k: int, n: int) -> int:
        """
        Find the sum of the first n k-palindromes.

        Parameters:
        k (int): The base in which the palindrome is represented.
        n (int): The number of k-palindromes to sum.

        Returns:
        int: The sum of the first n k-palindromes.
        """
        
        def is_palindrome_in_base_k(x: int) -> bool:
            """
            Checks whether a number is a palindrome in base k.

            Parameters:
            x (int): The number to check.

            Returns:
            bool: True if x is a palindrome in base k, False otherwise.
            """
            # Convert number x to its base k representation
            digs = []
            while x > 0:
                digs.append(x % k)
                x //= k
            # Check if the list of digits is the same forwards and backwards
            return digs == digs[::-1]

        total, cnt, length = 0, 0, 1
        while cnt < n:
            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            
            # Generate half palindromes directly
            for half in range(start, end):
                s = str(half)
                
                # Create the full palindrome from half the digits
                if length % 2 == 0:
                    pal_s = s + s[::-1]
                else:
                    pal_s = s + s[-2::-1]
                
                pal = int(pal_s)
                
                # Check if the palindrome is valid in base k
                if is_palindrome_in_base_k(pal):
                    total += pal
                    cnt += 1
                    
                    # If we have found n palindromes, return the sum
                    if cnt == n:
                        return total
            
            # Increment length of half-palindrome for next iteration
            length += 1
        return total
