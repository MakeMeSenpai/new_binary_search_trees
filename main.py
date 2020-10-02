from bst import Node
from bst import BinarySearchTree

# 8
#3 9 
#   11
node1 = Node(8)
node2 = Node(3)
node3 = Node(9)
node4 = Node(11)

#make Node(8) children Node(3) and Node(9)
node1.left = node2
node1.right = node3

#make Node(11) right child of Node(9)
node3.right = node4
#have built a tree

#search the tree for a target value

#imagine we are searching for 11
root = node1
target = 11
'''if root.data == target:
  print("Found it!")

if root.data > target:
  #look at left child
  if root.left.data == target:
    print("Found it!")

if root.data < target:
  #look at the right ChildProcessError
  if root.right.data == target:
    print("Found it")'''

'''def search(target, node):

  #base case is we found it or nowhere else to look
  if node is None or node.data == target:
    return node
  #recursive case
  if node.data > target:
    #look at the left child
    return search(target, node.left)
  if node.data < target:
    #look a the right child
    return search(target, node.right)


target = 8
result = search(target, root)
print(result)

def insert(node, new_node):
  #base case
  #we have found a node that doesn't have a child on the side we are traversing
  #recursive case
  #find the correct parent and insert there

  if node is None:#if nothing in the tree initially
      node = new_node
      return

  if new_node.data < node.data:

    if node.left is None: #if space on left
      #make the new node the new child
      node.left = new_node
      return
    else:#no space
      #repeat for left child
      #recurse
      insert(node.left, new_node)

  if new_node.data > node.data:
    if node.right is None:
      node.right = new_node
      return
    else:
      insert(node.right, new_node)

insert(root, Node(1))
insert(root, Node(20))
result = search(20, root)
print(result.data)'''

bst = BinarySearchTree()

bst.insert(bst.root, Node(1))
bst.insert(bst.root, Node(4))