'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Solution:
Once again this problem follows the Top ΓÇÿKΓÇÖ Numbers pattern. Here is our approach to the problem:

Since the array is already sorted, we can first find the number closest to X through binary search. LetΓÇÖs say that number is Y.
The K closest numbers to K adjacent to Y in the array. We can search both sides of Y to find the closest numbers.
Then, we can use a heap to efficiently search for the closest numbers. We can take K numbers in both directions of Y
and push them in a min-heap sorted by their difference from X.

Finally, we extract the top K numbers from the min-heap to find the required numbers.

https://www.youtube.com/watch?v=o-YDQzHoaKM

 '''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k
     
        while l < r:
            m = (l+r)//2
        
            if x -arr[m]>arr[m+k]-x:
                l = m +1
            else:
                r=m
        return arr[l:l+k]


        
        



