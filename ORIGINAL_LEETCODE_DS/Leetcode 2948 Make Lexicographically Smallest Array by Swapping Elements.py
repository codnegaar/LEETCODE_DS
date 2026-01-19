'''
Leetcode 2948 Make Lexicographically Smallest Array by Swapping Elements

You are given a 0-indexed array of positive integers nums and a positive integer limit.
In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.
Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. 
For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

Example 1:
        Input: nums = [1,5,3,9,8], limit = 2
        Output: [1,3,5,8,9]
        Explanation: Apply the operation 2 times:
        - Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
        - Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
        We cannot obtain a lexicographically smaller array by applying any more operations.
        Note that it may be possible to get the same result by doing different operations.

Example 2:
        Input: nums = [1,7,6,18,2,1], limit = 3
        Output: [1,6,7,18,1,2]
        Explanation: Apply the operation 3 times:
        - Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
        - Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
        - Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
        We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:
        Input: nums = [1,7,28,19,10], limit = 3
        Output: [1,7,28,19,10]
        Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
         
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109
        1 <= limit <= 109
'''

class Solution:
    """
    A solution to rearrange an array such that each group of numbers within
    the given limit remains sorted, preserving their lexicographical order.

    Methods
    -------
    lexicographicallySmallestArray(nums: list[int], limit: int) -> list[int]:
        Returns the lexicographically smallest array based on the given limit.
    """
    
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        """
        Rearranges the array into the lexicographically smallest order,
        where numbers are grouped based on the difference constraint (limit).

        Parameters
        ----------
        nums : list[int]
            The input array of integers.
        limit : int
            The maximum difference allowed between numbers in the same group.

        Returns
        -------
        list[int]
            The rearranged lexicographically smallest array.
        """
        # Initialize the result array
        ans = [0] * len(nums)
        
        # Pair each number with its index and sort them by the number values
        numAndIndexes = sorted([(num, i) for i, num in enumerate(nums)])
        
        # Group the numbers based on the limit constraint
        numAndIndexesGroups: list[list[tuple[int, int]]] = []
        for numAndIndex in numAndIndexes:
            # Start a new group if the difference exceeds the limit
            if (not numAndIndexesGroups or
                    numAndIndex[0] - numAndIndexesGroups[-1][-1][0] > limit):
                numAndIndexesGroups.append([numAndIndex])
            else:
                # Add the current number to the last group
                numAndIndexesGroups[-1].append(numAndIndex)
        
        # Sort numbers within each group and reassign them to their original indices
        for numAndIndexesGroup in numAndIndexesGroups:
            sortedNums = [num for num, _ in numAndIndexesGroup]  # Extract and sort numbers
            sortedIndices = sorted([index for _, index in numAndIndexesGroup])  # Extract and sort indices
            # Reassign sorted numbers to their respective indices
            for num, index in zip(sortedNums, sortedIndices):
                ans[index] = num
        
        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_nums = [8, 1, 4, 7, 6, 5]
    limit = 3
    print("Lexicographically smallest array:", solution.lexicographicallySmallestArray(example_nums, limit))

