'''
Leetcod e(Stack) 682 Baseball Game
 
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
        An integer x.
        Record a new score of x.
        '+'.
        Record a new score that is the sum of the previous two scores.
        'D'.
        Record a new score that is the double of the previous score.
        'C'.
        Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Example 1:
        Input: ops = ["5","2","C","D","+"]
        Output: 30
        Explanation:
        "5" - Add 5 to the record, record is now [5].
        "2" - Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5].
        "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
        "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
        The total sum is 5 + 10 + 15 = 30.

Example 2:
        Input: ops = ["5","-2","4","C","D","9","+","+"]
        Output: 27
        Explanation:
        "5" - Add 5 to the record, record is now [5].
        "-2" - Add -2 to the record, record is now [5, -2].
        "4" - Add 4 to the record, record is now [5, -2, 4].
        "C" - Invalidate and remove the previous score, record is now [5, -2].
        "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
        "9" - Add 9 to the record, record is now [5, -2, -4, 9].
        "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
        "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
        The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

Example 3:
        Input: ops = ["1","C"]
        Output: 0
        Explanation:
        "1" - Add 1 to the record, record is now [1].
        "C" - Invalidate and remove the previous score, record is now [].
        Since the record is empty, the total sum is 0.
 
Constraints:
        1 <= operations.length <= 1000
        operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
        For operation "+", there will always be at least two previous scores on the record.
        For operations "C" and "D", there will always be at least one previous score on the record.

'''

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Evaluate the total score after performing operations on a record of scores.

        Parameters:
        operations (List[str]): List of operations, where each operation is one of:
            - An integer: Add this score to the record.
            - "+": Add the sum of the last two scores to the record.
            - "D": Double the last score and add it to the record.
            - "C": Remove the last score from the record.

        Returns:
        int: Total score after performing all operations.
        """
        stk = []  # Stack to maintain the score history

        for op in operations:
            if op == "+":  # Add the sum of the last two scores
                stk.append(stk[-1] + stk[-2])
            elif op == "D":  # Double the last score
                stk.append(stk[-1] * 2)
            elif op == "C":  # Remove the last score
                stk.pop()
            else:  # Add the score as an integer
                stk.append(int(op))

        return sum(stk)  # Total score is the sum of all scores in the stack

# Time Complexity: O(n), where n is the number of operations.
# Space Complexity: O(n), for the stack to store scores.

# Unit Test
def test_calPoints():
    sol = Solution()

    # Example 1: Basic case
    operations = ["5", "2", "C", "D", "+"]
    assert sol.calPoints(operations) == 30, "Test Case 1 Failed"

    # Example 2: Case with multiple cancels
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    assert sol.calPoints(operations) == 27, "Test Case 2 Failed"

    # Example 3: Empty operation list
    operations = []
    assert sol.calPoints(operations) == 0, "Test Case 3 Failed"

    # Example 4: Single valid score
    operations = ["10"]
    assert sol.calPoints(operations) == 10, "Test Case 4 Failed"

    # Example 5: Case with negatives and doubles
    operations = ["10", "-10", "D", "+"]
    assert sol.calPoints(operations) == -50, "Test Case 5 Failed"  # Corrected expected value

    print("All test cases passed!")

# Run the tests
test_calPoints()

