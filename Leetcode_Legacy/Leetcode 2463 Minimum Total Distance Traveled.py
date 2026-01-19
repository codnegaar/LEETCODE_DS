'''

Leetcode 2463 Minimum Total Distance Traveled

There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot.
You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth
factory and that the jth factory can repair at most limitj robots.
The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. 
When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.
Note that:
          All robots move at the same speed.
          If two robots move in the same direction, they will never collide.
          If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
          If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
          If the robot moved from a position x to a position y, the distance it moved is |y - x|.
           

Example 1:
        Input: robot = [0,4,6], factory = [[2,2],[6,2]]
        Output: 4
        Explanation: As shown in the figure:
        - The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
        - The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
        - The third robot at position 6 will be repaired at the second factory. It does not need to move.
        The limit of the first factory is 2, and it fixed 2 robots.
        The limit of the second factory is 2, and it fixed 1 robot.
        The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

Example 2:
        Input: robot = [1,-1], factory = [[-2,1],[2,1]]
        Output: 2
        Explanation: As shown in the figure:
        - The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
        - The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
        The limit of the first factory is 1, and it fixed 1 robot.
        The limit of the second factory is 1, and it fixed 1 robot.
        The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
         

Constraints:
        1 <= robot.length, factory.length <= 100
        factory[j].length == 2
        -109 <= robot[i], positionj <= 109
        0 <= limitj <= robot.length
        The input will be generated such that it is always possible to repair every robot.
        

'''

from typing import List, Dict, Tuple

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Calculate the minimum total distance required for robots to reach factories for repairs.

        Args:
            robot (List[int]): A list of robot positions.
            factory (List[List[int]]): A list of factories, where each factory is represented 
                                       as [position, capacity].

        Returns:
            int: Minimum total distance for all robots to be repaired.
        """

        def dfs(i: int, j: int, load: int) -> int:
            """
            A recursive depth-first search function to determine the minimum distance 
            to repair robots using the available factories.

            Args:
                i (int): The current index of the robot being processed.
                j (int): The current index of the factory being considered.
                load (int): The current load (number of robots) processed by the factory at index j.

            Returns:
                int: Minimum distance to repair remaining robots given the current state.
            """
            # Base case 1: All robots have been assigned to a factory
            if i >= len(robot):
                return 0

            # Base case 2: No more factories available, but robots remain unassigned
            if j >= len(factory):
                return float('inf')

            # Memoization: Return previously computed result if available
            if (i, j, load) in memo:
                return memo[(i, j, load)]

            # Option 1: Skip the current factory for the current robot
            skip_factory = dfs(i, j + 1, 0)

            # Option 2: Assign current robot to the current factory if within capacity
            assign_to_factory = float('inf')
            if factory[j][1] > load:
                distance = abs(robot[i] - factory[j][0])
                assign_to_factory = distance + dfs(i + 1, j, load + 1)

            # Record the minimum distance for the current state in memo
            memo[(i, j, load)] = min(skip_factory, assign_to_factory)
            return memo[(i, j, load)]

        # Sort robot and factory positions to minimize distance
        robot.sort()
        factory.sort()

        # Memoization dictionary to store computed states
        memo: Dict[Tuple[int, int, int], int] = {}

        # Start DFS with initial indices and load
        return dfs(0, 0, 0)
