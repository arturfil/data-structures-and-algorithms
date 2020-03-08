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
    return (i-1) // 2 # make sure you are using this division since we don't care for float numbers here

  # Insert a new key 'k'
  def insertKey(self, k):
    heappush(self.heap, k)

  # Decrease value of key at index 'i' to new_val
  # It is assumed that the new value is smaller than heap[i]
  def decreaseKey(self, i, new_val):
    self.heap[i] = new_val
    
    while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
      # Swap heap[i] with heap[parent(i)] 
      self.heap[i] , self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i]) 

  # Method to remove minimum element from min heap
  def extractMin(self):
    return heappop(self.heap)
  
  # This method will delte key at index i.
  # first it changes the value to the most negative number which is neg. infinity
  # then uses extractMin()
  def deleteKey(self,i):
    self.decreaseKey(i, float("-inf"))
    self.extractMin()

  # Get the minimum element fromthe heap
  def getMin(self):
    return self.heap[0]

heapObj = MinHeap() 
heapObj.insertKey(3) 
heapObj.insertKey(2) 
heapObj.deleteKey(1) 
heapObj.insertKey(15) 
heapObj.insertKey(5) 
heapObj.insertKey(4) 
heapObj.insertKey(45) 
  
print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.decreaseKey(2, 1) 
print(heapObj.getMin())