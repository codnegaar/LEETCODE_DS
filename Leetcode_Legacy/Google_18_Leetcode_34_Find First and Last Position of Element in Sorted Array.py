'''

Solution
      Runtime complexity: O(LOG(N))
      Space complexity: O(1)


Scanning the array in a linear fashion would be highly inefficient because the array size could be in the millions. 
Instead, we will use binary search twice: once to find the low index and once to find the high index.
HereΓÇÖs the algorithm to find the low index:

      At each step, consider the array between low and high indices and calculate the mid index.
      If the element at mid is greater or equal to the key, the high becomes mid - 1. Index at low remains the same.
      If the element at mid is less than the key, low becomes mid + 1.
      When low is greater than high, low would be pointing to the first occurrence of the key. If the element at low does not match the key, return -1.
      For high index, we can use a similar algorithm with slight changes.
      Switch the low index to mid + 1 when element at mid index is less than or equal to the key.
      Switch the high index to mid - 1 when the element at mid is greater than the key.

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    
    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i 
        
