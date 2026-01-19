'''
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
        WordDictionary() Initializes the object.
        void addWord(word) Adds word to the data structure, it can be matched later.
        bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
        word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.

'''
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


# Second solution

class TrieNode:
    """
    Node structure for the Trie.
    Each node contains:
    - `children`: A dictionary mapping characters to their respective child nodes.
    - `is_word`: A boolean indicating if the node represents the end of a valid word.
    """
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    """
    WordDictionary supports adding words and searching words with wildcards.
    Methods:
    - addWord(word): Add a word to the dictionary.
    - search(word): Search for a word with optional wildcard support.
    """
    def __init__(self):
        """
        Initialize the WordDictionary with an empty root node.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add a word to the Trie.
        
        Parameters:
        - word (str): The word to add to the dictionary.
        """
        current_node = self.root
        for character in word:
            # Set default to add new child if character doesn't exist
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie, supporting '.' as a wildcard for any character.
        
        Parameters:
        - word (str): The word to search for, possibly containing '.'.

        Returns:
        - bool: True if the word exists in the Trie, False otherwise.
        """
        def dfs(node, index):
            """
            Depth-first search to handle wildcard matching.
            
            Parameters:
            - node (TrieNode): The current Trie node.
            - index (int): The current character index in the word.

            Returns:
            - bool: True if the word is found, False otherwise.
            """
            if index == len(word):  # Base case: end of the word
                return node.is_word
            
            char = word[index]
            if char == ".":
                # Explore all children for wildcard character
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            elif char in node.children:
                # Continue matching if the character exists
                return dfs(node.children[char], index + 1)

            return False  # No match found

        # Start DFS from the root
        return dfs(self.root, 0)

