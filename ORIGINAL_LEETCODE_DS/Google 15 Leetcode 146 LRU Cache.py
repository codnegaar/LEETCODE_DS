'''
Google 15 Leetcode 146 LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
      LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
      int get(int key) Return the value of the key if the key exists, otherwise return -1.
      void put(int key, int value) Update the value of the key if the key exists. Otherwise,
      add the key-value pair to the cache. If the number of keys exceeds the capacity from this 
      operation, evict the least recently used key. The functions get and put must each run in 
      O(1) average time complexity.

 

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

'''




class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]


# Second solution

class LRUCache:
    class Node:
        """
        Node class represents a doubly linked list node to store key-value pairs.
        """
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a given capacity.
        
        Parameters:
        capacity (int): Maximum capacity of the cache.
        """
        self.capacity = capacity
        self.head = self.Node(-1, -1)  # Dummy head node
        self.tail = self.Node(-1, -1)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}  # Dictionary to store key to Node mappings

    def _add_node(self, node: 'Node') -> None:
        """
        Adds a new node right after the head of the doubly linked list.
        
        Parameters:
        node (Node): The node to be added to the list.
        """
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def _delete_node(self, node: 'Node') -> None:
        """
        Deletes a node from the doubly linked list.
        
        Parameters:
        node (Node): The node to be deleted from the list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        """
        Gets the value of the key if it exists in the cache, otherwise returns -1.
        
        Parameters:
        key (int): The key to retrieve the value for.
        
        Returns:
        int: The value associated with the key, or -1 if not found.
        """
        if key in self.cache:
            node = self.cache[key]
            self._delete_node(node)
            self._add_node(node)  # Move the accessed node to the front (most recently used)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts a value in the cache. If the cache is at capacity, removes the least recently used item.
        
        Parameters:
        key (int): The key to insert or update.
        value (int): The value to associate with the key.
        """
        if key in self.cache:
            # Remove the existing node before updating
            node = self.cache[key]
            self._delete_node(node)
            del self.cache[key]

        if len(self.cache) == self.capacity:
            # Remove the LRU item, which is the node before the tail
            lru_node = self.tail.prev
            self._delete_node(lru_node)
            del self.cache[lru_node.key]

        # Insert the new node
        new_node = self.Node(key, value)
        self._add_node(new_node)
        self.cache[key] = new_node

### Example of Usage
if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))  # Expected output: 1
    lru_cache.put(3, 3)  # LRU key (2) is evicted
    print(lru_cache.get(2))  # Expected output: -1 (not found)
    lru_cache.put(4, 4)  # LRU key (1) is evicted
    print(lru_cache.get(1))  # Expected output: -1 (not found)
    print(lru_cache.get(3))  # Expected output: 3
    print(lru_cache.get(4))  # Expected output: 4

