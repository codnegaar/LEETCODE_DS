'''
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)




# Second solution
from typing import List, Set, Tuple

class TrieNode:
    """
    TrieNode represents a single node in the Trie data structure.
    It holds references to child nodes, a flag indicating if the node
    marks the end of a valid word, and a reference count to optimize deletion.
    """
    def __init__(self):
        self.children = {}  # Child nodes
        self.isWord = False  # End of word flag
        self.refs = 0  # Reference count

    def addWord(self, word: str):
        """
        Adds a word to the Trie.
        
        Args:
            word (str): The word to be added.
        """
        node = self
        node.refs += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.refs += 1
        node.isWord = True

    def removeWord(self, word: str):
        """
        Removes a word from the Trie by decrementing reference counters.
        
        Args:
            word (str): The word to be removed.
        """
        node = self
        node.refs -= 1
        for char in word:
            if char in node.children:
                next_node = node.children[char]
                next_node.refs -= 1
                if next_node.refs == 0:  # Prune unused nodes
                    del node.children[char]
                    return
                node = next_node

class Solution:
    """
    Solution class to find all valid words from a given board and word list.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds all words present on the board using a Trie and DFS.
        
        Args:
            board (List[List[str]]): 2D grid of characters.
            words (List[str]): List of words to search for.
        
        Returns:
            List[str]: List of words found on the board.
        """
        root = TrieNode()
        for word in words:
            root.addWord(word)  # Build Trie from word list

        rows, cols = len(board), len(board[0])
        result = set()  # Use set to avoid duplicate words
        visit = set()  # Track visited cells during DFS

        def dfs(r: int, c: int, node: TrieNode, word: str):
            """
            Depth-first search to find words on the board.
            
            Args:
                r (int): Row index.
                c (int): Column index.
                node (TrieNode): Current Trie node.
                word (str): Current word being built.
            """
            if (
                r < 0 or r >= rows or c < 0 or c >= cols or  # Out of bounds
                board[r][c] not in node.children or  # Char not in Trie
                node.children[board[r][c]].refs < 1 or  # No references left
                (r, c) in visit  # Already visited
            ):
                return

            visit.add((r, c))  # Mark cell as visited
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)  # Found a valid word
                node.isWord = False
                root.removeWord(word)  # Optimize by removing word from Trie

            # Explore all four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r, c))  # Unmark cell after exploring

        # Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)

# Example and Unit Test
if __name__ == "__main__":
    # Example board and words
    board = [
        ["o", "a", "b", "n"],
        ["o", "t", "a", "e"],
        ["a", "h", "k", "r"],
        ["a", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain", "oar"]

    # Create Solution instance and find words
    sol = Solution()
    result = sol.findWords(board, words)
    
    # Print result
    print("Words found:", result)

    # Unit Test
    assert sorted(result) == sorted(["oath", "eat", "oar"]), "Test Failed!"
    print("Test Passed!")

