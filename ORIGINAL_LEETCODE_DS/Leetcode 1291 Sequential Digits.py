'''
Leetcode 1291 Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
        Input: low = 100, high = 300
        Output: [123,234]

Example 2:
        Input: low = 1000, high = 13000
        Output: [1234,2345,3456,4567,5678,6789,12345] 

Constraints:
        10 <= low <= high <= 10^9

'''
class Solution:
    def sequentialDigits(self, low, high):
        result = []

        # Starting points for sequential digits
        for start in range(1, 10):
            num = start

            # Generate sequential digits starting with `start`
            for next_digit in range(start + 1, 10):
                num = num * 10 + next_digit
                if num > high:
                    break
                if num >= low:
                    result.append(num)

        return sorted(result)
