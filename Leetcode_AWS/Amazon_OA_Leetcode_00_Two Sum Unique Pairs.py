'''
Two Sum Unique Pairs(ount distinct pairs with given sum)
Write a function that takes a list of numbers and a target number, and then returns the number of unique pairs that add up to the target number.
[X, Y] and [Y, X] are considered the same pair, and not unique.

Examples
Example 1:
          Input: [1, 1, 2, 45, 46, 46], target = 47
          Output: 2

'''
from typing import List
def two_sum_unique_pairs(nums: List[int], target: int) -> int:
	seen = set()
	complement = set()
	for num in nums:
		if target - num in complement:
			pair = (num, target-num) if num< target-num else (target-num, num)
			seen.add(pair)
		complement.add(num)
	return len(seen)

if __name__ == '__main__':
    nums = [int(x) for x in input("Please enter a series of numbers and use comma separator: ").split(',')]
    target = int(input("Please enter a number for target: "))
    res = two_sum_unique_pairs(nums, target)
    print(f"Total number of unique pairs is: {res}")
    
'''
Please enter a series of numbers and use comma separator: 2,3,5,3,6,1,4,7,8,3,9,2,10,1,4,5
Please enter a number for target: 11
Total number of unique pairs is: 5
'''
