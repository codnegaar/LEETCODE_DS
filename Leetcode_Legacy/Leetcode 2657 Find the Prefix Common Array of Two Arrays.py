'''

Leetcode 2657 Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once. 

Example 1:
        Input: A = [1,3,2,4], B = [3,1,2,4]
        Output: [0,2,3,4]
        Explanation: At i = 0: no number is common, so C[0] = 0.
        At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
        At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
        At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:
        Input: A = [2,3,1], B = [3,1,2]
        Output: [0,1,3]
        Explanation: At i = 0: no number is common, so C[0] = 0.
        At i = 1: only 3 is common in A and B, so C[1] = 1.
        At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3. 

Constraints:
        1 <= A.length == B.length == n <= 50
        1 <= A[i], B[i] <= n
        It is guaranteed that A and B are both a permutation of n integers.

'''
 from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Finds the prefix common array for two given arrays A and B.

        The prefix common array is defined as an array where the value at each index i
        represents the number of common elements between the prefixes A[:i+1] and B[:i+1].

        Parameters:
        A (List[int]): The first input array.
        B (List[int]): The second input array.

        Returns:
        List[int]: The prefix common array.
        """
        # Initialize a set to track seen elements and the count of common elements
        seen = set()
        common_count = 0
        result = []

        # Iterate over both arrays simultaneously
        for a, b in zip(A, B):
            # Add element from A to the seen set, increase common count if it's in B
            if a in seen:
                common_count += 1
            else:
                seen.add(a)

            # Add element from B to the seen set, increase common count if it's in A
            if b in seen:
                common_count += 1
            else:
                seen.add(b)

            # Append the current common count to the result
            result.append(common_count)

        return result

# Unit tests
if __name__ == "__main__":
    # Create an instance of the solution
    solution = Solution()

    # Test cases
    A1 = [1, 2, 3, 4]
    B1 = [2, 1, 4, 3]
    print("Test Case 1:", solution.findThePrefixCommonArray(A1, B1))  # Expected: [0, 2, 2, 4]

    A2 = [1, 2, 3]
    B2 = [3, 2, 1]
    print("Test Case 2:", solution.findThePrefixCommonArray(A2, B2))  # Expected: [0, 1, 3]

    A3 = [1, 1, 1]
    B3 = [1, 1, 1]
    print("Test Case 3:", solution.findThePrefixCommonArray(A3, B3))  # Expected: [1, 2, 3]

    A4 = [1, 2, 3]
    B4 = [4, 5, 6]
    print("Test Case 4:", solution.findThePrefixCommonArray(A4, B4))  # Expected: [0, 0, 0]

    A5 = [1]
    B5 = [1]
    print("Test Case 5:", solution.findThePrefixCommonArray(A5, B5))  # Expected: [1]
