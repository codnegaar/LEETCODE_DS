'''
Minimum Length Substrings

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
        Signature: int minLengthSubstring(String s, String t)
        Input: s and t are non-empty strings that contain less than 1,000,000 characters each
        Output: Return the minimum length of the substring of s. If it is not possible, return -1

Example:
        s = "dcbefebce"
        t = "fd"
        output = 5
        Explanation: Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
'''
import math
import collections

# Build required character counts from string t
def required_char_counter(t):
    return collections.Counter(t)

# Check if the current slice satisfies the required character counts
def slice_requirement(slice_counts, required_counts):
    for char in required_counts:
        if slice_counts[char] < required_counts[char]:
            return False  # (Fixed typo: Flase → False)
    return True

# Main function using your helper function names
def min_length_substring(s, t):
    if not s or not t:
        return -1

    required_counts = required_char_counter(t)
    slice_counts = collections.Counter()
    left = 0
    min_len = math.inf

    for right in range(len(s)):
        slice_counts[s[right]] += 1

        while slice_requirement(slice_counts, required_counts):
            min_len = min(min_len, right - left + 1)
            slice_counts[s[left]] -= 1
            left += 1

    return min_len if min_len != math.inf else -1



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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  
