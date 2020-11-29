# Define node of a doubly linked list
class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        
        self.capacity = capacity
        
        # hash map
        self.map = {}
        
        # doubly linked list
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    # For Testing purpose: convert the doubly linked list into list, start and end with Node(0,0)
    def dlinkedlist_to_list(self):
        ret = []
        count = self.size
        p = self.head.next
        while count != 0:
            ret.append(p.key)
            p = p.next
            count -= 1
        return ret
        
    # insert the new node in font of the tail in the doubly linked list
    def insert_node(self, new_node):
        temp = self.tail.prev
        temp.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = temp
        self.size += 1
    
    # romove the given node from the doubly linked list
    def remove_node(self, node):
        temp_head = node.prev
        temp_tail = node.next
        temp_head.next = temp_tail
        temp_tail.prev = temp_head
        self.size -= 1
        
    # remove all nodes from the doubly linked list, except head and tail
    def remove_all_nodes(self):
        curr = self.head.next
        while self.size != 0:
            self.remove_node(curr)
        
    # write the key
    def put(self, key, value):
        new_node = Node(key,value)
        
        # 1. add / update the hash map
        self.map[key] = new_node
        
        # 2. insert into the doubly linked list
        self.insert_node(new_node)
        
        # 3. check capacity
        if (len(self.map) > self.capacity):
            # capacity is exceeded => remove the LRU node
            
            lru_node = self.head.next
            self.remove_node(lru_node)
            del self.map[lru_node.key]
    
    # read the key
    def get(self, key):
        # check if the map contains key 
        if key in self.map:
            curr_node = self.map[key]

            self.remove_node(curr_node)
            self.insert_node(curr_node)
            return curr_node.value
        return -1
    
    # delete the key
    def delete(self, key):
        # assume key always exists in map
        
        if key in self.map:
            curr_node = self.map[key]
            self.remove_node(curr_node)
            del self.map[curr_node.key]
    
    # reset the cache
    def reset(self):
        
        self.remove_all_nodes()
        self.map = {}
        
            
  
            