'''
For this problem, we simply need to prioritize the more valuable boxes first. To do this, we should sort the boxtypes array (B)
in descending order by the number of units per box (B[i][1]).

Then we can iterate through B and at each step, we should add as many of the boxes as we can, until we reach the truck size (T).
We should add the number of boxes added multiplied by the units per box to our answer (ans), and decrease T by the same number of boxes.

Once the truck is full (T == 0), or once the iteration is done, we should return ans.

Time Complexity: O(N log N) where N is the length of B, for the sort
Space Complexity: O(1)

Example 1:	

Input:	-------> boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: ------->  	8
Explanation:	There are:

              - 1 box of the first type that contains 3 units.
              - 2 boxes of the second type that contain 2 units each.
              - 3 boxes of the third type that contain 1 unit each.

              You can take all the boxes of the first and second types, and one box of the third type.
              The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
              
              
Example 2:
              
Input:	 -------> boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output:	 ------->   91
 
 '''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_unit = 0
        for b,n in boxTypes:
            box_num = min(b, truckSize)
            max_unit += box_num * n
            truckSize -= box_num
            if truckSize == 0: return max_unit
        return max_unit
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  
