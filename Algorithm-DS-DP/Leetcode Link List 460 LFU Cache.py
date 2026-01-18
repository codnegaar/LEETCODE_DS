'''
460 LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or insert the key if not already present. When the cache reaches its capacity, it should invalidate 
and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least 
recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or
put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
'''

class Node:
    def __init__(self, key, val, freq=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self._sentinel = Node(0, 0)
        self._len = 0
        self._sentinel.prev, self._sentinel.next = self._sentinel, self._sentinel
    
    def __len__(self): # implement magic method len() for DoublyLinkedList
        return self._len
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._len -= 1
        return node
    
    def remove_last(self):
        return self.remove(self._sentinel.prev)
    
    def insert_first(self, key, val, freq):
        node = Node(key, val, freq, self._sentinel, self._sentinel.next)
        node.next.prev = node
        self._sentinel.next = node
        self._len += 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        # a node: has a value, a frequency, prev and next pointers
        # nodes map: <key, node>
        # frequencies map: <frequency, a doubly linked list storing nodes that have that frequency>
        # could instead maintain a chained doubly linked list, with a dict storing <freq, place to insert a node with that freq>
        self._min_freq = 0
        self._nodes = {}
        self._freqs = {}

        self._capacity = capacity
        self._size = 0

    def get(self, key: int) -> int:
        if key not in self._nodes:
            return -1
        node = self._nodes[key]
        
        # adjust the frequencies lists
        self._freqs[node.freq].remove(node)
        if node.freq + 1 not in self._freqs:
            self._freqs[node.freq+1] = DoublyLinkedList()
        new_node = self._freqs[node.freq+1].insert_first(node.key, node.val, node.freq + 1)
        self._nodes[key] = new_node
        
        # adjust minimum frequency of the entire cache
        if self._min_freq == node.freq and len(self._freqs[node.freq]) == 0:
            self._min_freq = node.freq + 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._nodes:
            self.get(key)
            self._nodes[key].val = value
            return
        if self._size < self._capacity:
            self._size += 1
        else:
            # eviction 
            evicted_node = self._freqs[self._min_freq].remove_last()
            self._nodes.pop(evicted_node.key)
        if 1 not in self._freqs:
            self._freqs[1] = DoublyLinkedList()
        node = self._freqs[1].insert_first(key, value, 1)
        self._nodes[key] = node
        self._min_freq = 1
