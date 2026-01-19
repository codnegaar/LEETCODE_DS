"""
Algorithm:
Have two pointers which will define the starting index start and ending index end of the current window. Both will be 0 at the beginning.
Declare a Set that will store all the unique characters that we have encountered.
Declare a variable maxLength that will keep track of the length of the longest valid substring.
Scan the string from left to right one character at a time.
If the character has not encountered before i.e., not present in the Set the we will add it and increment the end index. 
The maxLength will be the maximum of Set.size() and existing maxLength.
If the character has encounter before, i.e., present in the Set, we will increment the start and we will remove the character at start index of the string.
Steps #5 and #6 are moving the window.
After the loop terminates, return maxLength.
"""
 if s == "":
    return 0
 firstChar = 0
 endChar = 0
 maxLen = 0
 longestSub = set()
 while endchar < len(s):
  if s[endChar] not in longestSub:
          longestSub.add(s[end])
          maxLen += 1
          maxLen = max(maxLen, len(longestSub))
      else:
          longestSub.remove(s[firstChar])
          start += 1
  return maxLen
