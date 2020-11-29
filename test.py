# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:12:07 2020

@author: hxf
"""

# import jlinkedlist
import unittest
#import copy
import lru


class Test(unittest.TestCase):
    
    lru_cache1 = None
    lru_cache2 = None

    def setUp(self):
        self.lru_cache1 = lru.LRUCache(3)
        self.lru_cache2 = lru.LRUCache(0)
        self.lru_cache3 = lru.LRUCache(1)
        
        
    def test1(self):
        
        self.lru_cache1.put(1,1)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [1], "write the key 1: the result should be [(1, 1)]")
        self.lru_cache1.put(2, 2)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [1, 2], "write the key 2: the result should be [(1, 1), (2, 2)]")
        self.lru_cache1.put(3, 3)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [1, 2, 3], "write the key 3: the result should be [(1, 1), (2, 2), (3, 3)]")
        self.lru_cache1.put(4, 4)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [2, 3, 4], "write the key 3: the result should be [(2, 2), (3, 3), (4, 4)]")
        self.lru_cache1.put(5, 5)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [3, 4, 5], "write the key 3: the result should be [(3, 3), (4, 4), (5, 5)]")
        self.assertEqual(self.lru_cache1.get(0), -1, "read the key 0: the result should be -1 as cache is [(3, 3), (4, 4), (5, 5)]")
        self.assertEqual(self.lru_cache1.get(3), 3, "read the key 3: the result should be 3 as cache is [(4, 4), (5, 5), (3, 3)]")
        self.lru_cache1.put(6,6)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [5, 3, 6], "write the key 6: the result should be [(5, 5), (3, 3), (6, 6)]")
        self.lru_cache1.delete(3)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [5, 6], "delete the key 3: the result should be [(5, 5), (6, 6)]")
        self.assertEqual(self.lru_cache1.get(3), -1, "read the key 3: the result should be -1 as cache is [(5, 5), (6, 6)]")
        self.assertEqual(self.lru_cache1.get(5), 5, "read the key 5: the result should be 5 as cache is [(6, 6), (5, 5)]")
        self.lru_cache1.put(7, 7)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [6, 5, 7], "write the key 6: the result should be [(6, 6), (5, 5), (7, 7)]")
        self.assertEqual(self.lru_cache1.get(5), 5, "read the key 5: the result should be 5 as cache is [(6, 6), (7, 7), (5, 5)]")
        self.assertEqual(self.lru_cache1.get(6), 6, "read the key 6: the result should be 6 as cache is [(7, 7), (5, 5), (6, 6)]")
        self.lru_cache1.put(8, 8)
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [5, 6, 8], "write the key 8: the result should be [(5, 5), (6, 6), (8, 8)]")
        self.lru_cache1.reset()
        self.assertEqual(self.lru_cache1.dlinkedlist_to_list(), [], "reset")
        
    def test2(self):
        self.lru_cache2.put(1,1)
        self.assertEqual(self.lru_cache2.dlinkedlist_to_list(), [], "write the key 1: the result should be []")
        self.lru_cache2.put(2, 2)
        self.assertEqual(self.lru_cache2.dlinkedlist_to_list(), [], "write the key 1: the result should be []")
        self.assertEqual(self.lru_cache2.get(2), -1, "read the key 2: the result should be -1 as cache is []")
        self.assertEqual(self.lru_cache2.get(3), -1, "read the key 3: the result should be 3 as cache is []")
        self.lru_cache2.reset()
        self.assertEqual(self.lru_cache2.dlinkedlist_to_list(), [], "reset")
    
    def test3(self):
        self.lru_cache3.put(1,1)
        self.assertEqual(self.lru_cache3.dlinkedlist_to_list(), [1], "write the key 1: the result should be [(1,1)]")
        self.assertEqual(self.lru_cache3.get(1), 1, "read the key 1: the result should be 1 as cache is [(1,1)]")
        self.lru_cache3.put(2, 2)
        self.assertEqual(self.lru_cache3.dlinkedlist_to_list(), [2], "write the key 3: the result should be [(2,2)]")
        self.assertEqual(self.lru_cache3.get(1), -1, "read the key 1: the result should be -1 as cache is [(2,2)]")
        self.lru_cache3.delete(2)
        self.assertEqual(self.lru_cache3.dlinkedlist_to_list(), [], "delete the key 2: the result should be []")
        self.assertEqual(self.lru_cache3.get(2), -1, "read the key 2: the result should be -1 as cache is []")
        self.assertEqual(self.lru_cache3.get(1), -1, "read the key 3: the result should be -1 as cache is []")
        self.lru_cache3.put(3,3)
        self.assertEqual(self.lru_cache3.dlinkedlist_to_list(), [3], "write the key 1: the result should be [(3,3)]")
        
        self.lru_cache3.reset()
        self.assertEqual(self.lru_cache3.dlinkedlist_to_list(), [], "reset")
        
        self.assertEqual(self.lru_cache3.get(2), -1, "read the key 2: the result should be -1 as cache is []")
        self.assertEqual(self.lru_cache3.get(1), -1, "read the key 3: the result should be -1 as cache is []")
        
        
if __name__ == '__main__':
    unittest.main()
    