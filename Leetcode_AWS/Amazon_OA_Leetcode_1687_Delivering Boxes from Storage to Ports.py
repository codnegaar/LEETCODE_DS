'''

You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on 
the number of boxes and the total weight that it can carry. You are given an array boxes, where boxes[i] = [ports​​i​, weighti],
and three integers portsCount, maxBoxes, and maxWeight. ports​​i is the port where you need to deliver the ith box and weightsi 
is the weight of the ith box.

portsCount is the number of ports.
maxBoxes and maxWeight are the respective box and weight limits of the ship.

The boxes need to be delivered in the order they are given. The ship will follow these steps:
    The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
    For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it.
    If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
    The ship then makes a return trip to storage to take more boxes from the queue.
    The ship must end at storage after all the boxes have been delivered.

Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.


First solution:
        
        n = len (boxes)
        dp = [sys.maxsize]*(n+1)
        dp[0]=0  # dp[i]=min trips to deliver boxes[0..i) and return to the storage
        
        weight = 0
        trips = 2
        left = 0
        
        for right in range(n):
            weight += boxes[right][1]
            if right> 0 and boxes[right][0] != boxes[right -1][0]:
                trips +=1
            while right - left > maxBoxes or weight > maxWeight or (left<right and dp[left]==dp[left+1]):
                weight -= boxes[left][1]
                
                if boxes[left][0] != boxes[left +1][0]:
                    trips -= 1
                left += 1
            dp[right +1] =dp[left]+ trips
        return dp[-1]
        

'''

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
       
        n = len(boxes)
        # dp[i] := min trips to deliver boxes[0..i) and return to the storage
        dp = [0] * (n + 1)
        trips = 2
        weight = 0

        l = 0
        for r in range(n):
            weight += boxes[r][1]

            # current box is different from previous one, need to make one more trip
            if r > 0 and boxes[r][0] != boxes[r - 1][0]:
                trips += 1

            # loading boxes[l] in the previous turn is always no bad than loading it in this turn
            while r - l + 1 > maxBoxes or weight > maxWeight or (l < r and dp[l + 1] == dp[l]):
                weight -= boxes[l][1]
                if boxes[l][0] != boxes[l + 1][0]:
                    trips -= 1
                l += 1
                #   min trips to deliver boxes[0..r]
                # = min trips to deliver boxes[0..l) + trips to deliver boxes[l..r]
            dp[r + 1] = dp[l] + trips

        return dp[n]

                
            
            
        
