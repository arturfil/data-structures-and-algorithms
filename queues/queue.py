# Queue, similar to the stack but First in - First out
class Queue(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []
  
  def enqueue(self,item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
    
q = Queue()
print(q.size())
q.enqueue(1)
q.enqueue(2)
q.enqueue("This is a string")
print(q.size())
