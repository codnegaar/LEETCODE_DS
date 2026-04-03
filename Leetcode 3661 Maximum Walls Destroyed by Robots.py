'''
Leetcode 3661 Maximum Walls Destroyed by Robots
 
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.
A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.
Return the maximum number of unique walls that can be destroyed by the robots.
Notes:
      A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
      Robots are not destroyed by bullets.
 

Example 1:
        Input: robots = [4], distance = [3], walls = [1,10]
        Output: 1
        Explanation:
        robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
        Thus, the answer is 1.

Example 2:
        Input: robots = [10,2], distance = [5,1], walls = [5,2,7]
        Output: 3
        Explanation:
        robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
        robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
        Thus, the answer is 3.

Example 3:
        Input: robots = [1,2], distance = [100,1], walls = [10]
        Output: 0
        Explanation:
        In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.
        
Constraints:
        1 <= robots.length == distance.length <= 105
        1 <= walls.length <= 105
        1 <= robots[i], walls[j] <= 109
        1 <= distance[i] <= 105
        All values in robots are unique
        All values in walls are unique

'''


class Solution:
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        n = len(robots)
        r = sorted(zip(robots, distance))
        rs = set(robots)
        
        bw = 0
        vw = []
        for w in walls:
            if w in rs:
                bw += 1
            else:
                vw.append(w)
        vw.sort()
        
        def get_w(x, y):
            if x > y:
                return 0
            i1 = bisect.bisect_left(vw, x)
            i2 = bisect.bisect_right(vw, y)
            return i2 - i1
        
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = get_w(r[0][0] - r[0][1], r[0][0] - 1)
        dp[0][1] = 0
        
        for i in range(1, n):
            L, d1 = r[i-1]
            R, d2 = r[i]
            
            eR = min(R - 1, L + d1)
            sL = max(L + 1, R - d2)
            
            wR = get_w(L + 1, eR)
            wL = get_w(sL, R - 1)
            wBoth = get_w(L + 1, R - 1) if eR >= sL else wR + wL
            
            dp[i][0] = max(dp[i-1][0] + wL, dp[i-1][1] + wBoth)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + wR)
            
        wEnd = get_w(r[-1][0] + 1, r[-1][0] + r[-1][1])
        ans = max(dp[-1][0], dp[-1][1] + wEnd)
        
        return ans + bw
