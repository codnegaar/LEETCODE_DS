
'''
Leetcode 1 Two_Sums


'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = {}
        for i, num in enumerate(nums):
            delta = target - num
            if delta in indexList:
                return [indexList[delta], i]
            indexList[num] = i
        return []
