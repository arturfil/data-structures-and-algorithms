# Smilar to queue, deque is like a combinations of stack and queue where you can add either at the front or back 
# - And also can add either to the front or back

class Deque(object):

  def __init__ (self):
    self.items = []

  def isEmtpy(self):
    return self.items == []
  
  def addFront(self, item):
    self.items.append(item)
  
  def addRear(self, item):
    self.items.insert(0, item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

d = Deque()
d.addFront("Hello")
d.addRear("Back")
print(d.size())