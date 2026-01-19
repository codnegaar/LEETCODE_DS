'''
Leetcode 1900 The Earliest and Latest Rounds Where Players Compete
 
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their 
initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes
against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round,
the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. 
If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible
round number in which these two players will compete against each other, respectively.
 
Example 1:
        Input: n = 11, firstPlayer = 2, secondPlayer = 4
        Output: [3,4]
        Explanation:
        One possible scenario which leads to the earliest round number:
        First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        Second round: 2, 3, 4, 5, 6, 11
        Third round: 2, 3, 4
        One possible scenario which leads to the latest round number:
        First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        Second round: 1, 2, 3, 4, 5, 6
        Third round: 1, 2, 4
        Fourth round: 2, 4

Example 2:
        Input: n = 5, firstPlayer = 1, secondPlayer = 5
        Output: [1,1]
        Explanation: The players numbered 1 and 5 compete in the first round.
        There is no way to make them compete in any other round.
 
Constraints:
        2 <= n <= 28
        1 <= firstPlayer < secondPlayer <= n
'''

from functools import cache
from typing import List, Tuple

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        Returns the earliest and latest round when firstPlayer and secondPlayer can meet
        in a single-elimination tournament of n players.
        """

        @cache
        def dp(players: Tuple[int]) -> Tuple[int, int]:
            l, r = 0, len(players) - 1
            while l < r:
                a, b = players[l], players[r]

                if {a, b} == {firstPlayer, secondPlayer}:
                    return (1, 1)

                l += 1
                r -= 1

            def simulate_round(players: Tuple[int], idx: int, current: List[int], results: List[Tuple[int]]):
                """Recursively simulate the round matchups and generate all valid next round possibilities"""
                if idx >= len(players) // 2:
                    if len(players) % 2 == 1:
                        current.append(players[len(players) // 2])  # Middle player advances automatically
                    results.append(tuple(sorted(current)))
                    if len(players) % 2 == 1:
                        current.pop()
                    return

                a = players[idx]
                b = players[-(idx + 1)]

                # Simulate both outcomes unless the match contains firstPlayer or secondPlayer
                if {a, b} == {firstPlayer, secondPlayer}:
                    return  # Already handled earlier

                if firstPlayer in (a, b) or secondPlayer in (a, b):
                    winner = firstPlayer if a == firstPlayer or b == firstPlayer else secondPlayer
                    current.append(winner)
                    simulate_round(players, idx + 1, current, results)
                    current.pop()
                else:
                    for winner in (a, b):
                        current.append(winner)
                        simulate_round(players, idx + 1, current, results)
                        current.pop()

            next_rounds = []
            simulate_round(players, 0, [], next_rounds)

            earliest, latest = float("inf"), float("-inf")
            for next_players in next_rounds:
                e, l = dp(next_players)
                earliest = min(earliest, e)
                latest = max(latest, l)

            return (earliest + 1, latest + 1)

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        return list(dp(tuple(range(1, n + 1))))
