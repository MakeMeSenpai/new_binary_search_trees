class Node:
  #building circle with number

  def __init__(self, data):
    self.data = data
    #left and right will point to another node
    self.left = None
    self.right = None 


class BinarySearchTree:
  
  def __init__(self):
    self.root = None #assuming this will become a Node() at some point

  def insert_helper(self, node, new_node):
    if new_node.data < node.data:

      if node.left is None: #if space on left
        #make the new node the new child
        node.left = new_node
        return
      else:#no space
        #repeat for left child
        #recurse
        self.insert_helper(node.left, new_node)

    if new_node.data > node.data:
      if node.right is None:
        node.right = new_node
        return
      else:
        self.insert_helper(node.right, new_node)

  def insert(self, node, new_node):
    #base case
    #we have found a node that doesn't have a child on the side we are traversing
    #recursive case
    #find the correct parent and insert there

    if self.root is None:#if nothing in the tree initially
        self.root = new_node
        return

    #self.insert_helper(self.root, new_node)
    if new_node.data < node.data:

      if node.left is None: #if space on left
        #make the new node the new child
        node.left = new_node
        return
      else:#no space
        #repeat for left child
        #recurse
        self.insert_helper(node.left, new_node)

    if new_node.data > node.data:
      if node.right is None:
        node.right = new_node
        return
      else:
        self.insert_helper(node.right, new_node)