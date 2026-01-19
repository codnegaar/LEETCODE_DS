'''
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
Return true if the sum exists and return false if it does not.

  Solution:
  
   - Runtime complexity: O(N)
   - Space complexity: O(N) 

  In this solution, you can use the following algorithm to find a pair that add up to the target (say val).
  Scan the whole array once and store visited elements in a hash set. During scan, for every element e in the array,
  we check if val - e is present in the hash set i.e. val - e is already visited.
  If val - e is found in the hash set, it means there is a pair (e, val - e) in array whose sum is equal to the given val.
  If we have exhausted all elements in the array and didnΓÇÖt find any such pair, the function will return false.

'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
      
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
       
 

'''
// Java solution:

class Solution {
    public int getSum(int a, int b) {
        
        while (b != 0){
            int tmp = (a & b) << 1;
	        a = a ^ b;
	        b = tmp;           
            
        }
	
        return a;       
        
    }
}

'''
