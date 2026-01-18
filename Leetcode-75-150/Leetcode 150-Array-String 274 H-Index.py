'''
Leetcode 150-Array-String 274 H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
        Input: citations = [3,0,6,1,5]
        Output: 3
        Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, and 5 citations respectively.
        Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
        Input: citations = [1,3,1]
        Output: 1

Constraints:
        n == citations.length
        1 <= n <= 5000
        0 <= citations[i] <= 1000

'''
# Heap Queu

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heap = []
        for citationNum in citations:
            heapq.heappush(heap, -citationNum)
        result = 0
        while heap:
            citationNum = heapq.heappop(heap)
            if -citationNum < result + 1:
                return result
            result += 1
        return result

#Second solution Array

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) # Sort the array in non-increasing order
        n = len(citations)
        h = 0
            
        # Iterate through the sorted array and compare each citation count to the number of papers that have at least that many citations
        for i in range(n):
            if citations[i] >= i+1: # If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index
                h = i+1        
        return h

# Second solution

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).

        Args:
        tokens (List[str]): A list of tokens representing the RPN expression.

        Returns:
        int: The evaluated result of the RPN expression.

        Supported operations are '+', '-', '*', and '/'.
        """
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    param_1 = ["2", "1", "+", "3", "*"]  # Sample input for RPN
    ret = solution.evalRPN(param_1)
    print(ret)  # Expected output: 9

