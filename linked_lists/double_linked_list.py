# Here just as the name suggest, the list has a pointer to the next and previous node which allows for faster search of values
# But is the same amount of time to delte or insert

class DoubleNode(object):
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None

a = DoubleNode("Head")
b = DoubleNode("First")
c = DoubleNode("Second")
d = DoubleNode("Tail")

a.next = b
b.next = c
b.prev = a
c.next = d


print(c.next.value)
print(b.next.value)
print(b.prev.value)