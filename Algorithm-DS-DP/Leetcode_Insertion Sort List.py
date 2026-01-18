'''

Insertion Sort
Report Issue
Going back to our pile of books analogy, where we attempted to sort by weight, let's explore another approach to sorting the pile of books. We'll start at the top of the pile and iterate over the books one by one. Every time we encounter a book that is lighter than the book above it, we'll move the book up until it is in its appropriate place. Repeating this for the entire pile of books, we will get the books in sorted order.

This is the core intuition behind insertion sort. Given a collection of integers, you can sort the list by proceeding from the start of the list, and every time you encounter an element that is out of order, you can continuously swap places with previous elements until it is inserted in its correct relative location based on what you’ve processed thus far. This process is best understood with a visual example.



In terms of efficiency of this approach, the worst possible input is a reversed list, where every element has to be inserted at the very beginning of the list, which leads to a total of 1 + 2 + \ldots + (n - 1)1+2+…+(n−1) or O(n^2)O(n 
2
 ) swaps. The space complexity of insertion sort is O(1)O(1). All operations are performed in-place.

Despite the O(n^2)O(n 
2
 ) time complexity, in practice, there are a couple of advantages to insertion sort.

For one, it is a stable sort. By design of its implementation, we will never swap an element later in the list with an equal element earlier in the list. But more importantly, there are cases where insertion sort may actually be the best sort.

Generally, on almost sorted arrays where the number of inversions is relatively small compared to the size of the array, insertion sort will be quite fast since the number of swaps required will be low on almost sorted arrays.

Next, insertion sort can also be the best choice on small arrays. This is more of an empirical observation based on experiments, but it is one that you should be aware of. Many sorting functions have a quick check for the size of the collection and if that value is below a threshold, the program will default to insertion sort. Java's official implementation of Arrays.sort() performs such a check before performing more theoretically optimal sorts.

In terms of disadvantages, on larger collections with many inversions, other sorts will generally outperform insertion sort. However, of all the sorts we have covered thus far, insertion sort is the first that is practically used, depending on the context.

Below is the implementation of insertion sort:



'''


class Solution:
    def insertion_sort(self, lst: List[int]) -> None:
        """
        Mutates elements in lst by inserting out of place elements into appropriate
        index repeatedly until lst is sorted
        """
        for i in range(1, len(lst)):
            current_index = i

            while current_index > 0 and lst[current_index - 1] > lst[current_index]:
                # Swap elements that are out of order
                lst[current_index], lst[current_index - 1] = lst[current_index - 1], lst[current_index]
                current_index -= 1
