# lru_cache

Implement a "Least-Recently Used" (LRU) Cache using **python**

To install python: https://www.python.org/downloads/

To run the unit test: ```python test.py ```

Complexity Analysis:

- for **put** and **get**:
  - time: O(1) since insert node to a fixed position in the doubly linked list and add pair into hash map only need O(1) time
  - space: O(capacity) since we need to keep the doubly linked list and hash map whose size is up to capacity + 2

- for **delete**:
  - time: O(1) since delete the pair from hash map only need O(1) time, and  we can access the specific node by getting the value of the hashmap, and so delete that node only needs O(1) time as well
  - space: O(1) 
  
- for **reset**:
  - time: O(n) since remove all nodes in the doubly linked list needs O(n) time, and clean the hash map only needs O(1) time.
  - space: O(1) since no extra memory is used when space is cleared

