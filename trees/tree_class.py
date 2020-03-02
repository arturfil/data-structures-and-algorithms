'''
This is the Tree Class data structure
What this allows compared to a linked list (where both this and the linked list use pointers)
is that the search process is much faster since the data is organized in a binary way, this allows to 
have a O(logn) time of search which is really fast
'''

class BinaryTree(object):

  def __init__(self,root):
    self.key = root
    self.leftChild = None
    self.rightChild = None

  def inserLeft(self, Node):
    if self.leftChild == None:
      self.leftChild = BinaryTree(Node)
    else:
      t = BinaryTree(Node)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRight(self, Node):
    if self.rightChild == None:
      self.rightChild = BinaryTree(Node)
    else:
      t = BinaryTree(Node) 
      t.rightChild = self.rightChild
      self.rightChild = t
  
  def getRightChild(self):
    return self.rightChild

  def getLeftChild(self):
    return self.leftChild

  def setRootChild(self, obj):
    self.key = obj

  def getRootVal(self):
    return self.key

  def printTree(self):
    pass

# Creating Binary tree and testing methods

# UNCOMMENT FOR TESTING


r = BinaryTree('a')
print(r.getRootVal())

r.insertRight('z')
r.setRootChild('b')
print(f'Root is {r.getRootVal()}')
print(f'Right child is {r.getRightChild().getRootVal()}')



# Tree traversal, in-order, pre-order, post-order

'''
[Notice that the tree is printed sideways, root is 4]
[Common rule for binary tree is that left side values are lower than "parent" node and right side values are bigger than parent node]
[Notice though how all the left values of the root are lower and all right values are higher than the root, that way the rule is kept]

          8
        6
      /   5
    4
      \   3
        2
          1

In order traversal would be visiting node 4, 2, 1, 3, 6, 5, 8
'''
def preOrder(tree):
  if tree:
    print(tree.getRootVal())
    preOrder(tree.getLeftChild())
    preOrder(tree.getRightChild())

def inOrder(tree):
  if tree != None:
    inOrder(tree.getLeftChild())
    print(tree.getRootVal())
    inOrder(tree.getRightChild())

def postOrder(tree):
  if tree != None:
    postOrder(tree.getLeftChild())
    postOrder(tree.getRightChild())
    print(tree.getRootVal())

postOrder(r)