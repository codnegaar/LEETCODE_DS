'''
Leetcode 1o41
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
        "G": move one step. Position: (0, 1). Direction: North.
        "G": move one step. Position: (0, 2). Direction: North.
        "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
        "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
        "G": move one step. Position: (0, 1). Direction: South.
        "G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
               
        # define direction and position
        dirX, dirY = 0, 1 # faces north.
        x, y = 0 , 0      # robot initially stands at (0, 0) 
        
        for d in instructions:  
            
            if d  == "G": # position
                x =  x + dirX
                y =  y + dirY
                
            if d == "L":  # direction
                dirX = -1*dirY
                dirY = dirX
                
            else:         # direction
                dirX = dirY
                dirY =  -1*dirX
                
        '''
         Return true if and only if there exists a circle in the plane 
         such that the robot never leaves the circle.
        '''         
        return (x,y) == (0, 0) or (dirX, dirY) != (0, 1)
       
       
       
       
 # Solution II
   
class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    x = 0
    y = 0
    d = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for instruction in instructions:
     
      if instruction == 'G':
        x += directions[d][0]
        y += directions[d][1]
        
      elif instruction == 'L':
        d = (d + 3) % 4
        
      else:
        d = (d + 1) % 4
        
    return (x, y) == (0, 0) or d > 0    
       
                
        
        
        

