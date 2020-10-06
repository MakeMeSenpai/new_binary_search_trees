class Node:

  def __init__(self, data):
    self.data = data

    #left and right will point to other nodes
    self.left = None
    self.right = None

node1 = Node(9)
node2 = Node(3)
node3 = Node(10)

#building the tree
root = node1

node1.left = node2
node1.right = node3

#TODO: add a node with data value 12 to be right child of Node(10)
node4 = Node(12)
node3.right = node4

#search the tree
def search(node, target):
    #base case, stops the recursion
    #1. once we have looked at everything and didn't find it
    #2. we have found it!
    if node is None: #1
        return None
    if node.data == target: #2
        return node
    #recursive case, calls function within itself
    if node.data < target: #go right
        return search(node.right, target)
    else: #go left
        return search(node.left, target)
    

result = search(root, 12)

def insert(node, new_node): 
  if new_node.data > node.data:
    #put new child on right if space
    if node.right is None:
      node.right = new_node
      return
    #otherwise keep looking
    else:
      insert(node.right, new_node)
  if new_node.data < node.data:
    #put new child on the left if space
    if node.left is None:
      node.left = new_node
      return
    #otherwise keep looking
    else:
      insert(node.left, new_node)

insert(root, Node(4))

#print(node2.right.data)

#TODO: Trees assignment
#Make a video explaining search and insert

#Extra credit
#write and explain delete(node, target)

#TODO: explain in order traversal in video

def in_order_traversal(node):
  if node is not None:
    #traverse
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
  else:
    return None

in_order_traversal(root)
#Extra credit write and explain pre order and post order