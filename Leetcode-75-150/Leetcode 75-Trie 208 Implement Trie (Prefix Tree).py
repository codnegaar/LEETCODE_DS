'''
Leetcode 75-Trie 208 Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

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

Explanation:
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
        At most 3 * 104 calls in total will be made to insert, search, and startsWith

The Trie data structure is a tree-like data structure used to store a collection of strings in a way that allows for efficient retrieval and prefix search.
In a Trie, each node represents a prefix of one or more strings, with the root node representing the empty string. Each node also has a boolean flag 
indicating whether a string ends at that node.

The intuition behind using a Trie is that we can efficiently search for a string or a prefix in the set of strings by traversing the Trie. We start at
the root node and move down the tree, following the edges labeled with the characters of the string or prefix we're searching for. If we reach a node
that has a string ending at it, then we know that the string we're searching for is in the set. If we reach a node that doesn't have a string ending 
at it, then we know that the string or prefix is not in the set.

Approach for this Problem :

1- Define a TrieNode class that has an array of TrieNode pointers to represent its children and a boolean value to indicate if it is the end of a word.

2- Define a Trie class that has a pointer to the root TrieNode.

3- Implement the insert method of the Trie class that takes a string as input and inserts it into the Trie by traversing the Trie based on each character
   in the string. If a TrieNode for a particular character does not exist, create one and set it as the child of the current TrieNode. Mark the final 
   TrieNode as the end of a word.

4- Implement the search method of the Trie class that takes a string as input and returns true if the string is in the Trie and false otherwise. 
  Traverse the Trie based on each character in the string. If a TrieNode for a particular character does not exist, return false. If the end of the word
   is reached and the TrieNode is marked as the end of a word, return true. Otherwise, return false.

5- Implement the startsWith method of the Trie class that takes a string as input and returns true if there is any word in the Trie that starts with
   the given prefix and false otherwise. Traverse the Trie based on each character in the prefix. If a TrieNode for a particular character does not
   exist, return false. Otherwise, return true.

6- Create a Trie object and call its insert, search, and startsWith methods to use the Trie data structure.

'''

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWordCompleted = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                newRoot.children[alphabetIndex] = TrieNode()
            newRoot = newRoot.children[alphabetIndex]
        newRoot.isWordCompleted = True
    
    def search(self, word: str) -> bool:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        if newRoot.isWordCompleted == True:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        newRoot = self.root
        for ch in prefix:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        return True
