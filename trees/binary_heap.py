'''
  - Binary Heaps are more strict binary trees (trees have to be balanced). 
  - Balanced tree means that the tree inserts and arranges nodes in order 
    for the tree to go to a new level.
  - There are max binary heaps and min binary heaps 
  - where either the largest value is at the root (max_heap) or the lowest 
    value is at the root (min_heap)
  - Binary heaps are good for searching, inserting or Deleting
  - Seach are Constant time and removing or inserting are O(logn) (which is pretty good)

  * To get the full reference go to GeeksForGeeks and search binary heap

  - Heaps can be implemented to sort or to use as priority queues (queues with a priority tweak)
'''
from heapq import heappush, heappop, heapify

class MinHeap:
  def __init__(self):
    self.heap = []

  def parent(self, i):
    return (i-1) / 2

  # Insert a new key 'k'
  def insertKey(self, k):
    # heappush(self.heap, k)
    pass

def greeting(name):
  return f"Hello {name}"
  