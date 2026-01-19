'''

Leetcode 1233 Remove Sub-Folders from the Filesystem

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], 
followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 
Example 1:
        Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        Output: ["/a","/c/d","/c/f"]
        Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:
        Input: folder = ["/a","/a/b/c","/a/b/d"]
        Output: ["/a"]
        Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:
        Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
        Output: ["/a/b/c","/a/b/ca","/a/b/d"] 

Constraints:
        1 <= folder.length <= 4 * 104
        2 <= folder[i].length <= 100
        folder[i] contains only lowercase letters and '/'.
        folder[i] always starts with the character '/'.
        Each folder name is unique.
'''
class Solution(object):
    def removeSubfolders(self, folders):
        """
        Removes subfolders from a list of folder paths.

        :param folders: List[str] - A list of folder paths.
        :return: List[str] - A list of root-level folders without any subfolders.
        """

        # Step 1: Sort the list of folder paths lexicographically
        # This ensures that all subfolders follow their respective parent folders
        folders.sort()

        # Result list to hold the root-level folders
        result = []

        # Step 2: Iterate through each folder path
        for path in folders:
            # Check if result is empty or the current path is not a subfolder of the last folder in result
            # This is done by ensuring path does not start with the last added folder + '/'
            if not result or not path.startswith(result[-1] + '/'):
                result.append(path)  # Add the current path to the result list

        # Step 3: Return the list of root-level folders
        return result

# Example usage
solution = Solution()
folders = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
print(solution.removeSubfolders(folders))  # Output: ['/a', '/c/d', '/c/f']


