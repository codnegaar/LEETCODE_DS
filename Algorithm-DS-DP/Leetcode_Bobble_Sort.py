'''
  Bubble Sort
Report Issue
Conceptually, bubble sort is an implementation of a rather simple idea. Suppose we have a collection of integers that we want to sort in ascending order. Bubble sort proceeds to consider two adjacent elements at a time. If these two adjacent elements are out of order (in this case, the left element is strictly greater than the right element), bubble sort will swap them. It then proceeds to the next pair of adjacent elements. In the first pass of bubble sort, it will process every set of adjacent elements in the collection once, making swaps as necessary. The core idea of bubble sort is it will repeat this process until no more swaps are made in a single pass, which means the list is sorted.



In terms of the running time of the algorithm, bubble sort’s runtime is entirely based on the number of passes it must make in the array until it’s sorted. If the array has nn elements, each pass will consider (n - 1)(n−1) pairs. In the worst case, when the minimum element is at the end of the list, it will take (n - 1)(n−1) passes to get it to the proper place at the front of the list, and then one more additional pass to determine that no more swaps are needed. Bubble sort, as a result, has worst case runtime of O(n^2)O(n 
2
 ). The space complexity of bubble sort is O(1)O(1). All sorting operations involve swapping adjacent elements in the original input array, so no additional space is required.

Bubble sort is also a stable sorting algorithm since equal elements will never have swapped places, so their relative ordering will be preserved.

Overall, bubble sort is fairly simple to implement, and it’s stable, but outside of that, this algorithm does not have many desirable features. It’s fairly slow for most inputs and, as a result, it is rarely used in practice.

Below is the implementation of bubble sort:

'''
class Solution:
    def bubble_sort(self, lst: List[int]) -> None:
      
        """
        Mutates lst so that it is sorted via swapping adjacent elements until the entire lst is sorted.
        """
        
        # create a boolean flag
        has_swapped = True
        
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                  
                    # Swap adjacent elements
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True          
