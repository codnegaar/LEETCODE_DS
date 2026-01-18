'''
Matching Pairs

Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
        int matchingPairs(String s, String t)
        Input
                s and t are strings of length N
                N is between 2 and 1,000,000
        Output
                Return an integer denoting the maximum number of matching pairs

Example 1:
        s = "abcd"
        t = "adcb"
        output = 4
        Explanation: Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
                     Therefore, the number of matching pairs of s and t will be 4.
        
Example 2:
        s = "mno"
        t = "mno"
        output = 1
        Explanation: Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.

'''

import math
import collections


# Count initial matches
def match_counter(s,t):
  return sum(1 for i in range(len(s)) if s[i] == t[i])


# return mismatch pairs
def find_mismatches(s, t):
    mismatch_list = []
    s_char = set()
    t_char = set()

    for i in range(len(s)):
        if s[i] != t[i]:
            mismatch_list.append((s[i], t[i]))
            s_char.add(s[i])
            t_char.add(t[i])

    return mismatch_list, s_char, t_char

  
# Check the possibility of two match-fixes
def has_two_way_swap(mismatch_list):
    mismatch_set = set(mismatch_list)
    for a, b in mismatch_list:
        if (b, a) in mismatch_set:
            return True
    return False
  

  
# check single mismatch fix
def has_one_way_swap(mismatch_list, s_char, t_char):
    for a, b in mismatch_list:
        if a in t_char or b in s_char:
            return True
    return False

  
def matching_pairs(s, t):  
    if s == t:
      return len(s) - 2  # forced to swap two different chars
    match_count = match_counter(s, t)
    mismatch_list, s_char, t_char = find_mismatches(s, t)
    
    if has_two_way_swap(mismatch_list):
      return match_count + 2
    
    if has_one_way_swap(mismatch_list, s_char, t_char):
      return match_count + 1
    
    return match_count - 1  # no useful swap available









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
