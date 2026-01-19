'''
208 Implement Trie (Prefix Tree)
 
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

'''

class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
    self.isWord = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node: TrieNode = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.isWord = True

  def search(self, word: str) -> bool:
    node: TrieNode = self._find(word)
    return node and node.isWord

  def startsWith(self, prefix: str) -> bool:
    return self._find(prefix)

  def _find(self, prefix: str) -> Optional[TrieNode]:
    node: TrieNode = self.root
    for c in prefix:
      if c not in node.children:
        return None
      node = node.children[c]
    return node


# second solution
class TrieNode:
    """
    Node structure for the Trie.
    Each node contains a dictionary for its children and a flag to mark the end of a word.
    """

    def __init__(self):
        self.children = {}  # Dynamic dictionary to store children
        self.is_end = False  # Flag to indicate if this node marks the end of a word


class Trie:
    """
    Trie (Prefix Tree) implementation to store words and prefixes.
    Efficient for word insertion, search, and prefix checking.

    Methods:
        insert: Adds a word to the Trie.
        search: Checks if a word exists in the Trie.
        startsWith: Checks if a prefix exists in the Trie.
    """

    def __init__(self):
        """
        Initialize the root node of the Trie.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Parameters:
        - word (str): The word to be inserted.
        """
        node = self.root
        for char in word:
            # Add the character as a child node if it doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the child node
        node.is_end = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Parameters:
        - word (str): The word to search for.

        Returns:
        - bool: True if the word exists, False otherwise.
        """
        node = self.root
        for char in word:
            # If the character isn't found, the word doesn't exist
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the child node
        return node.is_end  # Return True if it's the end of the word

    def startsWith(self, prefix: str) -> bool:
        """
        Check if a prefix exists in the Trie.

        Parameters:
        - prefix (str): The prefix to check.

        Returns:
        - bool: True if the prefix exists, False otherwise.
        """
        node = self.root
        for char in prefix:
            # If the character isn't found, the prefix doesn't exist
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the child node
        return True  # Prefix exists if traversal is successful


# Unit Test
def test_trie():
    """
    Unit tests for the Trie class.
    """
    trie = Trie()

    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")

    # Test cases for search
    assert trie.search("apple") == True, "Test case 1 failed"
    assert trie.search("app") == True, "Test case 2 failed"
    assert trie.search("appl") == False, "Test case 3 failed"

    # Test cases for startsWith
    assert trie.startsWith("app") == True, "Test case 4 failed"
    assert trie.startsWith("bat") == False, "Test case 5 failed"

    print("All test cases passed!")


# Example of usage
if __name__ == "__main__":
    test_trie()

