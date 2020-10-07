#!python3

# Binary Tree Example
class Node:
   def __init__(self, data):
     self.data = data
     # left and right attributes
     self.left = None
     self.right = None


# creating our nodes
node1 = Node(4)
node2 = Node(2)
node3 = Node(6)
node4 = Node(1)
node5 = Node(3)
node6 = Node(5)

# building our tree
root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6


# search the tree
def search(node, target):
  if node is None: # checks if there are no items left to search
    return None
  elif node.data == target: # checks if the node is our target
    return node
  elif node.data < target: # go right
    return search(node.right, target)
  else: # go left
    return search(node.left, target)

"""The function will recursively calls itself and check if the value is higher or lower then what we are looking for. For example, we call the function looking for 5. The funcion will figure out that our root node(node1.data == 4) is too small, and therefore go right as a result. Then when it reads our node3.data, it will determine that it is less than 6, and go left as a result. Finally finding 5, and returning the result."""
result = search(root, 5)


# now lets insert a new node into our tree
node7 = Node(7)
def insert(node, new_node):
  if new_node.data > node.data:
    # put new child on right if space
    if node.right is None:
      node.right = new_node
      return
    # otherwise keep looking
    else:
      insert(node.right, new_node)
  if new_node.data < node.data:
    # put new child on the left if space
    if node.left is None:
      node.left = new_node
      return
    # otherwise keep looking
    else:
      insert(node.left, new_node)

"""Here we created a Node with the value of 7. This function will recursively call itself until it finds an open spot for 7 -that makes sense in the database. Simularly to our search funtion, it will check -if it cannot find an empty space for our node- if our node's value/data belongs on the left or right side based on how big it is. You can choose any node to try and insert to, but for this example we have used the root node to cycle threw the entire tree."""
insert(root, node7)
insert(root, Node(8))


def delete(node, target):
  result = search(node, target - 1)
  if result.left == target:
    result.left = None
  elif result.right == target:
    result.right = None
  # does a second search to try and find a parent node
  result = search(node, target + 1)
  if result.left == target:
    result.left = None
  elif result.right == target:
    result.right = None
  # else, we print a not found response
  else:
    print(f"Could not find {target} in Tree.")

"""Here we take advantage of our search function in order to find the previous node. Becuase we are trying to delete 8, we have to look for the node with a value of 7. Note that if we were looking for 5, we would have to look for the parenting node, with a value of 6. As well, this example only works for integer based binary trees."""
delete(root, 8)


# Finally we can print our tree out.
def in_order_traversal(node):
  if node is not None:
    #traverse
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
  else:
    return None
in_order_traversal(root)
