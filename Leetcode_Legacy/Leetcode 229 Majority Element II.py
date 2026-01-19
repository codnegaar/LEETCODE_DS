'''
229 Majority Element II
 
Given an integer array of size n, find all elements that appear more than Γîè n/3 Γîï times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

'''
class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    ans1 = 0
    ans2 = 1
    count1 = 0
    count2 = 0

    for num in nums:
      if num == ans1:
        count1 += 1
      elif num == ans2:
        count2 += 1
      elif count1 == 0:
        ans1 = num
        count1 = 1
      elif count2 == 0:
        ans2 = num
        count2 = 1
      else:
        count1 -= 1
        count2 -= 1

    return [ans for ans in (ans1, ans2) if nums.count(ans) > len(nums) // 3]
