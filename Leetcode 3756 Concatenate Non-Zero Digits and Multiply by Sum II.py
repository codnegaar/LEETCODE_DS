'''

Leetcode 3756 Concatenate Non-Zero Digits and Multiply by Sum II

You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.

 

Example 1:
        Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]        
        Output: [12340, 4, 9]        
        Explanation:
                s[0..7] = "10203004"
                x = 1234
                sum = 1 + 2 + 3 + 4 = 10
                Therefore, answer is 1234 * 10 = 12340.
                s[1..3] = "020"
                x = 2
                sum = 2
                Therefore, the answer is 2 * 2 = 4.
                s[4..6] = "300"
                x = 3
                sum = 3
                Therefore, the answer is 3 * 3 = 9.

Example 2:
        Input: s = "1000", queries = [[0,3],[1,1]]        
        Output: [1, 0]        
        Explanation:        
                s[0..3] = "1000"
                x = 1
                sum = 1
                Therefore, the answer is 1 * 1 = 1.
                s[1..1] = "0"
                x = 0
                sum = 0
                Therefore, the answer is 0 * 0 = 0.

Example 3:        
        Input: s = "9876543210", queries = [[0,9]]        
        Output: [444444137]        
        Explanation:        
                s[0..9] = "9876543210"
                x = 987654321
                sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
                Therefore, the answer is 987654321 * 45 = 44444444445.
                We return 44444444445 modulo (109 + 7) = 444444137.
         

Constraints:
        1 <= m == s.length <= 105
        s consists of digits only.
        1 <= queries.length <= 105
        queries[i] = [li, ri]
        0 <= li <= ri < m
'''

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # idx[i] = number of non-zero digits before index i
        idx = [0] * (n + 1)

        # val[i] = number formed by first i non-zero digits
        val = [0] * (n + 1)

        # total[i] = sum of first i non-zero digits
        total = [0] * (n + 1)

        cnt = 0

        for i, ch in enumerate(s):
            digit = int(ch)

            if digit != 0:
                cnt += 1
                val[cnt] = (val[cnt - 1] * 10 + digit) % MOD
                total[cnt] = total[cnt - 1] + digit

            idx[i + 1] = cnt

        ans = []

        for l, r in queries:

            left = idx[l]
            right = idx[r + 1]

            # No non-zero digit in the range
            if left == right:
                ans.append(0)
                continue

            length = right - left

            number = (val[right] - val[left] * pow10[length]) % MOD
            sum_digits = total[right] - total[left]

            ans.append((number * sum_digits) % MOD)

        return ans
