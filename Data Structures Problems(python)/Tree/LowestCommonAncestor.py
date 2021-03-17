

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, a, b):
  node = root
  while node:
    if max(a, b) < node.info:
      node = node.left
    elif min(a, b) > node.info:
      node = node.right
    else:
      break
  return node

