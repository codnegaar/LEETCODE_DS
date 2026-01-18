'''
Radix Sort
Report Issue
A problem we encounter with counting sort is that it can’t easily handle strings where the alphabet size could be unconstrained. Additionally,
when the maximum value of the array is extraordinarily large, counting sort will lose its appeal since the additional memory overhead can cause 
things to slow down quite a bit.

Radix sort is an extension of counting sort that handles these problems. It works well with collections of strings and collections of integers
(especially when the maximum value is large).
There are a couple of variations of radix sort, but let’s focus on Least Significant Digit (LSD) Radix Sort.

Let’s use the example array A = [256, 336, 736, 443, 831, 907]A=[256,336,736,443,831,907]

LSD Radix Sort
The basic principle of LSD radix sort is to start with the rightmost, least significant, digit (in the case of strings, the rightmost character)
of each integer and perform a counting sort on just that digit. Since counting sort is a stable sort, it will keep elements in their relative
order in the case of ties.

After the first step of sorting we get the following array (focus on the last digit here):
[831, 443, 256, 336, 736, 907]

We repeat the process on the second digit to get the following array:
[907, 831, 336, 736, 443, 256]

And finally, the last step involves the leftmost digit, which then gives us our sorted array:
[256, 336, 443, 736, 831, 907]

In the case where Radix sort has to deal with integers that have a different number of digits, the leftmost digits in smaller numbers will be 
treated as 0 anyways, so the sorting algorithm will still work. In the case of strings, a common practice is to pad the smaller length strings
with special characters that are treated as the minimum values in an alphabet until the smaller length strings match the length of the longest string.

Here is the full LSD radix sort algorithm for integers. 1. Find the number of digits in the maximum integer. Let that be W 2. For each integer,
loop through digits from 1 to W in right to left order (least significant to most significant digit) * On each group of digits, perform counting sort
Below is the implementation of LSD Radix Sort (note that it uses a modified implementation of counting sort):


'''

class Solution:
    def counting_sort(self, lst: List[int], place_val: int, K: int = 10) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K
        """
        # intitialize count array of size K
        counts = [0] * K

        for elem in lst:
            digit = (elem // place_val) % 10
            counts[digit] += 1

        # we now overwrite our original counts with the starting index
        # of each digit over our group of digits
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            digit = (elem // place_val) % 10
            sorted_lst[counts[digit]] = elem
            # since we have placed an item in index counts[digit],
            # we need to increment counts[digit] index by 1 so the
            # next duplicate digit is placed in appropriate index
            counts[digit] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(len(lst)):
            lst[i] = sorted_lst[i]

    def radix_sort(self, lst: List[int]) -> None:
        # shift the minimum value in lst to be 0
        shift = min(lst)
        lst[:] = [num - shift for num in lst]
        max_elem = max(lst)

        # apply the radix sort algorithm
        place_val = 1
        while place_val <= max_elem:
            self.counting_sort(lst, place_val)
            place_val *= 10

        # undo the original shift
        lst[:] = [num + shift for num in lst]
        
        
        
     '''
The running time of LSD Radix sort requires a few parameters. Let WW be the maximum digit length within the list of integers.
Let NN be the size of the original input integer array. And lastly, since we are using counting sort, we must also be aware 
of the alphabet size KK. In the case of digits, it’s a constant 10, but when applied to other inputs, this alphabet size may 
change.

With these parameters defined, the running time of LSD radix sort is O(W(N + K))O(W(N+K)) as a result of at most WW calls
to counting sort. The amount of extra space needed is the same as counting sort – O(N + K)O(N+K).

The advantage of LSD Radix sort is that for a set of integers and strings with a reasonable WW and KK. It can be extraordinarily
fast, sorting in close to linear time (when WW is small). It is also a stable sort.

The disadvantages are that LSD radix sort does require some overhead memory, which when NN and/or KK is large, can cause major
performance hits when compared to other sorts. Additionally, it does require looking at all digits due to the fact that more 
significant digits later down the line have more impact on the final sorted result. Another type of radix sort that’s commonly
used that uses similar ideas looks at the most significant digit (MSD) first and is called MSD radix sort. This approach has a
better average case and best case performance than LSD radix sort, though the implementation is significantly trickier.

'''
