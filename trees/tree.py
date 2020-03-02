# simple implementation of a tree: List of Lists aka [[1,2,4],[2,4,5],[2,3,4]]. This could also be refered as a matrix
# I don't particularly like this way of making a binary tree, I prefer using a close with Root LeftNode & RightNode

def BinaryTree(r):
  return [r,[],[]]

def insertLeft(root, newBranch):
  t = root.pop(1)

  if len(t) > 1:
    root.insert(1, [newBranch,t,[]])
  else:
    root.insert(1,[newBranch,[],[]])

  return root

def insertRight(root, newBranch):
  t = root.pop(2)

  if len(t) > 1:
    root.insert(2, [newBranch, [],t])
  else:
    root.insert(2,[newBranch,[],[]])

  return root

def getRootVal(root):
  return root[0]

def setRootVal(root, newVal):
  root[0] = newVal

def getLeftChild(root):
  return root[1]

def getRightChild(root):
  return root[2]

r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r,5)
insertRight(r,6)
print(insertRight(r,7))
l = getLeftChild(r)
setRootVal(l,9)
print(r)
