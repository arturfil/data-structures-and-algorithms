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
    print(tree)

def inOrder():
  pass

def postOrder():
  pass
