'''
1268 Search Suggestions System
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common 
prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
        Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
        Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
        Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
        After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
        After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
        Input: products = ["havana"], searchWord = "havana"
        Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        Explanation: The only word "havana" will be always suggested while typing the search word.
 
Constraints:
        1 <= products.length <= 1000
        1 <= products[i].length <= 3000
        1 <= sum(products[i].length) <= 2 * 104
        All the strings of products are unique.
        products[i] consists of lowercase English letters.
        1 <= searchWord.length <= 1000
        searchWord consists of lowercase English letters.
'''

class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
    self.word: Optional[str] = None


class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    ans = []
    root = TrieNode()

    def insert(word: str) -> None:
      node = root
      for c in word:
        if c not in node.children:
          node.children[c] = TrieNode()
        node = node.children[c]
      node.word = word

    def search(node: Optional[TrieNode]) -> List[str]:
      res: List[str] = []
      dfs(node, res)
      return res

    def dfs(node: Optional[TrieNode], res: List[str]) -> None:
      if len(res) == 3:
        return
      if not node:
        return
      if node.word:
        res.append(node.word)
      for c in string.ascii_lowercase:
        if c in node.children:
          dfs(node.children[c], res)

    for product in products:
      insert(product)

    node = root

    for c in searchWord:
      if not node or c not in node.children:
        node = None
        ans.append([])
        continue
      node = node.children[c]
      ans.append(search(node))

    return ans


