class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child=None
        self.right_child=None
        self.parent=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root==None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value<current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent=current_node # set parent
            else: 
                self._insert(value,current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent=current_node # set parent
            else:
                self._insert(value,current_node.right_child)

        else: 
            print("Value already in tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(f'{current_node.value}')
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0) 
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node==None: return current_height
        left_height=self._height(current_node.left_child,current_height+1)        
        right_height=self._height(current_node.right_child,current_height+1)        
        return max(left_height, right_height)

    # Returns actual value
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value==current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)
    
    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # returns the node with min value int tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child != None:
                current = current.left_child
            return current
        
        # returns thenumber of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child != None: num_children+=1
            if n.right_child != None: num_children+=1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent
        node_children = num_children(node)

        # break operation into different cases based on the stuct of the tree & node to b deleted
        
        # Case 1 (node has no children)
        if node_children == 0:

            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # Case 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else: 
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else: 
                node_parent.right_child = child

            # correct the parent pointer in child
            child.parent=node_parent

        # Case 3 (node has two children)
        if node_children == 2:

            # get the inorder succesor of the deleted node
            succesor = min_value_node(node.right_child)

            # copy the inorder succesor's value to the node formerly
            # holding the value we wished to delete
            node.value = succesor.value

            # delte the inorder succesor noe htat it's value was
            # copied into the other node
            self.delete_node(succesor)


    # Return True or False if exists
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        return False

# Function to randomly fill in a tree
def fill_tree(tree, nums_elems=100, max_int=1000):
    from random import randint
    for _ in range(nums_elems):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree



# Code to test the binary search tree
tree = BinarySearchTree()

'''tree = fill_tree(tree)'''

tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(5)
tree.insert(8)
tree.insert(20)
tree.insert(12)

tree.print_tree()

print(f'Tree height is {tree.height()}')

'''
print(tree.search(20))
print(tree.search(10))
'''

tree.delete_value(8)
tree.print_tree()