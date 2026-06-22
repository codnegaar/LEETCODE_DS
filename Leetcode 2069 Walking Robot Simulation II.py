'''

LeetCode 2069 Walking Robot Simulation II

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
 

Example 1:
        example-1
        Input
        ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
        [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
        Output
        [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]
        
        Explanation
                Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
                robot.step(2);  // It moves two steps East to (2, 0), and faces East.
                robot.step(2);  // It moves two steps East to (4, 0), and faces East.
                robot.getPos(); // return [4, 0]
                robot.getDir(); // return "East"
                robot.step(2);  // It moves one step East to (5, 0), and faces East.
                                // Moving the next step East would be out of bounds, so it turns and faces North.
                                // Then, it moves one step North to (5, 1), and faces North.
                robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
                robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                                // Then, it moves four steps West to (1, 2), and faces West.
                robot.getPos(); // return [1, 2]
                robot.getDir(); // return "West"
 

Constraints:
        2 <= width, height <= 100
        1 <= num <= 105
        At most 104 calls in total will be made to step, getPos, and getDir.

'''
# Added using AI
class Robot:
    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.dir = "East"
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        perim = 2 * (self.width - 1) + 2 * (self.height - 1)
        num %= perim
        if num == 0:
            num = perim

        while num > 0:
            if self.dir == "East":
                maxX = min(self.x + num, self.width - 1)
                rem  = num - (maxX - self.x)
                num  = rem
                if rem == 0: self.x = maxX
                else:        self.x = maxX; self.dir = "North"
            elif self.dir == "West":
                minX = max(self.x - num, 0)
                rem  = num - (self.x - minX)
                num  = rem
                if rem == 0: self.x = minX
                else:        self.x = minX; self.dir = "South"
            elif self.dir == "North":
                maxY = min(self.y + num, self.height - 1)
                rem  = num - (maxY - self.y)
                num  = rem
                if rem == 0: self.y = maxY
                else:        self.y = maxY; self.dir = "West"
            elif self.dir == "South":
                minY = max(self.y - num, 0)
                rem  = num - (self.y - minY)
                num  = rem
                if rem == 0: self.y = minY
                else:        self.y = minY; self.dir = "East"

    def getPos(self): return [self.x, self.y]
    def getDir(self): return self.dir

