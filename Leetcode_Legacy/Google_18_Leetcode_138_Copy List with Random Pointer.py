'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value 
of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the
pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the 
original list.
For example:   if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the 
               copied list, x.random --> y.   Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
          val: an integer representing Node.val
          random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
          Your code will only be given the head of the original linked list.

Example 1: Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]  --> output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Video: https://www.youtube.com/watch?v=5Y2EiZST97Y

Solution
  Runtime complexity: O(N)
  Space complexity: O(N)
 

Here is how the solution algorithm works to find a paid that adds up to the target.
For this problem, we will use a map to track the arbitrary nodes pointed by the original list. 
Then, we create a deep copy of the original linked list in two passes.For the first pass, we 
create a copy of the original linked list. When create the new copy, use the same values for 
data and arbitrary_pointer in the copied list. Furthermore, itΓÇÖs important to keep updating 
the map with entries where the key is the address to the old node and the value is the address 
of the new node. Once weΓÇÖve created the copy, again weΓÇÖll pass the copied linked list and update 
the arbitrary pointers to the new address created in the first pass.

'''
 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
                
        '''
           create a hashmap, it's pretty straightforward right if we had a old node 
           that was null we want to the copy is also going to be null
        
        '''
        
        hashCopy = {None: None}        
        cur = head
        
        while cur: # First loop for nodes(value)
            copiedNode = Node(cur.val)
            hashCopy[cur] = copiedNode 
            cur = cur.next
            
            '''
               Run the loop one more time setting current to the beginning of the
               Linked list keep going until we reach the end of the linked lis            
            
            '''
            
        cur = head  # second loop for pointers
        while cur:
            copiedNode = hashCopy[cur]
            copiedNode.next = hashCopy[cur.next]
            copiedNode.random = hashCopy[cur.random]
            
            # Traverse in linkedList
            cur = cur.next

        return hashCopy [head]

        
