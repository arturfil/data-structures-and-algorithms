# Implementing out own stack datastructure
# A very common way to think about stacks is that you have to picture a stack of books and in order to get the one in the middle first you have to take
# all of the other books on top of the desired one.
# So in the same way, the stack structure only allows the utilization of the top most stored data.

class Stack(object):
  def __init__ (self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

s = Stack()

print(s.isEmpty())

s.push(1)
s.push("two")
print(s.peek())
print(s.size())
print(s.isEmpty())
s.pop()
print(s.peek())