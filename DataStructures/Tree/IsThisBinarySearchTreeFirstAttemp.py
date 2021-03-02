""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import sys
def check_order(root):
    result = True
    if root.left and root.right:
        result = (root.left.data < root.data) and (root.right.data > root.data) and check_order(root.left) and check_order(root.right) and check_nodes(root.left, root.data,'left') and check_nodes(root.right,root.data,'right')
    elif root.left and not root.right:
        result = (root.left.data < root.data) and check_order(root.left) and check_nodes(root.left, root.data,'left')
    elif root.right and not root.left:
        result = (root.right.data > root.data) and check_order(root.right) and check_nodes(root.right,root.data,'right')
    else:
        result = True
        
    return result


def check_nodes(root, data, operation):
    result = True 
    if root.left and root.right:
        result = check_nodes(root.left, data,operation) and check_nodes(root.right, data,operation)
    elif root.left and not root.right:
        result = check_nodes(root.left, data,operation)
    elif root.right and not root.left:
        result = check_nodes(root.right, data,operation)
    else:  
        if operation == 'left':
            result = root.data < data
        else:
            result = root.data > data
    
    return result
        
        
def check_binary_search_tree_(root):
    return check_order(root)
    
    