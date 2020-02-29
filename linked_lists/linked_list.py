# A linked list is a datasctructure that links Node objects.
# A node is a class that has two properties, the value and the pointer 'next'

# Pros:
  # - Linked list allow constant time insertion and deletions compared to an array
  # - Therefore it comes more useful to use a linked list instead of an array in the case that you have to 
  # add or delete values constantly

# Cons:
  # - To access an element you will have to traverse through the linked list in O(k) time to the Kth element
  # - Here arrays are more useful to access indexes if they are not meant to be deleted or updated frequently
class Node(object):
  def __init__ (self, value):
    self.value = value
    self.next = None

# Creating the nodes
a = Node(1)
b = Node(2)
c = Node(3)

# assigning the pointers 
a.next = b
b.next = c

# printing other node's value from current node
print(a.next.value)