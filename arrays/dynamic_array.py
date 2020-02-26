
# Creating and Implementing the dynamic array ourselves using the 
#   c type library built in and using objects with public and private methods
import ctypes

class DynamicArray(object):
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def __getitem__(self, k):
    if not 0 <= k < self.n:
      return IndexError('K is out of bounds!')

    return self.A[k]

  def append(self, ele):
    if self.n == self.capacity:
      # if capacity is full increase capacity twice its size
      self._resize(2*self.capacity) 

    self.A[self.n] = ele
    self.n +=1

  def _resize(self, new_cap):
    B = self.make_array(new_cap)
    # pointing values of Array 'A' into 'B'
    # Once we have new values in B plus the doubled capacity, we assign self.A = B. Basically B was an array place holder ( a temp )
    for k in range(self.n):
      B[k] = self.A[k]
    
    self.A = B
    self.capacity =  new_cap

  def make_array(self, new_cap):
    # here we are using a C library to make a pointer. (C language)
    return (new_cap * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[0])

    
